from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class Cadastros(BaseModel):
    nome: str = Field(min_length=1)
    email: str = Field(min_length=1, max_length=100)
    telefone: str = Field(min_length=9, max_length=100)
    usuario: int = Field(gt=4, lt=101)
    senha: int = Field(gt=8, lt=101)
    confirmacao: int = Field(gt=8, lt=101)


USERS = []

@app.post("/")
def create_user(user: User, db: Session = Depends(get_db)):

    user_model = models.Cadastros()
    user_model.title = user.title
    user_model.author = user.author
    user_model.description = user.description
    user_model.rating = user.rating

    db.add(user_model)
    db.commit()

    return user

