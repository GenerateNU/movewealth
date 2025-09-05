from fastapi import APIRouter, HTTPException, Depends, Body, UploadFile, File, Query
from typing import List
from app.schemas.bathroom import Bathroom, CreateBathroomRequest, GetWithinAreaRequest
from app.schemas.user import User
from app.models.bathroom import bathroom_model

router = APIRouter()

@router.post("/new", response_model=Bathroom)
async def create_bathroom(bathroom: CreateBathroomRequest = Body(...)):
    return await bathroom_model.create_bathroom(bathroom)

@router.get("/all", response_model=List[Bathroom])
async def get_bathrooms():
    return await bathroom_model.get_all_bathrooms()

@router.delete("/clear", response_model=None)
async def clear_bathrooms():
    return await bathroom_model.delete_all_bathrooms()