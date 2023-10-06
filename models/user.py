#!/usr/bin/python3
# user.py
# Tiffany Walker and Ethan Zalta
"""User class"""


from models.base_model import BaseModel


class User(BaseModel):
    """User class inherited from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
