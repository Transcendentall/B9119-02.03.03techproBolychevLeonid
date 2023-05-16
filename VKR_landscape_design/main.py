# main.py

from typing import Optional
from controllers import UserController
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

app.include_router(UserController.router)
