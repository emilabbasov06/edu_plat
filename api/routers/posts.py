from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session

from models import PostModel
from schemas import PostSchema, CreatePostSchema
from database import get_db

router = APIRouter(
    prefix='/posts',
    tags=['Posts']
)

@router.get('')
async def get_posts(db: Session = Depends(get_db)):
    posts = db.query(PostModel).all()
    if not posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'There was some problem')
    
    return posts


@router.post('')
async def create_post(post: CreatePostSchema, db: Session = Depends(get_db)):
    new_post = PostModel(title=post.title, content=post.content, category=post.category, user_id=post.user_id)

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post

