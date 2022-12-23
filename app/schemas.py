from pydantic import BaseModel


class ShopBase(BaseModel):
    name: str
    lat: float
    lon: float
    address: str
    city: str

    class Config:
        orm_mode=True