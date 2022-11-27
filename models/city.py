#!/usr/bin/python3
""" a module for City class manage Citys data """
import uuid
import models
from datetime import datetime
from models.base_model import BaseModel


class City(BaseModel):
    """
        a class that inhereits from BaseModel
        that manages City data
    """
    state_id = ""  # string - empty string: it will be the State.id
    name = ""  # string - empty string

    def __init__(self, *args, **kwargs):
        """ instansiation of the City class """
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
