#!/usr/bin/python3
"""
Task 5
to store first object, and to make sure the python code
is  not just easily readable, but usable with another language,
we convert the dictionary representation to a JSON string
"""
import json
import os
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
            from models.base_model import BaseModel
            objDict = {}
            with open(self.__file_path, mode="r", encoding="UTF-8") as newFile:
                for key, value in json.load(newFile).items():
                    objDict = self.new(classDict[value['__class__']](**value))
                    self.__objects[key] = objDict

        except (FileNotFoundError, NameError): # delete name error when classDict is available
            """this makes sure no error is raised if the file is not found"""
            pass
