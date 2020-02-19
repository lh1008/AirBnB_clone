#!/usr/bin/python3
""" Module that contains the program for the command line """


import cmd
import sys
import json
import models
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """ Class for the commmand line interpreter """
    intro = None
    prompt = '(hbnb) '
    file = None
    __models =[
        "BaseModel"
        ]

    """====================================================================="""
    """== METHODS =========================================================="""
    """====================================================================="""

    def do_EOF(self, arg):
        """ Method EOF to exit the program """
        return True

    def do_quit(self, arg):
        """ Method exit to exit the program """
        return True

    def emptyline(self):
        """ Method empty line with enter """
        pass

    def do_create(self, arg):
        """ Method to create new instance """
        take = arg.split( )
        if not arg:
            print("** class name missing **")
        elif take[0] not in self.__models:
            print("** class doesn't exist **")
        else:
            var = eval(take[0])()
            var.save()
            print(var.id)

    def do_show(self, arg):
        """
        Method that prints representation of an instance based
        on the class name
        """
        take = arg.split( )
        if not arg:
            print("** class name missing **")
        elif take[0] not in self.__models:
            print("** class doesn't exist **")
        elif len(take) < 2:
            print("** instance id missing **")
        else:
            var = models.storage.all()
            try:
                obj = var[take[0]+"."+take[1]]
                print(obj)
            except:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Method that deletes an instance based on the class
        name and id
        """
        take = arg.split( )
        if not arg:
            print("** class name missing **")
        elif take[0] not in self.__models:
            print("** class doesn't exist **")
        elif len(take) < 2:
            print("** instance id missing **")
        else:
            var = models.storage.all()
            try:
                obj = take[0]+"."+take[1]
                del var[obj]
                models.storage.save()
            except:
                print("** no instance found **")

    def do_all(self, arg):
        """ Method that prints all string rep of all instances """
        if arg:
            if arg not in self.__models:
                print("** class doesn't exist **")
            else:
                for i in self.__models:
                    print(self.__models)
        else:
            print(models.storage.all())

if __name__ == '__main__':
    HBNBCommand().cmdloop()
