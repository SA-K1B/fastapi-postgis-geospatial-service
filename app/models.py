from sqlalchemy import Column, Integer, String
from geoalchemy2 import Geography
from app.database import Base

class Ambulance(Base):
    __tablename__ = "ambulances1"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(Geography(geometry_type="POINT", srid=4326), nullable=False)
