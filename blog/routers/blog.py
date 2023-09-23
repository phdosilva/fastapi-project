from fastapi import APIRouter, Depends, status
from typing import List
from sqlalchemy.orm import Session

from .. import schemas, database, oauth2
from ..repository import blog


router = APIRouter(
    prefix="/blog",
    tags=["blogs"]
)

@router.get("/", response_model=List[schemas.ConsultedBlog])
def get_all(db: Session = Depends(database.get_db)):
    return blog.get_all(db)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(database.get_db), current_user = Depends(oauth2.get_current_user)):
    return blog.cerate(request, db)

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(database.get_db), current_user = Depends(oauth2.get_current_user)):
    return blog.delete(id, db)

@router.put("/{id}")
def update(id: int, request: schemas.Blog, db: Session = Depends(database.get_db), current_user = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ConsultedBlog)
def show(id: int, db: Session = Depends(database.get_db)):
    return blog.get(id, db)

