#!/usr/bin/python3
# test_city.py
# Tiffany Walker and Ethan Zalta
"""This is a Unittest class for testing the City Class"""

import unittest
from models.base_model import BaseModel
from models.city import City
import pycodestyle
import os


class TestBase(unittest.TestCase):

    def test_module_docstring(self):
        """Tests module docstring"""
        self.assertTrue(len(__import__("models").city.__doc__) > 0)

    def test_class_docstring(self):
        """Tests the class DocString"""
        self.assertTrue(len(__import__('models').city.City.__doc__) > 0)

    def test_pycodestyle_model(self):
        """Tests if model/base is pycodestyle compliant"""
        style = pycodestyle.StyleGuide(quiet=True)
        checkPyC = style.check_files(["models/city.py"])
        self.assertEqual(checkPyC.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pycodestyle_model(self):
        """Tests if test file is pycodestyle compliant"""
        style = pycodestyle.StyleGuide(quiet=True)
        checkPyC = style.check_files(["tests/test_city.py"])
        self.assertEqual(checkPyC.total_errors, 0,
                         "Found code style errors (and warnings).")
