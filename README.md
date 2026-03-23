⚔️ Areeb's LLM Story Forge
An AI-powered, full-stack choose-your-own-adventure story generator. Enter any theme and a large language model generates a complete branching narrative with multiple paths and endings — in seconds.
🔗 Live Demo: coming soon
📦 Backend API: coming soon

✨ Features

🤖 LLM-generated stories — powered by Meta's LLaMA 3 via the Groq API
🌿 Branching narratives — every story has multiple paths and endings
⚡ Async job processing — story generation runs as a background job with real-time polling
🗄️ Persistent storage — all stories and nodes saved to a database
🎨 Dark fantasy UI — custom-designed frontend with a moody forest aesthetic
📱 Fully responsive — works on desktop and mobile


🛠️ Tech Stack
Backend
TechnologyPurposePython 3.13Core backend languageFastAPIREST API framework with automatic OpenAPI docsSQLAlchemyORM for database modeling and queriesSQLiteLightweight relational databaseLangChainLLM orchestration and prompt managementLangChain-GroqGroq API integration for LLaMA 3 inferencePydanticData validation and structured LLM output parsingUvicornASGI server for running FastAPIPython-dotenvEnvironment variable management
Frontend
TechnologyPurposeReact 18Component-based UI frameworkViteLightning-fast frontend build toolReact Router v6Client-side routing and navigationAxiosHTTP client for API communicationCSS3Custom styling with CSS variables and animations
AI / LLM
TechnologyPurposeGroq APIUltra-fast LLM inference engineLLaMA 3.1 8BMeta's open-source large language modelPydantic Output ParsersStructured JSON extraction from LLM responsesPrompt EngineeringCustom system prompts for consistent story structure
Dev Tools & Practices

RESTful API design with proper status codes and error handling
Async background jobs with polling pattern
Environment-based configuration (no hardcoded secrets)
Git version control with clean commit history
VS Code development environment


🏗️ Architecture
┌─────────────────┐         ┌──────────────────────────────────┐
│                 │  HTTP   │           FastAPI Backend         │
│  React Frontend │ ──────► │                                  │
│    (Vite)       │         │  ┌─────────┐    ┌─────────────┐  │
│                 │ ◄────── │  │ Routers │───►│   SQLite DB │  │
└─────────────────┘  JSON   │  └─────────┘    └─────────────┘  │
                            │       │                           │
                            │       ▼                           │
                            │  ┌──────────────────┐            │
                            │  │  StoryGenerator   │            │
                            │  │  (LangChain)      │            │
                            │  └──────────────────┘            │
                            │       │                           │
                            │       ▼                           │
                            │  ┌──────────────────┐            │
                            │  │    Groq API       │            │
                            │  │  (LLaMA 3.1 8B)  │            │
                            │  └──────────────────┘            │
                            └──────────────────────────────────┘

🚀 Running Locally
Prerequisites

Python 3.13+
Node.js 18+
A free Groq API key

Backend
bashcd backend
pip install -r requirements.txt
Create a .env file in the backend/ directory:
GROQ_API_KEY=your_groq_api_key_here
DATABASE_URL=sqlite:///./databse.db
ALLOWED_ORIGINS=http://localhost:5173
bashuvicorn main:app --reload
API runs at http://localhost:8000
Auto-generated docs at http://localhost:8000/docs
Frontend
bashcd frontend
npm install
npm run dev
App runs at http://localhost:5173

📁 Project Structure
llm-story-forge/
├── backend/
│   ├── core/
│   │   ├── config.py          # App settings via Pydantic
│   │   ├── models.py          # LLM response models
│   │   ├── prompts.py         # System prompts for LLM
│   │   └── story_generator.py # LangChain + Groq logic
│   ├── db/
│   │   └── database.py        # SQLAlchemy setup
│   ├── models/
│   │   ├── story.py           # Story & StoryNode DB models
│   │   └── job.py             # Background job DB model
│   ├── routers/
│   │   ├── story.py           # Story endpoints
│   │   └── job.py             # Job status endpoints
│   ├── schemas/
│   │   ├── story.py           # Pydantic request/response schemas
│   │   └── job.py             # Job schemas
│   └── main.py                # FastAPI app entry point
└── frontend/
    └── src/
        ├── components/
        │   ├── StoryGenerator.jsx  # Theme input + job polling
        │   ├── StoryGame.jsx       # Interactive story UI
        │   ├── StoryLoader.jsx     # Story fetching wrapper
        │   ├── ThemeInput.jsx      # Theme form
        │   └── LoadingStatus.jsx   # Loading state
        ├── App.jsx                 # Router setup
        └── App.css                 # Full custom styling

👤 Author
Areeb Khan — @areebcodes
