#!/usr/bin/python3
"""Serializes instances to JSON and deserializes JSON to instances."""

import json


class FileStorage:
    """Serializes and Deserializes instances <-> JSON."""
    __file_path = "str"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets object into '__objects'."""
        self.__objects.update({obj.to_dict()['__class__'] + '.' + obj.id : obj})

    def save(self):
        """Saves objects to a file in json format"""
        with open(self.__file_path, 'w') as f:
            tmp = {}
            tmp = self.__objects
            for k, v in tmp.items():
                tmp[k] = val.to_dict()
            json.dump(tmp, f)

    def reload(self):
        """Unloads objects from a json file"""
        from models.base_model import BaseModel


        try:
            tmp = {}
            with open(self.__file_path, 'r') as f:
                tmp = json.load(f)
                for key, val in tmp.items():
                    self.__objects[key] = BaseModel(**val)
        except FileNotFoundError:
            pass