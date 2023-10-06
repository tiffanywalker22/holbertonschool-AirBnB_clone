#!/usr/bin/python3
# review.py
# Tiffany Walker and Ethan Zalta
"""Class Review"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Review class inherited from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
