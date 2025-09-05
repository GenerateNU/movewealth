from pydantic import BaseModel
from datetime import datetime

class Person(BaseModel):
    id: str
    name: str
    major: str
    fun_fact: str
    favorite_restaurant_in_boston: str
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    class Config:
        from_attributes = True

class CreatePersonRequest(Person):
    name: str
    major: str
    fun_fact: str
    favorite_restaurant_in_boston: str
