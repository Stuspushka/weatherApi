from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from .database import Base


class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    searches = relationship("SearchHistory", back_populates="city")


class SearchHistory(Base):
    __tablename__ = "search_history"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    city_id = Column(Integer, ForeignKey("cities.id"))
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    city = relationship("City", back_populates="searches")
