from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DATETIME
from sqlalchemy.sql.expression import Null
from connection.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String, nullable=False)
    password = Column(String, nullable=False)
    materiaUsuario = Column(String, nullable=False)
    raUsuario = Column(Integer, nullable=False)
 
class TipoUser(Base):
    __tablename__ = "tipousers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(Integer, nullable=False)

class Sala(Base):
    __tablename__ = "sala"

    Id_sala = Column(Integer, primary_key=True, autoincrement=True)
    ativa = Column(Boolean, nullable=False)
    caixa_som = Column(Boolean, nullable=False)
    capacidade = Column(Integer, nullable=False)
    microfone = Column(Boolean, nullable=False)
    nome_sala = Column(String, nullable=False)
    projetor = Column(Boolean, nullable=False)
    computador = Column(Integer, nullable=False)

