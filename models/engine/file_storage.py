#!/usr/bin/python3


class FileStorage():
    """Serializes and deserialize json and instances to one another."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return __objects
    def new(self, obj):
        pass
    def save(self):
        pass
    