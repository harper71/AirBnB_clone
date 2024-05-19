#!/usr/bin/python3
"""creates a class that stores user data"""
import json
import os
from models.base_model import BaseModel
from datetime import datetime


class FileStorage:
    """class the storage json data"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        obj_cls_name = obj.__class__.__name__

        key = "{}.{}".format(obj_cls_name, obj.id)

        self.__objects[key] = obj

    @staticmethod
    def convert_datetimes(obj):
        """converts the datetime to a string"""
        if isinstance(obj, dict):
            return {k: FileStorage.convert_datetimes(v)
                    for k, v in obj.items()}
        elif isinstance(obj, list):
            return [FileStorage.convert_datetimes(i) for i in obj]
        elif isinstance(obj, datetime):
            return obj.isoformat()
        return obj

    def save(self):
        """serializes the json file"""
        obj_dict = {}

        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()
        obj_dict = self.convert_datetimes(obj_dict)

        with open(self.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """deserializes the json file"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    if value['__class__'] == 'BaseModel':
                        self.__objects[key] = BaseModel(**value)
