#!/usr/bin/python3
"""amenity class for coustomers needs"""
from models.base_model import BaseModel

class Review(BaseModel):
    """review of the houses been rented"""

    place_id = ""
    user_id = ""
    text = ""