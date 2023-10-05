#!/usr/bin/python3
# base_model.py

import uuid
import datetime

class Basemodel:
    """ Our class for Base """
    def __init__(self):
        """ initalizes new instance of basemodel """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def save(self):
        """ updates 'updated_at with current datetime """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ converts instance to dictionary representation """
        class_name = self.__class__.__name__
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = class_name
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict
    

