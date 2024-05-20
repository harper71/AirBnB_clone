#!/usr/bin/python3
""" FileStorage class"""
import json
from models.base_model import BaseModel

class FileStorage:
    """ creating file path and object """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns dictionary __objects """
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
