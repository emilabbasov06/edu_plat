from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session

from models import UserType, PostCategoryType
from database import get_db

router = APIRouter(
    prefix='/others',
    tags=['Other Elements (Types, Categories)']
)

@router.get('/categories')
async def get_categories():
    names = dir(PostCategoryType)[4:]
    categories = []

    if not names:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Nothing found')
    else:
        for name in names:
            categories.append(PostCategoryType[name].value)

    return categories

@router.get('/usertypes')
async def get_user_types():
    names = dir(UserType)[4:]
    types = []
    if not names:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Nothing found')
    else:
        for name in names:
            types.append(UserType[name].value)

    return types
