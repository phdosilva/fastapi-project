from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(blog: schemas.Blog, db: Session):
    new_blog = models.Blog(title=blog.title, body=blog.body, creator_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog 

def delete(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog {id} not found.")
    
    blog.delete(synchronize_session=False)
    db.commit()
    return {f"Blog with id {id} was deleted."}

def update(id: int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog {id} not found.")
     
    blog.update({"title": request.title, "body": request.body}, synchronize_session=False)
    db.commit()
    
    return {f"Blog {id} was modified."}

def get(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} was not found.")
    
    return blog
