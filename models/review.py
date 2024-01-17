#!/usr/bin/python3
""" Review module for the HBNB project """
<<<<<<< HEAD
=======
<<<<<<< HEAD
from models.base_model import Base
>>>>>>> 55b7042d428bb15db1154f856a5724024c9d5feb
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review classto store review information """
<<<<<<< HEAD
    place_id = ""
    user_id = ""
    text = ""
=======
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
=======
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review classto store review information """
    place_id = ""
    user_id = ""
    text = ""
>>>>>>> 75899db89f6e3f5da16aff976271d677b9c232c2
>>>>>>> 55b7042d428bb15db1154f856a5724024c9d5feb
