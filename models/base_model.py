#!/usr/bin/python3
"""
A model to implement BaseModel class
"""
import uuid

from datetime import datetime
from models import storage


class BaseModel:
    """
    A class that defines the common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the BaseModel class
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new()
        else:
            for k, v in kwargs.items():
                if k != '__class__':
                    if k in ['created_at', 'updated_at']:
                        setattr(self, k, datetime.fromisoformat(v))
                    else:
                        setattr(self, k, v)

    def __str__(self):
        """
        Returns the string representation of the class 'BaseModel'
        """
        return (f'{type(self).__name__} {self.id} {self.__dict__}')

    def save(self):
        """
        Updates 'self.updated_at' with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containign all keys/values of __dict__
        of the instance
        """
        dicto = self.__dict__.copy()
        dicto['__class__'] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if k in ['created_at', 'updated_at']:
                v = self.__dict__[k].isoformat()
                dicto[k] = v
        return dicto
