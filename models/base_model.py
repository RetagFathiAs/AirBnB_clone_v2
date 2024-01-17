#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
<<<<<<< HEAD
from sqlalchemy import Column, DATETIME, String
from sqlalchemy.ext.declarative import declarative_base
import models
from os import getenv

if getenv("HBNB_TYPE_STORAGE") == 'db':
    Base = declarative_base()
else:
    Base = object
=======
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String

Base = declarative_base()
>>>>>>> 75899db89f6e3f5da16aff976271d677b9c232c2


class BaseModel:
    """A base class for all hbnb models"""

<<<<<<< HEAD
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        id = Column(String(60), primary_key=True)
        created_at = Column(DATETIME, default=datetime.utcnow, nullable=False)
        updated_at = Column(DATETIME, default=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            tf = "%Y-%m-%dT%H:%M:%S.%f"
            if "updated_at" in kwargs:
                kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                                         tf)
            else:
                self.updated_at = datetime.now()
            if "created_at" in kwargs:
                kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                         tf)
            else:
                self.created_at = datetime.now()
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            for key in kwargs:
                if key != "__class__":
                    setattr(self, key, kwargs[key])
=======
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if hasattr(self, key):
                    setattr(self, key, value)
>>>>>>> 75899db89f6e3f5da16aff976271d677b9c232c2

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
<<<<<<< HEAD
        dic = self.__dict__.copy()
        if "_sa_instance_state" in dic:
            del dic["_sa_instance_state"]
        return '[{}] ({}) {}'.format(cls, self.id, dic)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()
=======
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()
>>>>>>> 75899db89f6e3f5da16aff976271d677b9c232c2

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
<<<<<<< HEAD
        if "_sa_instance_state" in dictionary:
            del dictionary["_sa_instance_state"]
        return dictionary

    def delete(self):
        """ deletes the instance"""
        models.storage.delete(self)
=======
        try:
            del dictionary["_sa_instance_state"]
        except KeyError:
            pass
        return dictionary

    def delete(self):
        """
        
        """
        from models import storage
        storage.delete(self)
>>>>>>> 75899db89f6e3f5da16aff976271d677b9c232c2
