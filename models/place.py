#!/usr/bin/python3
"""module for place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """class for user place"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = int(0)
    number_bathrooms = int(0)
    max_guest = int(0)
    price_by_night = int(0)
    latitude = float(0.0)
    longitude = float(0.0)
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Constructor for place"""

        super().__init__(*args, **kwargs)
