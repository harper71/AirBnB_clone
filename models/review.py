#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base

class Review(BaseModel):
    place_id: str = ""
    user_id: str = ""  
    text: str = ""
