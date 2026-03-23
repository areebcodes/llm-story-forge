from sqlalchemy.orm import Session

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

from core.prompts import STORY_PROMPT
from models.story import Story, StoryNode
from core.models import StoryLLMResponse, StoryNodeLLM
from dotenv import load_dotenv
import os
import json
import re

load_dotenv()

MAX_RETRIES = 3


class StoryGenerator:

    @classmethod
    def _get_llm(cls):
        return ChatGroq(model="llama-3.3-70b-versatile", api_key=os.getenv("GROQ_API_KEY"))

    @classmethod
    def _extract_json(cls, text: str) -> dict:
        """Try to extract and parse JSON from the model's response text."""
        text = re.sub(r"```json\s*", "", text)
        text = re.sub(r"```\s*", "", text)
        text = text.strip()

        try:
            return json.loads(text)
        except json.JSONDecodeError:
            pass

        match = re.search(r'\{.*\}', text, re.DOTALL)
        if match:
            try:
                return json.loads(match.group())
            except json.JSONDecodeError:
                pass

        raise ValueError(f"Could not extract valid JSON from response: {text[:300]}")

    @classmethod
    def generate_story(cls, db: Session, session_id: str, theme: str = "fantasy") -> Story:
        llm = cls._get_llm()
        story_parser = PydanticOutputParser(pydantic_object=StoryLLMResponse)

        prompt = ChatPromptTemplate.from_messages([
            ("system", STORY_PROMPT),
            ("human", f"Create the story with this theme: {theme}")
        ]).partial(format_instructions=story_parser.get_format_instructions())

        last_error = None

        for attempt in range(1, MAX_RETRIES + 1):
            try:
                raw_response = llm.invoke(prompt.invoke({}))
                response_text = raw_response.content if hasattr(raw_response, "content") else str(raw_response)

                story_data = cls._extract_json(response_text)
                story_structure = StoryLLMResponse.model_validate(story_data)

                story_db = Story(title=story_structure.title, session_id=session_id)
                db.add(story_db)
                db.flush()

                root_node_data = story_structure.rootNode
                if isinstance(root_node_data, dict):
                    root_node_data = StoryNodeLLM.model_validate(root_node_data)

                cls._process_story_node(db, story_db.id, root_node_data, is_root=True)

                db.commit()
                return story_db

            except Exception as e:
                last_error = e
                db.rollback()
                if attempt < MAX_RETRIES:
                    continue

        raise RuntimeError(f"Failed to generate story after {MAX_RETRIES} attempts. Last error: {last_error}")

    @classmethod
    def _process_story_node(cls, db: Session, story_id: int, node_data: StoryNodeLLM, is_root: bool = False) -> StoryNode:
        node = StoryNode(
            story_id=story_id,
            content=node_data.content if hasattr(node_data, "content") else node_data["content"],
            is_root=is_root,
            is_ending=node_data.isEnding if hasattr(node_data, "isEnding") else node_data["isEnding"],
            is_winning_ending=node_data.isWinningEnding if hasattr(node_data, "isWinningEnding") else node_data["isWinningEnding"],
            options=[]
        )
        db.add(node)
        db.flush()

        if not node.is_ending and (hasattr(node_data, "options") and node_data.options):
            options_list = []
            for option_data in node_data.options:
                next_node = option_data.nextNode

                if isinstance(next_node, dict):
                    next_node = StoryNodeLLM.model_validate(next_node)

                child_node = cls._process_story_node(db, story_id, next_node, False)

                options_list.append({
                    "text": option_data.text,
                    "node_id": child_node.id
                })

            node.options = options_list

        db.flush()
        return node
