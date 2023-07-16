#!/usr/bin/python3

"""
Where the city address is located in
"""


from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city with its associated information"""
    state_id = ""
    name = ""
