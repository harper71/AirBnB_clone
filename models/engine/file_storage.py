#!/usr/bin/python3
"""
Contains the FileStorage class
"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}

class FileStorage:
    """ creating file path and object """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """returns the dictionary __objects"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj witj key """
        key = obj.__class__, __name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """ Serializes the __object to the JSON file """
        obj_dict = {}
        for key in self.__objects:
            obj_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """ deserializes the JSON File """
        try:
            with open(self.__file_path, "r") as f:
                obj_dict = json.load(f)
                for key in obj_dict:
                    self.__objects[key] = classess[obj_dict[key]["__class__"]](**obj_dict[key])
        except Exception:
            pass
