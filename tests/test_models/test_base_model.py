#!/usr/bin/python3
"""
Unittest for BaseModel class
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import pep8
import time


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel"""

    def test_pep8_conformance_base_model(self):
        """Test that base_model.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")

    def test_pep8_conformance_test_base_model(self):
        """Test that test_base_model.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_base_model.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")

    def test_docstring_base_model(self):
        """Test for the presence of docstrings"""
        self.assertIsNotNone(BaseModel.__doc__)

    def test_is_instance(self):
        """Test that an object is an instance of BaseModel"""
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

    def test_attributes_exist(self):
        """Test that object has necessary attributes"""
        obj = BaseModel()
        self.assertTrue(hasattr(obj, "id"))
        self.assertTrue(hasattr(obj, "created_at"))
        self.assertTrue(hasattr(obj, "updated_at"))

    def test_created_at_updated_at(self):
        """Test that created_at and updated_at are datetime objects"""
        obj = BaseModel()
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_diff_datetime_objs(self):
        """Test that two instances have different created_at and updated_at"""
        obj1 = BaseModel()
        time.sleep(0.01)
        obj2 = BaseModel()
        self.assertNotEqual(obj1.created_at, obj2.created_at)
        self.assertNotEqual(obj1.updated_at, obj2.updated_at)

    def test_str_method(self):
        """Test the __str__ method output"""
        obj = BaseModel()
        output = str(obj)
        self.assertIn("[BaseModel]", output)
        self.assertIn("id", output)
        self.assertIn("created_at", output)
        self.assertIn("updated_at", output)


if __name__ == "__main__":
    unittest.main()

