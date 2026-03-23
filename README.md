# ⚔️ Areeb's LLM Story Forge

An AI-powered, full-stack choose-your-own-adventure story generator. Enter any theme and a large language model generates a complete branching narrative with multiple paths and endings — in seconds.

🔗 **Live Demo:** (https://llm-story-forge.vercel.app/) | 📦 **Backend API:** (https://llm-story-forge.onrender.com/docs)

---

## ✨ Features

- 🤖 LLM-generated stories powered by Meta's LLaMA 3 via the Groq API
- 🌿 Branching narratives with multiple paths and endings
- ⚡ Async job processing with real-time polling
- 🗄️ Persistent storage with SQLite
- 🎨 Custom dark fantasy UI
- 📱 Fully responsive

---

## 🛠️ Tech Stack

**Backend:** Python 3.13 · FastAPI · SQLAlchemy · SQLite · LangChain · LangChain-Groq · Pydantic · Uvicorn

**Frontend:** React 19 · Vite · React Router v6 · Axios · CSS3

**AI / LLM:** Groq API · LLaMA 3.1 8B · Pydantic Output Parsers · Prompt Engineering

**Practices:** RESTful API design · Async background jobs · Git · Environment-based config

---

## 🚀 Running Locally

**Prerequisites:** Python 3.13+ · Node.js 18+ · [Groq API key](https://console.groq.com)

**Backend**
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Create `backend/.env`:

```
GROQ_API_KEY=your_key_here
DATABASE_URL=sqlite:///./databse.db
ALLOWED_ORIGINS=http://localhost:5173
```

**Frontend**
```bash
cd frontend
npm install
npm run dev
```

---

## 👤 Author

**Areeb Khan** — [@areebcodes](https://github.com/areebcodes)
