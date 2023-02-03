from sqlalchemy import Column, Integer, String
from database import Base


class Cadastros(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    telefone = Column(String)
    usuario = Column(String)
    senha = Column(String)
    confirmacao = Column(String)
    