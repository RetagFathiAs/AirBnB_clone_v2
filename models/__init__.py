#!/usr/bin/python3
<<<<<<< HEAD
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
=======
"""
Instantiates a storage object.

-> If the environmental variable 'HBNB_TYPE_STORAGE' is set to 'db',
   instantiates a database storage engine (DBStorage).
-> Otherwise, instantiates a file storage engine (FileStorage).
"""
>>>>>>> 75899db89f6e3f5da16aff976271d677b9c232c2
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
<<<<<<< HEAD
    storage = DBStorage()
else:
    storage = FileStorage()
    
=======
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
>>>>>>> 75899db89f6e3f5da16aff976271d677b9c232c2
storage.reload()
