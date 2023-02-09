#!/usr/bin/python3
"""This model defines the base class for all models in the HBNB clone project"""

import uuid
from datetime import datetime

class BaseModel:
    """
    Base Class for all models.
    Attributes:
        id(string) - unique id of each BaseModel.
        created_at(datetime) - Current Datetime when instance was created
        updated_at(datetime) - Datetime of last update to object    
    """
    def __init__(self, *args, **kwargs):
        """Inititalizes an instance of BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of instance"""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """Updates 'updated_at' attribute with current datetime"""
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """Converts instance to dictionary format"""
        res = self.__dict__.copy()
        res[__class__] = self.__class__.__name__
        for k, v in res:
            if type(v) is datetime:
                res[k] = v.isoformat()
        return res