from sqlalchemy import Column, Integer, Float, String, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class WaterQualityObservation(Base):
    __tablename__ = "water_quality_observations"

    id = Column(Integer, primary_key=True, index=True)
    location = Column(JSON)
    date_time = Column(String)
    description = Column(String)
    parameters = Column(JSON)
