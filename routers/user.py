from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter

from ..utils import utils

from ..auth import oauth2

from ..models import models
from ..connection.database import get_db, engine
from ..schemas import schemas
from typing import List, Optional
from sqlalchemy.orm import Session
from pydantic import BaseModel
from fastapi.params import Body
from typing import List, Optional

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/users",
    tags=['Users']
)


@router.post("/createuser", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

  hashed_password = utils.hash(user.password)
  user.password = hashed_password

  new_user = models.Usuario(**user.dict())
  db.add(new_user)
  db.commit()
  db.refresh(new_user)

  return new_user


@router.get('/createuser/{id}', response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    user = db.query(models.Usuario).filter(models.Usuario.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {id} does not exist")

    return user

@router.delete("/createuser/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):

    users_query = db.query(models.Usuario).filter(models.Usuario.id == id)

    user = users_query.first()

    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")

    users_query.delete(synchronize_session=False)
    db.commit()

    return users_query

@router.get("/users")
def get_users(db: Session = Depends(get_db),limit: int = 10, skip: int = 0, search: Optional[str] = "", ):
    users = db.query(models.Usuario).all()
    return {"data": users}


@router.put("/users/{id}")
def update_users(id: int, updated_post: schemas.UserCreate, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):

    users_query = db.query(models.Usuario).filter(models.Usuario.id == id)

    users = users_query.first()

    if users == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")

    users_query.update(updated_post.dict(), synchronize_session=False)

    db.commit()

    return users_query.first()
