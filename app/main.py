from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, Base
from app import models, schemas
from geoalchemy2.functions import ST_GeomFromText, ST_Distance
from sqlalchemy import func
from geoalchemy2.shape import to_shape
app = FastAPI()

# Create tables (only for development, use Alembic in production)
Base.metadata.create_all(bind=engine)

# Dependency: get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint to add an ambulance
@app.post("/ambulances/", response_model=schemas.AmbulanceResponse)
def create_ambulance(data: schemas.AmbulanceCreate, db: Session = Depends(get_db)):
    point = f"POINT({data.location[1]} {data.location[0]})"
    ambulance = models.Ambulance(name=data.name, location=ST_GeomFromText(point, 4326))
    db.add(ambulance)
    db.commit()
    db.refresh(ambulance)
    location_shape = to_shape(ambulance.location)  # Convert to Shapely Point
    location_tuple = (location_shape.x, location_shape.y)  # Extract as tuple
    return {"id": ambulance.id, "name": ambulance.name, "location": location_tuple}

# Endpoint to find ambulances within a given radius
@app.get("/ambulances/nearby/")
def find_nearby_ambulances(lat: float, lon: float, radius: float, db: Session = Depends(get_db)):
    point = ST_GeomFromText(f"POINT({lon} {lat})", 4326)
    ambulances = (
        db.query(models.Ambulance)
        .filter(ST_Distance(models.Ambulance.location, point) <= radius)
        .all()
    )
    return [ambulance.name for ambulance in ambulances]
