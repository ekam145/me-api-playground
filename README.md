# Me API Playground

A personal backend API that exposes my profile, skills, and projects using
Flask and a relational SQL database (SQLite).

This project demonstrates database design, API development, and query-based
data access.

---

## Tech Stack

- Backend: Flask (Python)
- Database: SQLite (SQL)
- ORM: SQLAlchemy
- Frontend: Minimal HTML + Fetch API

---

## Database Schema

The database uses a normalized relational schema.

Tables:
- profile
- skills
- projects
- project_skills (many-to-many)
- links

The raw SQL schema is available in `schema.sql`.

---

## API Endpoints

### Health Check

GET /health

Returns 200 OK if the service is running.

---

### Get All Projects

GET /projects


Returns a list of all projects.

---

### Filter Projects by Skill

GET /projects?skill=python


Returns projects associated with the given skill.

---

## Local Setup

```bash
git clone <repo-url>
cd me-api-playground
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python seed.py
python run.py


Server runs on:

http://127.0.0.1:5000
