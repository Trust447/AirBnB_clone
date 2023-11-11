#!/usr/bin/python3
"""module for review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class for user review"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Constructor for review"""

        super().__init__(*args, **kwargs)
