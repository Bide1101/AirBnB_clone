#!/usr/bin/python3
"""
This program contains the entry point of the command interpreter
"""


import cmd
import sys
from models.base_model import BaseModel
import json
from models import storage
from models.user import User
from models. state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classDict = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
        }
"""
classDict = ["BaseModel",
            "User",
            "State",
            "City",
            "Amenity",
            "Review"
            "Place"]
"""
class HBNBCommand(cmd.Cmd):
    """this implements quit and EOF, help, a custom prompt"""
    prompt = '(hbnb) '
    # classDict = {"BaseModel": BaseModel}

    def do_quit(self, arg):
        """This will help exit the program"""
        sys.exit(1)

    def do_EOF(self, arg):
        """This also exits the program, just like quit"""
        print()
        return True

    def emptyline(self):
        """This does not do anything"""
        pass

    def help_help(self, arg):
        """The Help function provides the description of any given command"""
        print("It provides the description of commands")

    def do_create(self, className):
        """This creates a new instance of BaseModel and prints the id"""
        if not className:
            print("** class name missing **")
        elif className not in classDict:
            print("** class doesn't exist **")
        else:
            # arguments = className.split(" ")
            newInstance = eval(className)()
            # id = getattr(newI
            newInstance.save()
            print(newInstance.id)

    def do_show(self, className):
        """This prints the string representation of
        an instance based on classname and id
        """
        if not className:
            print("** class name missing **")
        else:
            className = className.split()
            if len(className) != 2:
                print("** instance id missing **")
            elif className[0] not in classDict:
                print("** class doesn't exist **")
            else:
                for key, value in storage.all().items():
                    if className[1] == value.id:
                        print(value)
                        return
                print("** no instance found **")

    def do_destroy(self, className):
        """Deletes an instance based on the class name and id"""
        if not className:
            print("** class name missing **")
            return
        else:
            className = className.split()
            if len(className) != 2:
                print("** instance id missing **")
                return
            elif className[0] not in classDict:
                print("** class doesn't exist **")
                return
            else:
                for key, value in storage.all().items():
                    if className[1] == value.id:
                        del storage.all()[key]
                        storage.save()
                        return
                print("** no instance found **")

    def do_all(self, className):
        """This prints all string representation of all instances
        based or not on the class name
        """
        if not className:
            print("** class name missing **")
            return
        names = className.split(" ")
        if names[0] not in classDict:
            print("** class doesn't exist **")
        else:
            allObjects = storage.all()
            instanceList = []
            for key, value in allObjects.items():
                objectName = value.__class__.__name__
                if objectName == names[0]:
                    instanceList += [value.__str__()]
                    print(instanceList)
        # args = className.split('.')
        # if not className.endswith('.all()'):
            # print("Invalid command format. Usage: <class name>.all()")
            # return

        # class_name = className[:-6]
        # if class_name not in classDict:
            # print("** Class doesn't exist **")
            # return

        # instances = classDict[class_name].all()
        # for instance in instances:
            # print(str(instance))

    def do_update(self, arguments):
        """This updates an instance based on the class name and id 
        by adding or updating the attribute
        and saves the changes to the JSON file
        """
        argt = arguments.split()
        if len(argt) == 0:
            print("** class name missing **")
            return False
        elif argt[0] not in classDict:
            print("** class doesn't exist **")
        elif argt[0] in classDict:
            if len(argt) > 1:
                key = argt[0] + "." + argt[1]
                if key in storage.all():
                    if len(argt) > 2:
                        if len(argt) > 3:
                            setattr(storage.all()[key], argt[2], argt[3])
                            storage.all()[key].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")

    def count(self, className):
        """This retrieves the number of instances of a class"""
        # if className in HBNBCommand.classDict:
        count = 0
        allObjects = storage.all()
            # for key, value in allObjects.all().items():
        for nameID in allObjects.keys():
            if nameID.split(".")[0] == className:
                # clasS = key.split('.')
                # if clasS[0] == className:
                # if className in key:
                count += 1
        print(count)
            # else:
            # print("** class doesn't exist **")

    def parse(arg):
        return tuple(arg.split())
if __name__ == '__main__':
    HBNBCommand().cmdloop()
