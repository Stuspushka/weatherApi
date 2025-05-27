from pydantic import BaseModel
from typing import List
from datetime import datetime

class CityBase(BaseModel):
    name: str

class CityResponse(CityBase):
    id: int

    class Config:
        orm_mode = True

class SearchHistoryResponse(BaseModel):
    user_id: str
    city: CityResponse
    timestamp: datetime

    class Config:
        orm_mode = True

class CityStat(BaseModel):
    city: str
    count: int

class UserHistoryResponse(BaseModel):
    cities: List[str]

class WeatherResponse(BaseModel):
    city: str
    temperature: float
    units: str
