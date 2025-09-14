#!/usr/bin/python3
"""
Review class definition
"""
from models.engine.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""