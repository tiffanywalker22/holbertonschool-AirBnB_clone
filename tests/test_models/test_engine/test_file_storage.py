#!/usr/bin/python3
# test_engine_file_storage.py
# Tiffany Walker and Ethan Zalta
"""This is a Unittest class for testing the FileStorage Class"""

import unittest
from models.base_model import BaseModel
from models.engine import file_storage
from models.engine.file_storage import FileStorage
from models import storage
import pycodestyle
import os


class TestFileStorage(unittest.TestCase):

    def test_module_docstring(self):
        """Tests module docstring"""
        self.assertTrue(len(__import__("models").
                        engine.file_storage.__doc__) > 0)

    def test_class_docstring(self):
        """Tests the class DocString"""
        self.assertTrue(len(__import__('models').engine.file_storage.
                        FileStorage.__doc__) > 0)

    def test_pycodestyle_model(self):
        """Tests if model/base is pycodestyle compliant"""
        style = pycodestyle.StyleGuide(quiet=True)
        checkPyC = style.check_files(["models/engine/file_storage.py"])
        self.assertEqual(checkPyC.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pycodestyle_model(self):
        """Tests if test file is pycodestyle compliant"""
        style = pycodestyle.StyleGuide(quiet=True)
        checkPyC = style.check_files(["tests/test_models/test_engine/"
                                     "test_file_storage.py"])
        self.assertEqual(checkPyC.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_all(self):
        """testing all function"""
        self.my_obj = BaseModel()
        self.storage = FileStorage()
        test_dict = self.storage.all()
        self.assertIsInstance(test_dict, dict)
        self.assertIn(self.my_obj, test_dict.values())

    def test_new(self):
        """testing new function"""
        my_model = BaseModel()
        self.storage = FileStorage()
        self.storage.new(my_model)
        test_dict = self.storage.all()
        self.assertIn(my_model, test_dict.values())

    def test_save(self):
        """testing save function"""
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", "r") as file:
            all_data = file.read()
        self.assertTrue(len(all_data) > 0)

    def test_reload(self):
        """testing the reload"""
        pass
        # come back to this one
