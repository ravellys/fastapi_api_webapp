from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from schemas.teste import Teste
from schemas.users import UserCreate, ShowUser
from db.session import get_db
from db.repository.users import create_new_user

router = APIRouter()


@router.post("/", response_model=ShowUser)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        user = create_new_user(user, db)
        return user
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=f"Error: {e}")


@router.post("/teste")
def teste(teste: Teste):
    print(teste)
    return teste