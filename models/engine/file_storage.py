#!/usr/bin/python3


import json
import os.path

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
        self.__objects = obj

    def save(self):
        """serializes __objects to the json file"""
        new_dict = {}
        for i in self.__objects:
            new_dicti[ = self.__objects[i].to_dict()
        with open(self__file_path, 'w') as fil:
            json.dump(new_dict, fil)

    def reload(self):
        """deserializes the Json file to __objects."""
        if os.path.exists(_file_path) is True:
            with open(__file_path, 'r') as f:
                __objects = json.load(f)
