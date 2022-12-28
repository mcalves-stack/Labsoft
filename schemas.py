from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel,Field
from pydantic.generics import GenericModel
from datetime import datetime
from fastapi import Form
from typing import Optional


class UserOut(BaseModel):
  id: int
  login: str
  password: str
  materiaUsuario: str
  raUsuario: int
  created_at: datetime

  class Config:
     orm_mode = True

class UserCreate(BaseModel):
    login: str
    password: str
    materiaUsuario: str
    raUsuario: int

class UserLogin(BaseModel):
  login: str
  password: str

class Token(BaseModel):
  access_token: str
  token_type: str

class TokenData(BaseModel):
  id: Optional[str] = None

class Room(BaseModel):
  id: int
  ativa: bool
  caixa_som: bool
  capacidade: int
  microfone: bool
  nome_sala: str
  projetor: bool
  computador: int
  created_at: datetime

  class Config:
     orm_mode = True

class CreateRooms(BaseModel):
  ativa: bool
  caixa_som: bool
  capacidade: int
  microfone: bool
  nome_sala: str
  projetor: bool
  computador: int
  

class Professor(BaseModel):
  id: int
  nome: str
  Id_Professor: int
  created_at: datetime

  class Config:
     orm_mode = True

class CreateProfessor(BaseModel):
  nome: str
  Id_Professor: int

