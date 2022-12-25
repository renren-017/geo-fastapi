from typing import Optional

from pydantic import BaseModel


class ShopBase(BaseModel):
    name: str
    lat: float
    lon: float
    address: str
    city: str

    class Config:
        orm_mode=True


class ShopUpdate(BaseModel):
    name: Optional[str]
    lat: Optional[float]
    lon: Optional[float]
    address: Optional[str]
    city: Optional[str]
