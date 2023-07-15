#!/usr/bin/python3
"""
This is a class User that inheritds from baseModel
"""


from models.base_model import BaseModel


class User(BaseModel):
    """This class inherits and has the folloeing public attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
