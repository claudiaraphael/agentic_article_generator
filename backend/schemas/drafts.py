from pydantic import BaseModel
from typing import Optional

# Shared properties for Draft
class DraftBase(BaseModel):
    name: str
    content: str
    article_id: int # Foreign key to Article

# Properties to receive on item creation
class DraftCreate(DraftBase):
    pass

# Properties to return to client (including the ID)
class DraftSchema(DraftBase):
    id: int

    class Config:
        from_attributes = True
