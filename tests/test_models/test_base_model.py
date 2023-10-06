#!/usr/bin/python3
# test_base_model.py
# Tiffany Walker and Ethan Zalta
"""This is a Unittest class for testing the Base Model"""

import unittest
from models.base_model import BaseModel
import pycodestyle
import os


class TestBase(unittest.TestCase):

    def test_module_docstring(self):
        """Tests module docstring"""
        self.assertTrue(len(__import__("models").base_model.__doc__) > 0)

    def test_class_docstring(self):
        """Tests the class DocString"""
        self.assertTrue(len(__import__('models').
                        base_model.BaseModel.__doc__) > 0)

    def test_pycodestyle_model(self):
        """Tests if model/base is pycodestyle compliant"""
        style = pycodestyle.StyleGuide(quiet=True)
        checkPyC = style.check_files(["models/base_model.py"])
        self.assertEqual(checkPyC.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pycodestyle_model(self):
        """Tests if test file is pycodestyle compliant"""
        style = pycodestyle.StyleGuide(quiet=True)
        checkPyC = style.check_files(["tests/test_models/test_base_model.py"])
        self.assertEqual(checkPyC.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_create_class(self):
        """Test Creating Class correctly"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        self.assertEqual(my_model.name, "My First Model")
        self.assertEqual(my_model.my_number, 89)

    def test_class_attributes(self):
        """Testing regular attributes of Base Model Class"""
        my_model = BaseModel()
        self.assertEqual(len(my_model.id), 36)
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))
        self.assertTrue(hasattr(my_model, "id"))
        self.assertIsInstance(my_model, BaseModel)

    def test_save_function(self):
        """Testing the update/save function"""
        my_model = BaseModel()
        origin = my_model.updated_at
        my_model.save()
        self.assertNotEqual(origin, my_model.updated_at)

    def test_to_json(self):
        """Testing the json formatting of to_dict func"""
        my_model = BaseModel()
        test_dict = my_model.to_dict()
        self.assertIsInstance(test_dict, dict)
        self.assertIsInstance(test_dict["updated_at"], str)

    def test__str__(self):
        """Checks correct formatting for __str__ method"""
        my_model = BaseModel()
        self.assertEqual(my_model.__str__(),
                         (f"[{my_model.__class__.__name__}] "
                         f"({my_model.id}) {my_model.__dict__}"))
