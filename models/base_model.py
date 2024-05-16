#!/usr/bin/python3
import datetime
import uuid
"""base model of the airbnb project"""
class BaseModel:
    """base model 
    """
    def __init__(self):
        self.id = uuid.uuid4()
        id = str(id)
        self.created_at = datetime.datetime.now()
        self.update_at = datetime.datetime.now()

    def save(self):
        self.update_at = datetime.datetime.now()
    
    def to_dict(self):
        self.update_at = self.update_at.isoformat()
        self.created_at = self.created_at.isoformat()
        all_atributes = {}

        for key, values in self.__dict__.items():
            all_atributes[key] = values
        
        return all_atributes
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__} ({self.id}) {self.__dict__}"
    
