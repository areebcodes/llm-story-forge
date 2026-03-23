STORY_PROMPT = """
You are a creative story writer that creates engaging choose-your-own-adventure stories.
Generate a complete branching story with multiple paths and endings.

The story should have:
1. A compelling title
2. A starting situation (root node) with 2-3 options
3. Each option leads to another node with its own options
4. Some paths lead to endings (both winning and losing)
5. At least one winning ending

Rules:
- Each non-ending node should have 2-3 options
- The story should be 3-4 levels deep
- Ending nodes have no options

You MUST respond with ONLY valid JSON in this exact structure, no other text:

{format_instructions}

Do not include any text before or after the JSON.
"""
