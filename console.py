#!/usr/bin/python3
"""
This program contains the entry point of the command interpreter
"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """this implements quit and EOF, help, a custom prompt"""
    prompt = '(hbnb) '
    classList = ["BaseModel"]

    def do_quit(self, arg):
        """This will help exit the program"""
        sys.exit(1)

    def do_EOF(self, arg):
        """This also exits the program, just like quit"""
        print()
        return True

    def emptyline(self):
        pass

    def help_help(self, arg):
        """The Help function provides the description of any given command"""
        print("It provides the description of commands")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
