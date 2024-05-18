#!/usr/bin/python3
import datetime
import uuid
"""base model of the airbnb project"""


class BaseModel:
    """base model """
    def __init__(self, *args, **kargs):
        if kargs:
            for key, value in kargs.items():
                if key != '__class__':
                    setattr(self, key, value)

        self.id = uuid.uuid4()
        self.created_at = datetime.datetime.now()
        self.update_at = datetime.datetime.now()

    def save(self):
        self.update_at = datetime.datetime.now()

    def to_dict(self):
        self.update_at = self.update_at.isoformat()
        self.created_at = self.created_at.isoformat()
        all_atributes = {'__class__': self.__class__.__name__}

        for key, values in self.__dict__.items():
            all_atributes[key] = values

        return all_atributes

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
