#!/usr/bin/python3


from uuid import uuid4
from datetime import datetime
"""
class module that defines all common attributes/
methods for other classes
"""


class BaseModel:
    """class that defines all common attributes/
    methods for other classes"""


    def __init__(self):
        """constructor for class instances"""

        self.id =str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """string repressentation"""

        return "{} {} {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        
        """updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values"""

        ins_dict = {}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                ins_dict[key] = value.isoformat()
            ins_dict[key] = value
        ins_dict['__class__'] = self.__class__.__name__
        return ins_dict
