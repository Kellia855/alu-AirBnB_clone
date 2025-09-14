#!/usr/bin/python3

import json
import os

class FileStorage:
    """Serializes instances to a JSON file & deserializes back"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return dictionary of objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Add new object to __objects"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to JSON file"""
        obj_dict = {
            key: obj.to_dict() for key, obj in FileStorage.__objects.items()
        }
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialize JSON file to __objects"""
        if not os.path.exists(FileStorage.__file_path):
            return
        try:
            with open(FileStorage.__file_path, "r") as f:
                obj_dict = json.load(f)
            from models.base_model import BaseModel  # 
            for key, value in obj_dict.items():
                cls_name = value["__class__"]
                if cls_name == "BaseModel":
                    FileStorage.__objects[key] = BaseModel(**value)
        except Exception:
            pass
