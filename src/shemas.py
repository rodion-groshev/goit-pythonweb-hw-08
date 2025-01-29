from pydantic import BaseModel, Field, EmailStr, ConfigDict
from typing import List, Optional
from datetime import datetime

class FirstName(BaseModel):
    first_name: str = Field(min_length=2, max_length=20)

