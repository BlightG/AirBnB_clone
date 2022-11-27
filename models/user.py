#!/usr/bin/python3
""" a module for user class manage users data """
import uuid
import models
from datetime import datetime
from models.base_model import BaseModel


class User(BaseModel):
    """
        a class that inhereits from BaseModel
        that manages user data
    """
    email = ""  # string - empty string
    password = ""  # string - empty string
    first_name = ""  # string - empty string
    last_name = ""  # string - empty string

    def __init__(self, *args, **kwargs):
        """ instansiation of the user class """
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
