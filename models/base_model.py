#!/bin/python3
""" A Basemodel for airbnb project """
import uuid
from datetime import datetime
import models


class BaseModel():
    """ A base for manipulating Airbnb """

    def __init__(self, *args, **kwargs):
        """ initalization of BaseModel """
        if kwargs:
            self.__dict__ = {
                **kwargs,
                "created_at": datetime.fromisoformat(kwargs["created_at"]),
                "updated_at": datetime.fromisoformat(kwargs["updated_at"]),
                "__class__": ""
            }
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """ updates the basemodels time and date """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def __str__(self):
        """ prints a string representation of an instance"""
        return "[{}]({}) {}".format(self.__class__.__name__,
                                    self.id, self.__dict__)

    def __setattr__(self, key, value):
        """ sets attribute for a class """
        object.__setattr__(self, key, value)
        object.__setattr__(self, 'updated_at', datetime.now())

    def to_dict(self):
        """
            returns a dictionary containing all the
            keys/value pairs of __dict__ of the instance
        """
        return {
                **self.__dict__,
                "__class__": self.__class__.__name__,
                "updated_at": self.updated_at.isoformat(),
                "created_at": self.created_at.isoformat()
                }
