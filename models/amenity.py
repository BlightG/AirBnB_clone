#!/sr/bin/python3
""" a module for Amenity
 class manage Amenity
s data """
import uuid, models
from datetime import datetime
from models.base_model import BaseModel



class Amenity(BaseModel):
    """
        a class that inhereits from BaseModel 
        that manages Amenity data 
    """
    name = "" #string - empty string
    
    def __init__(self, *args, **kwargs):
        """ instansiation of the Amenity class """
        if  kwargs:
            self.__dict__ = {
                 **kwargs, "created_at":datetime.fromisoformat(kwargs["created_at"]),
                "updated_at":datetime.fromisoformat(kwargs["updated_at"]),
                "__class__":""
            }
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            models.storage.new(self)
