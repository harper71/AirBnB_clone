#!/usr/bin/python3
"""base model of the airbnb project"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """The BaseModel class serves as the foundation
    for all other models in the application.
    It provides common attributes and functionalities
    like unique ID generation, timestamps,
    saving to storage, and dictionary representation.
    """

    def __init__(self, *args, **kwargs):
        """
        The constructor for the BaseModel class.

        Args:
            *args (optional): Variable arguments
            (not used in this implementation).
            **kargs (dict, optional): Keyword arguments used to
            initialize the object's attributes.
            If provided, kargs should contain key-value pairs representing
            attributes and their values.

        Raises:
            AttributeError: If attempting
            to set the special key '__class__' as an attribute.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.fromisoformat(value)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """
        Updates the update_at attribute to the current datetime and
        calls storage.save()
        to persist the object's data to the storage system.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Converts the object to a dictionary representation.

        Returns:
            dict: A dictionary containing the object's
            attributes as key-value pairs.
            The '__class__' key stores the class name,
            and timestamps are converted
            to ISO format for wider compatibility.
        """
        all_atributes = self.__dict__.copy()
        all_atributes["__class__"] = self.__class__.__name__
        all_atributes["created_at"] = self.created_at.isoformat()
        all_atributes["updated_at"] = self.updated_at.isoformat()

        return all_atributes

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
