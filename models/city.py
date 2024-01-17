#!/usr/bin/python3
""" City Module for HBNB project """
<<<<<<< HEAD
from sqlalchemy import Column, ForeignKey, String
from models.base_model import BaseModel, Base
=======
<<<<<<< HEAD
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship
from models.base_model import Base
>>>>>>> 55b7042d428bb15db1154f856a5724024c9d5feb


class City(BaseModel, Base):
    """
    >>City inherits from BaseModel and Base (respect the order)
    >>class attribute __tablename__ -
            represents the table name, cities
    >>class attribute name
            represents a column containing a string (128 characters)
            cant be null
    >>class attribute state_id
            represents a column containing a string (60 characters)
            cant be null
            is a foreign key to states.id
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
<<<<<<< HEAD
=======
    places = relationship("Place", backref="cities", cascade="delete")
=======
from sqlalchemy import Column, ForeignKey, String
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """
    >>City inherits from BaseModel and Base (respect the order)
    >>class attribute __tablename__ -
            represents the table name, cities
    >>class attribute name
            represents a column containing a string (128 characters)
            cant be null
    >>class attribute state_id
            represents a column containing a string (60 characters)
            cant be null
            is a foreign key to states.id
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
>>>>>>> 75899db89f6e3f5da16aff976271d677b9c232c2
>>>>>>> 55b7042d428bb15db1154f856a5724024c9d5feb
