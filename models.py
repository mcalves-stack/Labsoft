from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.expression import Null
from database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String, nullable=False)
    password = Column(String, nullable=False)
    materiaUsuario = Column(String, nullable=False)
    raUsuario = Column(Integer, nullable=False)


    