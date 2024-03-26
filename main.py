from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String, Float, JSON
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from pydantic import BaseModel
from typing import List
import datetime
from fastapi import Query
from sqlalchemy import func
import os

# Import dotenv and load environment variables
from dotenv import load_dotenv
load_dotenv()


# NeonDB PostgreSQL database URL
DATABASE_URL = os.getenv("DATABASE_URL")


# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create base class for database models
Base = declarative_base()

# Define database model for Observations
class Observation(Base):
    __tablename__ = "observations"

    id = Column(Integer, primary_key=True, index=True)
    location = Column(JSON)
    date_time = Column(String)
    description = Column(String)
    parameters = Column(JSON)

# API models for Observations
class ObservationCreate(BaseModel):
    location: dict
    date_time: str
    description: str
    parameters: dict

class ObservationUpdate(BaseModel):
    location: dict
    date_time: str
    description: str
    parameters: dict

class ObservationResponse(BaseModel):
    id: int
    location: dict
    date_time: str
    description: str
    parameters: dict

# FastAPI app
app = FastAPI()

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create tables
Base.metadata.create_all(bind=engine)

# API endpoints for Observations
@app.post("/observations/", response_model=ObservationResponse)
def create_observation(observation: ObservationCreate, db: Session = Depends(get_db)):
    db_observation = Observation(**observation.dict())
    db.add(db_observation)
    db.commit()
    db.refresh(db_observation)
    return db_observation

@app.get("/observations/", response_model=List[ObservationResponse])
def read_observations(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    observations = db.query(Observation).offset(skip).limit(limit).all()
    return observations

@app.get("/observations/{observation_id}", response_model=ObservationResponse)
def read_observation(observation_id: int, db: Session = Depends(get_db)):
    observation = db.query(Observation).filter(Observation.id == observation_id).first()
    if observation is None:
        raise HTTPException(status_code=404, detail="Observation not found")
    return observation

@app.put("/observations/{observation_id}", response_model=ObservationResponse)
def update_observation(observation_id: int, observation: ObservationUpdate, db: Session = Depends(get_db)):
    db_observation = db.query(Observation).filter(Observation.id == observation_id).first()
    if db_observation is None:
        raise HTTPException(status_code=404, detail="Observation not found")
    for field, value in observation.dict().items():
        setattr(db_observation, field, value)
    db.commit()
    db.refresh(db_observation)
    return db_observation

@app.delete("/observations/{observation_id}", response_model=ObservationResponse)
def delete_observation(observation_id: int, db: Session = Depends(get_db)):
    db_observation = db.query(Observation).filter(Observation.id == observation_id).first()
    if db_observation is None:
        raise HTTPException(status_code=404, detail="Observation not found")
    db.delete(db_observation)
    db.commit()
    return db_observation

@app.get("/observations/closest_location/")
def get_closest_location(latitude: float = Query(...), longitude: float = Query(...), db: Session = Depends(get_db)):
    # Perform logic to find observations closest to the given latitude and longitude
    # Example logic: Calculate distance using haversine formula and return closest observations
    closest_observations = db.query(Observation).all()  # Replace with actual query logic
    return closest_observations


@app.get("/observations/date_range/")
def get_observations_in_date_range(start_date: str = Query(...), end_date: str = Query(...),
                                   db: Session = Depends(get_db)):
    # Perform logic to find observations within the specified date range
    # Example logic: Query observations between start_date and end_date
    observations_in_range = db.query(Observation).filter(Observation.date_time.between(start_date, end_date)).all()
    return observations_in_range


@app.get("/observations/quality_parameters/")
def get_observations_by_quality_parameters(pH_min: float = Query(None), pH_max: float = Query(None),
                                           conductivity_min: float = Query(None), conductivity_max: float = Query(None),
                                           DO_min: float = Query(None), DO_max: float = Query(None),
                                           contaminants: List[str] = Query(None), db: Session = Depends(get_db)):
    # Perform logic to filter observations based on quality parameters
    # Example logic: Query observations based on specified pH, conductivity, DO, and contaminants
    query = db.query(Observation)
    if pH_min is not None:
        query = query.filter(Observation.parameters['pH'] >= pH_min)
    if pH_max is not None:
        query = query.filter(Observation.parameters['pH'] <= pH_max)
    if conductivity_min is not None:
        query = query.filter(Observation.parameters['conductivity'] >= conductivity_min)
    if conductivity_max is not None:
        query = query.filter(Observation.parameters['conductivity'] <= conductivity_max)
    if DO_min is not None:
        query = query.filter(Observation.parameters['DO'] >= DO_min)
    if DO_max is not None:
        query = query.filter(Observation.parameters['DO'] <= DO_max)
    if contaminants is not None:
        for contaminant in contaminants:
            query = query.filter(Observation.parameters['contaminants'].astext.contains(contaminant))

    filtered_observations = query.all()
    return filtered_observations





