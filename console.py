#!/usr/bin/python3
""" Module that contains the program for the command line """


import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """ Class for the commmand line interpreter """
    intro = None
    prompt = '(hbnb) '
    file = None

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
