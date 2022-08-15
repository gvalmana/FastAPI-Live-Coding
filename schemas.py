from tokenize import String
from pydantic import BaseModel
from typing import Optional

class UserRequestModel(BaseModel):
    username: str
    email: str

class UserResponseModel(BaseModel):
    username: str
    email: str