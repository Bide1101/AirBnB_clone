
#!/usr/bin/python3
"""
This is a base model that defines all the common methods for other classes
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """" The actual class that defines all attributes"""
    def __init__(self, *args, **kwargs):
        """This is to initialize the basemodel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        if len(kwargs) < 0:
            storage.new(self)
        else:
            d = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == 'created_at':
                    value = datetime.strptime(kwargs[key], d)
                elif key == 'updated_at':
                    value = datetime.strptime(kwargs[key], d)
                elif key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """This function prints the string
        rerprewsentation of the basemodel
        """
        return ("[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """"This updates the public instance attribute with current datetime"""
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """This returns a dictionary containing all keys/
        values of __dict__ of some instances
        """
        newDict = {}
        newDict["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if isinstance(value, (datetime, )):
                newDict[key] = value.isoformat()
            else:
                newDict[key] = value
        return newDict
