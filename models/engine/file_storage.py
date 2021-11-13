#!/usr/bin/python3


import json
import os.path

class FileStorage():
    """Serializes and deserialize json and instances to one another."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return __objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        cls = self.__class__.__name__
        key = cls.id

    def save(self):
        """serializes __objects to the json file"""
        with open(__file_path, 'w') as f:
            json.dump(_objects, f)

    def reload(self):
        """deserializes the Json file to __objects."""
        if os.path.exists(_file_path) is True:
            with open(__file_path, 'r') as f:
                __objects = json.load(f)
