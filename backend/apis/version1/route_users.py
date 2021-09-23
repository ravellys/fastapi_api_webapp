from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.teste import Teste
from schemas.users import UserCreate, ShowUser
from db.session import get_db
from db.repository.users import create_new_user

router = APIRouter()


@router.post("/", response_model=ShowUser)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_new_user(user, db)
    return user


@router.post("/teste")
def teste(teste: Teste):
    print(teste)
    return teste