from sqlalchemy.ext.asyncio import AsyncSession
from watchfiles import awatch

from src.repository.contacts import ContactRepository
from src.schemas import ContactSchema


class ContactService:
    def __init__(self, db: AsyncSession):
        self.contact_repo = ContactRepository(db)

    async def create_contact(self, body: ContactSchema):
        return await self.contact_repo.create_contact(body)

    async def get_contacts(self, skip: int, limit: int):
        return await self.contact_repo.get_contacts(skip, limit)

    async def get_contact(self, contact_id: int):
        return await self.contact_repo.get_contact_by_id(contact_id)

    async def get_contact_first_name(self, contact_name: str):
        return await self.contact_repo.get_contact_by_first_name(contact_name)

    async def get_contact_second_name(self, contact_name: str):
        return await self.contact_repo.get_contact_by_second_name(contact_name)

    async def get_contact_email(self, contact_email: str):
        return await self.contact_repo.get_contact_by_email(contact_email)

    async def get_upcoming_birthday(self):
        return await self.contact_repo.get_upcoming_birthday()

    async def update_contact(self, contact_id: int, body: ContactSchema):
        return await self.contact_repo.update_contact(contact_id, body)

    async def remove_contact(self, contact_id: int):
        return await self.contact_repo.remove_contact(contact_id)
