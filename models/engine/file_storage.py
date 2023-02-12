#!/usr/bin/python3
"""Serializes instances to JSON and deserializes JSON to instances."""

import json


class FileStorage:
    """Serializes and Deserializes instances <-> JSON."""
    __file_path = "str"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets object into '__objects'."""
        FileStorage.__objects.update({obj.to_dict()['__class__'] + '.' + obj.id : obj})

    def save(self):
        """Saves storage"""
        with open(FileStorage.__file_path, 'w') as f:
            json.dumps(FileStorage.__objects, f)