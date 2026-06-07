This is an all-in-one platform designed to centralize language learning tools, inspired by personal experience to make robust language acquisition more efficient and organized.

This is a beginner project, and the code is not perfect. I am still learning and improving my skills. If you have any suggestions or feedback, please feel free to reach out to me.

## Tech Stack
Frontend: Vite, React, TypeScript

Backend: Python, FastAPI, Uvicorn

Database: PostgreSQL 18

## Prerequisites
Before you begin, ensure you have the following installed:

Node.js (latest LTS)

Python 3.10+

PostgreSQL 18

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

### 3. Database Setup

Ensure PostgreSQL is installed and running. Create a new database and user for the application, then run the following query to create the table:

```sql
CREATE TABLE chat_logs (
    id SERIAL PRIMARY KEY,
    prompt TEXT NOT NULL,
    response TEXT NOT NULL
);
```
### Make sure the DB is up and running before starting the backend, as the backend will attempt to connect to the database on startup.


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

### env. requirements:
- OpenAI API key.
Put your key in the .env file as follows:
```bash
# Database Configuration
DB_USER=your_postgres_user
DB_PASSWORD=your_postgres_password
DB_NAME=your_database_name
DB_HOST=localhost

# API Keys
API_KEY=your_openai_api_key_here
```