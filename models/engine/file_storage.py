#!/usr/bin/python3
""" This class serializes instances to a JSON file and deserializes Json files
    to instances.                                                           """

import json
from models.base_model import BaseModel
import models.user


class FileStorage():
    """ This class handels Json files with instances, it has 2 private class
        attributes and 4 public instance methods"""

    """====================================================================="""
    """= INIT & CLASS VARIABLES ============================================"""
    """====================================================================="""

    def __init__(self):
        """ Initializes the class. """
        self.__file_path = "file.json"
        self.__objects = {}

    """====================================================================="""
    """== METHODS =========================================================="""
    """====================================================================="""

    """-----------"""
    """- Public --"""
    """-----------"""
    def all(self):
        """ Returns a dictionary containing __objects. """
        return self.__objects

    def new(self, obj):
        """ Creates a new dictionary representation to save into a file. """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """ Saves the data into the HDD via a file. """
        dic = {}
        for k, v in self.__objects.items():
            dic[k] = v.to_dict()

        with open(self.__file_path, 'w') as jfile:
            json.dump(dic, jfile)

    def reload(self):
        """ Loads the data from the HDD into an instance. """
        new_dic = {}
        try:
            with open(self.__file_path, 'r') as jfile:
                var = json.load(jfile)

                for key, value in var.items():
                    self.__objects[key] = eval(value['__class__'])(**value)

        except:
            pass

    """-----------"""
    """- Private -"""
    """-----------"""

    """-----------"""
    """-- Class --"""
    """-----------"""

    """-----------"""
    """-- Static -"""
    """-----------"""

    """====================================================================="""
    """== SETTERS & GETTERS ================================================"""
    """====================================================================="""
