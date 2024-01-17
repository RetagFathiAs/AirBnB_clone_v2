#!/usr/bin/python3
""" State Module for HBNB project """
<<<<<<< HEAD
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Amenity(BaseModel):
    """Amenity class"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)
=======
from models.base_model import BaseModel


class Amenity(BaseModel):
    name = ""
>>>>>>> 75899db89f6e3f5da16aff976271d677b9c232c2
