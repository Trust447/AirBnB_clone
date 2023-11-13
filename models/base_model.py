#!/usr/bin/python3
"""
class module that defines all common attributes/
methods for other classes
"""
import uuid
from datetime import datetime



class BaseModel:
    """class that defines all common attributes/
    methods for other classes"""

    def __init__(self, *args, **kwargs):
        """constructor for BaseModel arguments"""
        """from models import storage"""

        from models import storage
        self.id = kwargs.get('id', str(uuid.uuid4()))
        self.created_at = kwargs.get('created_at', datetime.now())
        self.updated_at = kwargs.get('updated_at', datetime.now())

        if '__class__' in kwargs:
            del kwargs['__class__']
        for key, value in kwargs.items():
            if key in ('created_at', 'updated_at'):
                date_time_val = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, date_time_val)
            else:
                setattr(self, key, value)

            if 'created_at' not in kwargs or 'updated_at' not in kwargs:
                storage.new(self)

    def __str__(self):
        """string repressentation"""

        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values"""

        ins_dict = {}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                ins_dict[key] = value.isoformat()
            else:
                ins_dict[key] = value
        ins_dict['__class__'] = self.__class__.__name__
        return ins_dict
