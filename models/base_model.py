#!/usr/bin/python3
""" This is the base class for the AirBnB clone """

import datetime
import uuid
import models


class BaseModel():
    """ This class is the base model for all the AirBnB subclasses. """

    """====================================================================="""
    """= INIT & CLASS VARIABLES ============================================"""
    """====================================================================="""

    def __init__(self, *args, **kwargs):
        """ Initializes the class. """

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

        else:
            for key in kwargs:
                if key == 'created_at' or key == 'updated_at':
                    formt = "%Y-%m-%dT%H:%M:%S.%f"
                    self.__dict__[key] = datetime.datetime.strptime(
                        kwargs[key], formt)
                elif key != '__class__':
                    self.__dict__[key] = kwargs[key]

    """====================================================================="""
    """== METHODS =========================================================="""
    """====================================================================="""

    """-----------"""
    """- Public --"""
    """-----------"""

    def __str__(self):
        """ Defines what the class should print. """
        name = self.__class__.__name__
        text = ("[{}] ({}) {}".format(name, self.id, self.__dict__))
        return text

    def save(self):
        """ Updates the public instance attribute "update_at" with the current
            datetime.                                                       """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__ of the
            instance.                                                       """
        diction = self.__dict__.copy()
        diction['__class__'] = self.__class__.__name__
        diction['updated_at'] = diction['updated_at'].isoformat()
        diction['created_at'] = diction['created_at'].isoformat()

        return diction

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
