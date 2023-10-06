#!/usr/bin/python3
# file_storage.py
# Tiffany Walker and Ethan Zalta
"""This class will manage file storage, adding to and loading
from json formatted files"""

import json
import os
import models
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """This Class is used for managing adding to and loading from files
    specifically in json format."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns each of the objects in ___objects dictionary"""
        return self.__objects

    def new(self, obj):
        """Creates a new object in __objects with key <obj class name>.id"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serializes __objects then puts into json file"""
        objDict = {}
        for key, value in self.__objects.items():
            objDict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(objDict))

    def reload(self):
        """Loads a json file, deserializes json to __objects,
        if no file exists, no exception is raised."""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                objDict = json.loads(file.read())
                for key, value in objDict.items():
                    self.__objects[key] = eval(value["__class__"])(**value)
        except Exception as e:
            pass

    allowed_classes = [BaseModel, User]
