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
        for i in FileStorage.__objects:
            new_dict[i] = self.__objects[i].to_dict()
            with open(self.__file_path, 'w') as fil:
                json.dump(new_dict, fil)

    def reload(self):
        """deserializes the Json file to __objects."""
        try:
            with open(self.__file_path, 'r') as f:
                json_file = json.load(f)
                for key in json_file:
                    self.__objects[key] = classes[json_file[key]["__class__"]](**json_file[key])
        except:
            pass
