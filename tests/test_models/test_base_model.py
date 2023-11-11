#!/usr/bin/python3
"""modules"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import os
from uuid import uuid4
import json


class TestBaseModel(unittest.TestCase):
    """test cases"""


    def setUp(self):
        self.my_model = BaseModel()
        self.my_model.name = "My_First_Model"
        self.my_model.my_number = 89

    def test_instantiation(self):
        self.assertIsInstance(self.my_model, BaseModel)
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)
        self.assertIsInstance(self.my_model.id, str)

    def test_str_representation(self):
        expected_str = "[BaseModel] ({}) {}".format(self.my_model.id, self.my_model.__dict__)
        self.assertEqual(str(self.my_model), expected_str)

    def test_to_dict(self):
        my_model_dict = self.my_model.to_dict()
        expected_keys = ['id', 'created_at', 'updated_at', 'name', 'my_number', '__class__']
        self.assertCountEqual(my_model_dict.keys(), expected_keys)
        self.assertIsInstance(my_model_dict['created_at'], str)
        self.assertIsInstance(my_model_dict['updated_at'], str)
        self.assertEqual(my_model_dict['name'], "My_First_Model")
        self.assertEqual(my_model_dict['my_number'], 89)

    def test_json_conversion(self):
        my_model_json = json.dumps(self.my_model.to_dict())
        my_new_model = BaseModel(**json.loads(my_model_json))

        self.assertEqual(self.my_model.id, my_new_model.id)
        self.assertEqual(self.my_model.created_at, my_new_model.created_at)
        self.assertEqual(self.my_model.updated_at, my_new_model.updated_at)
        self.assertEqual(self.my_model.name, my_new_model.name)
        self.assertEqual(self.my_model.my_number, my_new_model.my_number)
        self.assertIsInstance(my_new_model, BaseModel)

if __name__ == '__main__':
    unittest.main()
