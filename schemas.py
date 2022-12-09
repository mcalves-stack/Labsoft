from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel,Field
from pydantic.generics import GenericModel
from fastapi import Form
from typing import Optional



class UserOut(BaseModel):
  id: int
  login: str
  password: str
  materiaUsuario: str
  raUsuario: str

  class Config:
     orm_mode = True


class UserCreate(BaseModel):
    login: str
    password: str
    materiaUsuario: str
    raUsuario: str


class UserLogin(BaseModel):
  login: str
  password: str 

class Token(BaseModel):
  access_token: str
  token_type: str

class TokenData(BaseModel):
  id: Optional[str] = None


