#!/usr/bin/python3
import json
"""creates a class that stores user data"""


class FileStorage:
    """class the storage json data"""
    def __init__(self):
        self.__file_path = "file.json"
        self.__object = {}

    def all(self):
        return self.__object

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes the json file"""
        with open(self.__file_path, "w") as write_file:
            json.dump(self.__object, write_file)

    def reload(self):
        """deserializes the json file"""
        with open(self.__file_path, "r") as read_file:
            if not self.__file_path:
                pass
            else:
                self.__object = json.load(read_file)
