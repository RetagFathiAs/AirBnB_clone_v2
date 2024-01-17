#!/usr/bin/python3
""" State Module for HBNB project """
<<<<<<< HEAD
=======
<<<<<<< HEAD
from models.base_model import Base
>>>>>>> 55b7042d428bb15db1154f856a5724024c9d5feb
from models.base_model import BaseModel


class Amenity(BaseModel):
<<<<<<< HEAD
    name = ""
=======
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
>>>>>>> 55b7042d428bb15db1154f856a5724024c9d5feb
