from typing import List
from pydantic import BaseModel
# class House(BaseModel):
#     url: str


class Region(BaseModel):
    property_urls: List[str]
