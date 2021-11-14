#!/usr/bin/python3


import json
from models.base_model import BaseModel


class FileStorage():
    """Serializes and deserialize json and instances to one another."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        i = obj.__class__.__name__ + '.' + obj.id
        self.__objects[i] = obj

    def save(self):
        """serializes __objects to the json file and uses pandas to_json"""
        a_dict = {}
        for key in self.__objects.keys():
            a_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(a_dict, f)

    def reload(self):
        """deserializes the Json file to __objects."""
        try:
            with open(self.__file_path, 'r') as f:
                _objects = json.load(f)
        except:
            pass
