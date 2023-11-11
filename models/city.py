#!/usr/bin/python3
"""module for city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """class for user city"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Constructor for city"""

        super().__init__(*args, **kwargs)
