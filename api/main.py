from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import engine, get_db
from models import Base
#from schemas import CreateUserSchema

app = FastAPI()
Base.metadata.create_all(bind=engine)


@app.get('/')
async def index():
    return {
        'message': 'Hello, there!'
    }

#@app.get('/check')
#async def check_connection(db: Session = Depends(get_db)):
#    users = db.query(UserModel).all()
#    return users

#@app.post('/insert')
#async def create_user(user: CreateUserSchema, db: Session = Depends(get_db)):
#    new_user = UserModel(
#        full_name = user.full_name,
#        email = user.email
#    )
#
#    db.add(new_user)
#    db.commit()
#    db.refresh(new_user)
#
#    return new_user
