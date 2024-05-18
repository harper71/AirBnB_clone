#!/usr/bin/python3
import datetime
import uuid
from models import storage
"""base model of the airbnb project"""


class BaseModel:
    """The BaseModel class serves as the foundation
    for all other models in the application.
    It provides common attributes and functionalities
    like unique ID generation, timestamps,
    saving to storage, and dictionary representation.
    """

    def __init__(self, *args, **kargs):
        """
        The constructor for the BaseModel class.

        Args:
            *args (optional): Variable arguments (not used in this implementation).
            **kargs (dict, optional): Keyword arguments used to 
            initialize the object's attributes.
            If provided, kargs should contain key-value pairs representing 
            attributes and their values.

        Raises:
            AttributeError: If attempting to set the special key '__class__' as an attribute.
        """
        if kargs:
            for key, value in kargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.datetime.fromisoformat(value)
                if key != '__class__':
                    setattr(self, key, value)

        else:
            storage.new()

        self.id = uuid.uuid4()
        self.created_at = datetime.datetime.now()
        self.update_at = datetime.datetime.now()

    def save(self):
        """
        Updates the update_at attribute to the current datetime and
        calls storage.save()
        to persist the object's data to the storage system.
        """
        self.update_at = datetime.datetime.now()
        storage.save()

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
        self.update_at = self.update_at.isoformat()
        self.created_at = self.created_at.isoformat()
        all_atributes = {'__class__': self.__class__.__name__}

        for key, values in self.__dict__.items():
            all_atributes[key] = values

        return all_atributes

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
