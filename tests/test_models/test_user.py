#!/usr/bin/python3
"""unittests for models/user.py."""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
     """Unittests for testing the User class."""

     def test_user_attributes(self):
        self.assertEqual(User, type(User()))

if __name__ == '__main__':
    unittest.main()
