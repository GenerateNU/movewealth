from typing import List
from motor.motor_asyncio import AsyncIOMotorCollection
from app.schemas.person import Person, CreatePersonRequest
from app.database.mongodb import db

class PersonModel:
    def __init__(self):
        self.collection: AsyncIOMotorCollection = db["persons"]

    async def create_person(self, person: CreatePersonRequest) -> Person:
        person_data = person.model_dump()

        await self.collection.insert_one(person_data)

        return Person(**person_data)

    async def get_all_persons(self) -> List[Person]:
        persons_list = await self.collection.find().to_list(length=None)

        return [Person(**person) for person in persons_list]

    async def delete_all_persons(self) -> None:
        await self.collection.delete_many({})

person_model = PersonModel()