from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from pydantic import BaseModel
from contextlib import asynccontextmanager
import time
import logging
import models
import db_functions
from database import engine, get_db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    max_retries = 5
    retry_interval = 2
    
    for attempt in range(max_retries):
        try:
            models.Base.metadata.create_all(bind=engine)
            logger.info("Database tables created successfully")
            break
        except Exception as e:
            if attempt < max_retries - 1:
                logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {retry_interval}s...")
                time.sleep(retry_interval)
            else:
                logger.error(f"Failed to create tables after {max_retries} attempts")
                raise
    
    yield

app = FastAPI(title="Simple FastAPI app", lifespan=lifespan)

class UserCreate(BaseModel):
    name: str
    email: str

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI with MySQL!"}

@app.get("/users")
def read_users(db: Session = Depends(get_db)):
    users = db_functions.get_users(db)
    return {"users": [{"id": user.id, "name": user.name, "email": user.email} for user in users]}

@app.post("/users")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = db_functions.create_user(db=db, name=user.name, email=user.email)
    return {"message": "User created", "user": {"id": new_user.id, "name": new_user.name, "email": new_user.email}}

@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db_functions.get_user(db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user": {"id": user.id, "name": user.name, "email": user.email}}

@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "error", "database": str(e)}