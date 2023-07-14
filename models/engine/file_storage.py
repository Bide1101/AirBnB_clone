#!/usr/bin/python3
"""
Task 5
to store first object, and to make sure the python code
is  not just easily readable, but usable with another language,
we convert the dictionary representation to a JSON string
"""
import json
import os
from models.base_model import BaseModel
# from models.base_model import BaseModel

class FileStorage:
    """this sertializes instance to a JSON file and deserializes vice versa"""
    __file_path = "file.json"
    __objects = {}
    classDict = {'BaseModel': BaseModel} # should be filled when the classes to be reloaded are created later

    def all(self):
        """This returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """This setrs in objects with a specified key and value"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """This serializes __objects to the JSON file"""
        newDict = {}
        for key, value in FileStorage.__objects.items():
            newDict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as jsonfile:
            json.dump(newDict, jsonfile)

    def reload(self):
        """This deserializes JSON files to objects if the exist"""
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as jfile:
                all_objs = json.loads(jfile.read())
            for obj_id, obj in all_objs.items():
                name_class = obj_id.split(".")[0]
                self.new(eval(name_class + "(**obj)"))
        except:
            pass
