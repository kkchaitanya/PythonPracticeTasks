
import os
import socket
from contextlib import asynccontextmanager

import redis
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import text

from database import Base, engine, SessionLocal
from models import Course


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="Docker FastAPI Masterclass",
    lifespan=lifespan
)


class CourseCreate(BaseModel):
    name: str
    price: float


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {
        "message": "FastAPI running inside Docker",
        "container": socket.gethostname(),
        "environment": os.getenv("APP_ENV", "development")
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/ready")
def ready(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"database": "connected"}
    except Exception:
        raise HTTPException(503, "Database unavailable")


@app.post("/courses")
def create_course(
    data: CourseCreate,
    db: Session = Depends(get_db)
):
    course = Course(name=data.name, price=data.price)
    db.add(course)
    db.commit()
    db.refresh(course)

    return {
        "id": course.id,
        "name": course.name,
        "price": course.price
    }


@app.get("/courses")
def list_courses(db: Session = Depends(get_db)):
    return db.query(Course).order_by(Course.id).all()


@app.delete("/courses/{course_id}")
def delete_course(
    course_id: int,
    db: Session = Depends(get_db)
):
    course = db.get(Course, course_id)

    if course is None:
        raise HTTPException(404, "Course not found")

    db.delete(course)
    db.commit()
    return {"message": "Course deleted"}


@app.get("/cache-demo")
def cache_demo():
    client = redis.Redis(
        host=os.getenv("REDIS_HOST", "redis"),
        port=6379,
        decode_responses=True
    )

    visits = client.incr("visits")

    return {
        "total_visits": visits,
        "container": socket.gethostname()
    }