#!/usr/bin/python3
"""Initalizes models as a module"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
