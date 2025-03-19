from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session

from models import UserModel
from schemas import UserSchema, CreateUserSchema
from database import get_db

router = APIRouter(
    prefix='/users',
    tags=['Users']
)

@router.get('')
async def get_users(db: Session = Depends(get_db)):
    users = db.query(UserModel).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'There was some problem')

    return users


@router.post('', response_model=UserSchema)
async def create_user(user: CreateUserSchema, db: Session = Depends(get_db)):
    new_user = UserModel(name=user.name, email=user.email, password=user.password, acc_type=user.acc_type)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
