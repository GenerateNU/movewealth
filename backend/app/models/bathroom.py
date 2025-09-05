from datetime import datetime
from typing import List
from fastapi import UploadFile, HTTPException
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorCollection
from app.schemas.bathroom import Bathroom, CreateBathroomRequest, GetWithinAreaRequest
from app.database.mongodb import db
import json

class BathroomModel:
    def __init__(self):
        self.collection: AsyncIOMotorCollection = db["bathrooms"]
        
    async def create_bathroom(self, bathroom: CreateBathroomRequest) -> Bathroom:
        bathroom_data = bathroom.model_dump()

        bathroom_data = { **bathroom_data, "approved": True }

        await self.collection.insert_one(bathroom_data)

        return Bathroom(**bathroom_data)

    async def get_all_bathrooms(self) -> List[Bathroom]:
        bathrooms_list = await self.collection.find({"approved": True}).to_list(length=None)

        return [Bathroom(**bathroom) for bathroom in bathrooms_list]
    
    async def delete_all_bathrooms(self) -> None:
        await self.collection.delete_many({})

bathroom_model = BathroomModel()