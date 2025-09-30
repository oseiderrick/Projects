from fastapi import FastAPI
from .routers import router
from .auth import router as auth_router

app = FastAPI(title="Student Attendance API", version="1.0.0")
app.include_router(auth_router)
app.include_router(router)
