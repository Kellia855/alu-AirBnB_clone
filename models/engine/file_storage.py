#!/usr/bin/python3
"""This module defines FileStorage for BaseModel only"""

import json
from models.base_model import BaseModel


class FileStorage:
    """Serializes BaseModel instances to a JSON file and deserializes back"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of all objects"""
        return self.__objects

    def new(self, obj):
        """Add new BaseModel object to __objects with key <class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to JSON file"""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialize JSON file to __objects"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
            for key, val in obj_dict.items():
                self.__objects[key] = BaseModel(**val)
        except FileNotFoundError:
            # If file doesn't exist, do nothing
            pass

