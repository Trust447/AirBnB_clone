#!/usr/bin/python3
"""a module for state class"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class inherits from BaseModel"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Constructor for state"""

        super().__init__(*args, **kwargs)
