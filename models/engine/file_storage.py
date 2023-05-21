#!/usr/bin/python3
"""
An engine model to implement the FileStorage class
"""


import json


class FileStorage:
    __file_path = "file.json"
    __objects = dict()
    
    def __init__(self):
        """
        Initializes an object of the FileStorage class
        """
        pass

    def all(self):
        """
        Returns the dictionary '__objects'
        """
        return self.__objects
    
    def new(self, obj):
        """
        Stores a new object in __objects
        """
        self.__objects[f"{obj.__class__.__name__}.id"] = obj

    def save(self):
        """
        Serializes __objects to the json file
        """
        with open(self.__file_path, 'w') as f:
            json.dump(self.__objects, f)
    
    def reload(self):
        """
        Deserializes the json file(If it exists)
        """
        try:
            with open(self.__file_path, 'r') as f:
                temp = json.load(f)
                for i in temp:
                    self.__objects[i] = temp[i]

        except:
            pass