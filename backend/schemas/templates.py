from pydantic import BaseModel
from typing import Optional

# Shared properties for Template
class TemplateBase(BaseModel):
    name: str
    body: str

# Properties to receive on item creation
class TemplateCreate(TemplateBase):
    pass

# Properties to return to client (including the ID)
class TemplateSchema(TemplateBase):
    id: int

    class Config:
        from_attributes = True
