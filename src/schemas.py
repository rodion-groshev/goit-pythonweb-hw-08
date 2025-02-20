from pydantic import BaseModel, Field, EmailStr, ConfigDict
from typing import List, Optional
from datetime import date


class ContactSchema(BaseModel):
    first_name: str = Field(min_length=2, max_length=20)
    second_name: str = Field(min_length=2, max_length=20)
    email: EmailStr
    phone: str = Field(min_length=10, max_length=13)
    birthday: date
    additional: Optional[str] = None


class ContactResponse(ContactSchema):
    id: int
    model_config = ConfigDict(from_attributes=True)
