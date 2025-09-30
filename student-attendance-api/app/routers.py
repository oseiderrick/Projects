from fastapi import APIRouter, Depends, HTTPException, Cookie, Query
from sqlalchemy.orm import Session
from .db import SessionLocal, engine
from .models import Base, Student, Attendance
from .schemas import StudentCreate, StudentOut, AttendanceCreate, AttendanceOut
from .auth import get_current_user, COOKIE_NAME

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine)

@router.get("/students", response_model=list[StudentOut])
def list_students(page: int = Query(1, ge=1), limit: int = Query(20, ge=1, le=100), db: Session = Depends(get_db)):
    offset = (page - 1) * limit
    return db.query(Student).order_by(Student.id).offset(offset).limit(limit).all()

@router.post("/students", response_model=StudentOut)
def create_student(body: StudentCreate, db: Session = Depends(get_db)):
    s = Student(first_name=body.first_name, last_name=body.last_name, email=body.email)
    db.add(s); db.commit(); db.refresh(s)
    return s

@router.get("/attendance", response_model=list[AttendanceOut])
def list_attendance(date: str | None = None, page: int = Query(1, ge=1), limit: int = Query(50, ge=1, le=200), db: Session = Depends(get_db)):
    q = db.query(Attendance)
    if date:
        q = q.filter(Attendance.date == date)
    offset = (page - 1) * limit
    return q.order_by(Attendance.id).offset(offset).limit(limit).all()

@router.post("/attendance", response_model=AttendanceOut)
def create_attendance(body: AttendanceCreate, db: Session = Depends(get_db), access_token: str | None = Cookie(default=None, alias=COOKIE_NAME)):
    user = get_current_user(access_token)
    # user is validated; proceed
    a = Attendance(student_id=body.student_id, date=body.date, status=body.status)
    db.add(a); db.commit(); db.refresh(a)
    return a
