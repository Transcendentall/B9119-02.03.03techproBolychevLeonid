from pydantic import BaseModel
from typing import Optional

class UserInBD(BaseModel):
    user_login: str
    user_password: str
    user_email: str
    user_surname: Optional[str] = None
    user_name: Optional[str] = None
    user_fathername: Optional[str] = None
    user_age: Optional[int] = None
    user_isFemale: Optional[bool] = None
    user_picture: Optional[str] = None
    user_isAdmin: bool

class UserRegister(BaseModel):
    user_login: str
    user_password: str
    user_email: str

class UserAuthorization(BaseModel):
    user_login: str
    user_password: str

