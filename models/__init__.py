#!/usr/bin/python3
<<<<<<< HEAD
=======
<<<<<<< HEAD
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
=======
>>>>>>> 55b7042d428bb15db1154f856a5724024c9d5feb
"""
Instantiates a storage object.

-> If the environmental variable 'HBNB_TYPE_STORAGE' is set to 'db',
   instantiates a database storage engine (DBStorage).
-> Otherwise, instantiates a file storage engine (FileStorage).
"""
<<<<<<< HEAD
=======
>>>>>>> 75899db89f6e3f5da16aff976271d677b9c232c2
>>>>>>> 55b7042d428bb15db1154f856a5724024c9d5feb
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
<<<<<<< HEAD
    from models.engine.db_storage import DBStorage
=======
<<<<<<< HEAD
>>>>>>> 55b7042d428bb15db1154f856a5724024c9d5feb
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
<<<<<<< HEAD
=======
    
=======
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
>>>>>>> 75899db89f6e3f5da16aff976271d677b9c232c2
>>>>>>> 55b7042d428bb15db1154f856a5724024c9d5feb
storage.reload()
