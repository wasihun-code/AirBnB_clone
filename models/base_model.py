#!/usr/bin/python3
"""A class that defines all common attributes for other class."""


import uuid
import models
from datetime import datetime


class BaseModel():
    """Documentation for BaseModel class."""

    def __init__(self, *args, **kwargs):
        """kwargs - unpacking dictionaries and setting attributes"""
        if (kwargs != {} and kwargs is not None):
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    vals = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, vals)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """prints class information"""
        cls = self.__class__.__name__
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """updates the tiem of updated_now to current time"""
        updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Creates a dictionary object for serialization/deserialization"""
        a_dict = self.__dict__.copy()
        a_dict["created_at"] = self.created_at.isoformat()
        a_dict["updated_at"] = self.updated_at.isoformat()
        a_dict["__class__"] = self.__class__.__name__
        return a_dict
