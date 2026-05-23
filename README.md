This is an all-in-one platform designed to centralize language learning tools, inspired by personal experience to make robust language acquisition more efficient and organized.

This is a beginner project, and the code is not perfect. I am still learning and improving my skills. If you have any suggestions or feedback, please feel free to reach out to me.

## Tech Stack
Frontend: Vite, React, TypeScript

Backend: Python, FastAPI, Uvicorn

## Prerequisites
Before you begin, ensure you have the following installed:

Node.js (latest LTS)

Python 3.10+

## Installation & Setup
### 1. Backend (FastAPI)

```bash
cd app_project
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```
### 2. Frontend (Vite/React)

```bash
cd ../frontend
npm install
```

### Start the Backend:

```bash
cd app_project
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uvicorn app:app --reload
```
### Start the Frontend:

```bash
cd ../frontend
npm run dev
```

Proceed to http://localhost:5173 to access the application.

Note: Remember to create your .env file based on .env.example before running the services.
Ensure you have the necessary API keys and configurations set up.

### API requirements:
- OpenAI API key.
Put your key in the .env file as follows:
```bash
API_KEY=your_openai_api_key_here
```