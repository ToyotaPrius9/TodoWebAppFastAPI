from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from typing import List, Optional
from fastapi.middleware.cors import CORSMiddleware

# Create a FastAPI instance
app = FastAPI()

# Database URL 
DATABASE_URL = "sqlite:///./todotodo.db"

# SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a SQLAlchemy Base class
Base = declarative_base()

# Define Task model using SQLAlchemy ORM
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    completed = Column(Boolean, default=False)

# Create all tables in the database
Base.metadata.create_all(bind=engine)

# Pydantic model for Task
class TaskCreate(BaseModel):
    text: str

class TaskResponse(BaseModel):
    id: int
    text: str
    completed: bool

# CORS (Cross-Origin Resource Sharing) configuration
origins = [
    "http://localhost:3000",  # Allow requests from the frontend URL
    # Add more origins as needed
]

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Endpoint to create a new task
@app.post("/tasks/", response_model=TaskResponse)
def create_task(task: TaskCreate):
    db = SessionLocal()
    db_task = Task(text=task.text)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# Endpoint to list all tasks
@app.get("/tasks/", response_model=List[TaskResponse])
def read_tasks(skip: int = 0, limit: int = 10):
    db = SessionLocal()
    tasks = db.query(Task).offset(skip).limit(limit).all()
    return tasks

# Endpoint to delete a task
@app.delete("/tasks/{task_id}/")
def delete_task(task_id: int):
    db = SessionLocal()
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
        return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")
