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
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for k in kwargs:
                if k in ['created_at', 'updated_at']:
                    setattr(self, k, datetime.fromisoformat(kwargs[k]))
                elif k != '__class__':
                    setattr(self, k, kwargs[k])

    def __str__(self):
        """Returns a string representation of instance"""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """Updates 'updated_at' attribute with current datetime"""
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """Converts instance to dictionary format"""
        res = self.__dict__.copy()
        res['__class__'] = self.__class__.__name__
        res['created_at'] = self.created_at.isoformat()
        res['updated_at'] = self.updated_at.isoformat()
        return res