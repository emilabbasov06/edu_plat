from fastapi import FastAPI, Depends, status, HTTPException
from sqlalchemy.orm import Session

from database import engine, get_db
from models import Base
from routers import users, posts

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(posts.router)

@app.get('/')
async def index():
    return {
        'message': 'Hello, there!'
    }
