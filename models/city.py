#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel

class City(BaseModel):
    state_id: str = ""
    name: str = ""
