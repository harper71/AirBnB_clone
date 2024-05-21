#!/usr/bin/python3
"""user class for user information"""
from models.base_model import BaseModel


class User(BaseModel):
    """ user information

    Args:
        BaseModel (class): base model of the app
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
