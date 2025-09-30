Student Attendance API

Overview
A production-ready FastAPI service for managing students and attendance with JWT auth, pagination, and connection pooling. Matches the resume bullet: "Boosted query efficiency 30%… designing a REST API with indexed queries, pagination, and connection pooling for large cohorts."

Quickstart
1) Python 3.11+ recommended
2) pip install -r requirements.txt
3) uvicorn app.main:app --reload

Auth (JWT, HTTP-only cookies)
- POST /auth/register
- POST /auth/login
- POST /auth/logout

Core Endpoints
- GET /students?page=1&limit=20
- POST /students
- GET /attendance?date=YYYY-MM-DD&page=1&limit=50
- POST /attendance (mark attendance for a student)

Tech
- FastAPI, SQLAlchemy (SQLite by default), PyJWT
- Indexed tables, pagination helpers, connection pooling (SQLAlchemy engine pool)
- CI-ready (pytest), Dockerfile

License
MIT
