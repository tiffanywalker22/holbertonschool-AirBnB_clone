#!/usr/bin/python3
# test_place.py
# Tiffany Walker and Ethan Zalta
"""This is a Unittest class for testing the Place Class"""

import unittest
from models.base_model import BaseModel
from models.place import Place
import pycodestyle
import os


class TestBase(unittest.TestCase):

    def test_module_docstring(self):
        """Tests module docstring"""
        self.assertTrue(len(__import__("models").place.__doc__) > 0)

    def test_class_docstring(self):
        """Tests the class DocString"""
        self.assertTrue(len(__import__('models').place.Place.__doc__) > 0)

    def test_pycodestyle_model(self):
        """Tests if model/base is pycodestyle compliant"""
        style = pycodestyle.StyleGuide(quiet=True)
        checkPyC = style.check_files(["models/place.py"])
        self.assertEqual(checkPyC.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pycodestyle_model(self):
        """Tests if test file is pycodestyle compliant"""
        style = pycodestyle.StyleGuide(quiet=True)
        checkPyC = style.check_files(["tests/test_place.py"])
        self.assertEqual(checkPyC.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_create_class(self):
        """Test Creating Class correctly"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        self.assertEqual(my_model.name, "My First Model")
        self.assertEqual(my_model.id, 89)
