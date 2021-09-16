from typing import Optional
from pydantic import BaseModel, EmailStr


class Teste(BaseModel):
    name: str
    description: str
