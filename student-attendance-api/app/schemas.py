from pydantic import BaseModel, EmailStr
from datetime import date

class StudentCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr

class StudentOut(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    class Config:
        from_attributes = True

class AttendanceCreate(BaseModel):
    student_id: int
    date: date
    status: str

class AttendanceOut(BaseModel):
    id: int
    student_id: int
    date: date
    status: str
    class Config:
        from_attributes = True
