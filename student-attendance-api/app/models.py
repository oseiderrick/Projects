from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, Index
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

    attendances = relationship("Attendance", back_populates="student")
    __table_args__ = (
        Index("ix_students_name", "first_name", "last_name"),
    )

class Attendance(Base):
    __tablename__ = "attendance"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), index=True)
    date = Column(Date, index=True)
    status = Column(String)  # "present" | "absent" | "late"
    created_at = Column(DateTime, default=datetime.utcnow, index=True)

    student = relationship("Student", back_populates="attendances")
    __table_args__ = (
        Index("ix_attendance_student_date", "student_id", "date"),
    )
