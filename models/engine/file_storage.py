#!/usr/bin/python3
# file_storage.py
# Tiffany Walker and Ethan Zalta
"""This class will manage file storage, adding to and loading
from json formatted files"""

import json
import models


class FileStorage:
    """This Class is used for managing adding to and loading from files
    specifically in json format."""

    def all(self):
        """Returns each of the objects in ___objects dictionary"""
        return self.__objects

    def new(self, obj):
        """Creates a new object in __objects with key <obj class name>.id"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj
