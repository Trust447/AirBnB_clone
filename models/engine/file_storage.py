#!/usr/bin/python3
import json
from models.base_model import BaseModel
"""module with a class that serializes instances to a JSON
file and deserializes JSON file to instances
"""


class FileStorage:
    """ class that serializes instances to a JSON
    file and deserializes JSON file to instances
    """
    
    __file_path = ""
    __objects = {}

    def __init__(self):
        """method for instantiation"""

    def all(self):
        """method that returns the dictionary __objects"""

        dic_obj = FileStorage.__objects
        return dic_obj

    def new(self, obj):
        """method that sets in __objects the obj with key
        <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj


    def save(self):
        """method that serializes __objects to the
        JSON file (path: __file_path)"""
        py_dict = {}
        for keys, values in FileStorage.__objects.items():
            py_dict[keys] = values.to_dict()
        try:
            with open(FileStorage.__file_path, 'w'encoding='utf-8') as json_file:
                py_dict = json.dump(json_dict, json_file)
        except Exception as err:
            pass


    def reload(self):
        """method that deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise,
        do nothing. If the file doesn’t exist,
        no exception should be raised)"""


