#!/usr/bin/python3
""" a module for review class manage reviews data """
import uuid
import models
from datetime import datetime
from models.base_model import BaseModel


class Review(BaseModel):
    """
        a class that inhereits from BaseModel
        that manages review data
    """
    place_id = ""  # string - empty string: it will be the Place.id
    user_id = ""  # string - empty string: it will be the User.id
    text = ""  # string - #empty string

    def __init__(self, *args, **kwargs):
        """ instansiation of the review class """
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
