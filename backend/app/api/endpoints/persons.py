from fastapi import APIRouter, Body
from typing import List
from app.schemas.person import Person, CreatePersonRequest
from app.models.person import person_model

router = APIRouter()

@router.post("/new", response_model=Person)
async def create_person(person: CreatePersonRequest = Body(...)):
    return await person_model.create_person(person)

@router.get("/all", response_model=List[Person])
async def get_persons():
    return await person_model.get_all_persons()

@router.delete("/clear", response_model=None)
async def clear_persons():
    return await person_model.delete_all_persons()