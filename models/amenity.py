#!/usr/bin/python3
"""
Amenities included in the apartments
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Represents an amenity available in apartments """
    name = ""
