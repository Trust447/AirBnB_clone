#!/usr/bin/python3
"""
This module defines the User class, which inherits from BaseModel.
"""

from models.base_model import BaseModel

class User(BaseModel):
    """ User class that inherits from BaseModel """
    def __init__(self, email="", password="", first_name="", last_name=""):
        super().__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
