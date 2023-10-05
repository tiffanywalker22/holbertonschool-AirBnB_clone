#!/usr/bin/python3
# base_model.py
# Tiffany Walker and Ethan Zalta
"""Creating the class BaseModel"""

import uuid
from datetime import datetime
import models

class BaseModel:
    """ Our class for Base """
    def __init__(self, *args, **kwargs):
        """ initalizes new instance of basemodel """
        if kwargs:
            for key, value in kwargs.items():
                my_list = ["created_at, updated_at"]
                if key in my_list:
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = (datetime.now())
            self.updated_at = self.created_at

    def save(self):
        """ updates 'updated_at with current datetime """
        self.updated_at = (datetime.now())
        models.storage.save()

    def to_dict(self):
        """ converts instance to dictionary representation """
        class_name = self.__class__.__name__
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = class_name
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict
    
    def __str__(self):
        """ string rep of instance """
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

