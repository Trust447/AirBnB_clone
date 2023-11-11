#!/usr/bin/python3
"""module for amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """class for user amenity"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Constructor for amenity"""
        super().__init__(*args, **kwargs)
