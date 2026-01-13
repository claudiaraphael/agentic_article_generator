from pydantic import BaseModel
from typing import Optional

# Shared properties
class ThemeBase(BaseModel):
    name: str
    description: Optional[str] = None

# Properties to receive on item creation
class ThemeCreate(ThemeBase):
    pass

# Properties to return to client
class ThemeSchema(ThemeBase):
    id: int

    class Config:
        from_attributes = True
