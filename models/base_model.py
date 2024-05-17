#!/usr/bin/python3
"""
contains class BaseModel
"""

from datetime import datetime
import uuid

class BaseModel:
    """ The BaseModel class from which future class will be derived """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()


    def save(self):
        """ updates the attribute 'updated_at' with current datetime """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of the instance
        """
        return {
                'id': self.id,
                'created_at': self.created_at.isoformat(),
                'updated_at': self.updated_at.isoformat(),
                '__class__': self.__class__.__name__
                }
    def __str__(self):
        """ string representation of the BaseModel class """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)
