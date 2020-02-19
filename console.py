#!/usr/bin/python3
""" Module that contains the program for the command line """


import cmd
import sys
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """ Class for the commmand line interpreter """
    intro = None
    prompt = '(hbnb) '
    file = None
    __models =["Amenity", "BaseModel", "City", "Place", "Review", "State",
               "User"]

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
                obj = take[0] + "." + take[1]
                del var[obj]
                models.storage.save()
            except:
                print("** no instance found **")

    def do_all(self, arg):
        """ Method that prints all string rep of all instances """
        all_instances = models.storage.all()
        if arg:
            if arg not in self.__models:
                print("** class doesn't exist **")
            else:
                for elem in all_instances.values():
                    if elem.__class__.__name__ == arg:
                        print(str(elem))
        else:
            for elem in all_instances.keys():
                print(str(all_instances[elem]))

    def do_update(self, args):
        """
        Method that updates an instance based on the class name
        and id
        """
        args = args.split( )
        if len(args) < 4:
            if len(args) == 0:
                print("** class name missing **")
            if len(args) == 1:
                print("** class id missing **")
            if len(args) == 2:
                print("** attribute name missing **")
            if len(args) == 3:
                print("** value missing **")
        else:
            all_instances = models.storage.all()
            id_list = [] # Stores matching classes id
            found_id = ""

            for var in all_instances.keys():
                name_id = var.split(".")
                if name_id[0] == args[0]:
                    id_list.append(name_id[1])

            if len(id_list) == 0: #There was no match in class_name"
                print("** class doesn't exist **")
                return

            for ids in id_list:
                if ids == args[1]: # If the Id exist in a class
                    found_id = ids
                    break

            if found_id == "": # No match was found
                print("** no instance found **")
                return

            key = (args[0] + "." + args[1])
            obj = all_instances[key]
            atr = args[2]
            obj.__dict__[atr] = args[3]
            obj.save()
            print(obj)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
