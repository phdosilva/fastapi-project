from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import schemas, database, oauth2
from ..repository import user


router = APIRouter(
    prefix="/user",
    tags=["user"]
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ConsultedUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db), current_user = Depends(oauth2.get_current_user)):
    return user.create(request, db)

@router.get("/{id}", response_model=schemas.ConsultedUser)
def get_user(id: int, db: Session = Depends(database.get_db), current_user = Depends(oauth2.get_current_user)):
    return user.get(id, db)