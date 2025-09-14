#!/usr/bin/python3
import unittest
from datetime import datetime
import os
import json
from models.engine.base_model import BaseModel
from models.engine import storage


class TestBaseModel(unittest.TestCase):
    """Unit tests for BaseModel class with FileStorage integration."""

    def setUp(self):
        """Set up for tests: clear storage and file before each test."""
        storage._FileStorage__objects = {}
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """Clean up after tests."""
        storage._FileStorage__objects = {}
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_attributes(self):
        """Test standard attributes of BaseModel."""
        bm = BaseModel()
        self.assertIsInstance(bm.id, str)
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)
        self.assertEqual(str(bm), f"[BaseModel] ({bm.id}) {bm.__dict__}")

    def test_save_updates_updated_at_and_creates_file(self):
        """Test save() updates updated_at and writes JSON to file."""
        bm = BaseModel()
        old_updated_at = bm.updated_at
        bm.save()
        self.assertNotEqual(bm.updated_at, old_updated_at)
        self.assertTrue(os.path.exists("file.json"))

        # Check JSON file content
        with open("file.json", "r") as f:
            data = json.load(f)
        key = f"BaseModel.{bm.id}"
        self.assertIn(key, data)
        self.assertEqual(data[key]["id"], bm.id)

    def test_to_dict_contains_expected_keys(self):
        """Test that to_dict() contains all expected keys."""
        bm = BaseModel()
        bm.name = "Test"
        bm.my_number = 42
        d = bm.to_dict()
        self.assertEqual(d["__class__"], "BaseModel")
        self.assertEqual(d["name"], "Test")
        self.assertEqual(d["my_number"], 42)
        self.assertIsInstance(d["created_at"], str)
        self.assertIsInstance(d["updated_at"], str)

    def test_kwargs_instantiation(self):
        """Test creating BaseModel instance from dictionary."""
        bm = BaseModel()
        bm.name = "KwargsTest"
        bm.my_number = 100
        bm_json = bm.to_dict()
        bm_new = BaseModel(**bm_json)
        self.assertEqual(bm.id, bm_new.id)
        self.assertEqual(bm.name, bm_new.name)
        self.assertEqual(bm.my_number, bm_new.my_number)
        self.assertIsInstance(bm_new.created_at, datetime)
        self.assertIsInstance(bm_new.updated_at, datetime)
        self.assertFalse(bm is bm_new)

    def test_storage_new_and_all(self):
        """Test that a new instance is added to storage."""
        bm = BaseModel()
        key = f"BaseModel.{bm.id}"
        self.assertIn(key, storage.all())
        self.assertIs(storage.all()[key], bm)

    def test_reload_restores_objects(self):
        """Test that reload() restores objects from file.json."""
        bm = BaseModel()
        bm.name = "ReloadTest"
        storage.save()

        # Clear storage and reload
        storage._FileStorage__objects = {}
        storage.reload()

        all_objs = storage.all()
        key = f"BaseModel.{bm.id}"
        self.assertIn(key, all_objs)
        reloaded_obj = all_objs[key]
        self.assertEqual(reloaded_obj.id, bm.id)
        self.assertEqual(reloaded_obj.name, "ReloadTest")
        self.assertIsInstance(reloaded_obj.created_at, datetime)
        self.assertIsInstance(reloaded_obj.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()

