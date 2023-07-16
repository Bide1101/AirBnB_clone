#!/usr/bin/python3
"""
subclass Review about the apartments
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """subclass that contains reviews from previous and current users"""
    place_id = ""
    user_id = ""
    text = ""
