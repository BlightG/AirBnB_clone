#!/usr/bin/python3
""" a module for Place class manage Places place data """
import uuid
import models
from datetime import datetime
from models.base_model import BaseModel


class Place(BaseModel):
    """
        a class that inhereits from BaseModel
        that manages Place data
    """
    city_id = ""  # string - empty string: it will be the City.id
    user_id = ""  # string - empty string: it will be the User.id
    name = ""  # string - empty string
    description = ""  # string - empty string
    number_rooms = 0  # integer - 0
    number_bathrooms = 0  # integer - 0
    max_guest = 0  # integer - 0
    price_by_night = 0  # integer - 0
    latitude = 0.0  # float - 0.0
    longitude = 0.0  # float - 0.0
    amenity_ids = []  # list of string - empty list:
#                    it will be the list of Amenity.id later

    def __init__(self, *args, **kwargs):
        """ instansiation of the Place class """
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
