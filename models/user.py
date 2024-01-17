#!/usr/bin/python3
"""This module defines a class User"""
<<<<<<< HEAD
=======
<<<<<<< HEAD
from models.base_model import Base
>>>>>>> 55b7042d428bb15db1154f856a5724024c9d5feb
from models.base_model import BaseModel


class User(BaseModel):
    """This class defines a user by various attributes"""
<<<<<<< HEAD
=======
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")
=======
from models.base_model import BaseModel


class User(BaseModel):
    """This class defines a user by various attributes"""
>>>>>>> 55b7042d428bb15db1154f856a5724024c9d5feb
    email = ''
    password = ''
    first_name = ''
    last_name = ''
<<<<<<< HEAD
=======
>>>>>>> 75899db89f6e3f5da16aff976271d677b9c232c2
>>>>>>> 55b7042d428bb15db1154f856a5724024c9d5feb
