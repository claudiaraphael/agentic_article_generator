from pydantic import BaseModel
from typing import Optional, List

# Import the ThemeSchema for embedding
from schemas.theme import ThemeSchema

# Shared properties for Article
class ArticleBase(BaseModel):
    theme_id: int
    title: Optional[str] = None
    research_report: Optional[str] = None
    analysis_report: Optional[str] = None
    seo_keyword_list: Optional[List[str]] = None
    draft: Optional[str] = None
    edition: Optional[str] = None
    output: Optional[str] = None

# Properties to receive on item creation
class ArticleCreate(ArticleBase):
    pass

# Properties to return to client (including the ID and related Theme data)
class ArticleSchema(ArticleBase):
    id: int
    theme: ThemeSchema # Embed the full theme schema here

    class Config:
        from_attributes = True
