#!/usr/bin/python3
from models.base_model import BaseModel
"""a module for state class"""


class State(BaseModel):
    """State class inherits from BaseModel"""

    self.name = ""

    def __init__(self, *args, **kwargs):
        """Constructor for state"""

        super().__init__(*args, **kwargs)
