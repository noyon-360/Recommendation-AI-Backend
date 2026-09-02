from pydantic import BaseModel, ConfigDict, Field


class User(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str = Field(alias="_id")
    name: str
    age: int
    favorite_categories: list[str] = []
    favorite_items: list[str] = []
