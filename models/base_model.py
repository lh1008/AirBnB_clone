#!/usr/bin/python3
""" This is the base class for the AirBnB clone """

import datetime
import uuid
from models import storage


class BaseModel():
    """ This class is the base model for all the AirBnB subclasses. """

    """====================================================================="""
    """= INIT & CLASS VARIABLES ============================================"""
    """====================================================================="""

    def __init__(self, *args, **kwargs):
        """ Initializes the class. """
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

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
        updated = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__ of the
            instance.                                                       """
        diction = {}
        diction['__class__'] = self.__class__.__name__

        if self.__dict__:
            for key, value in self.__dict__.items():
                if isinstance(value, datetime.datetime) is True:
                    value = value.isoformat()
                diction[key] = value

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
