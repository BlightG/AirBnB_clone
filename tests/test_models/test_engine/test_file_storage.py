#!/usr/bin/python3
""" test module for File Storage """
import unittest
import time
import io
import sys
import datetime
from models.engine.file_storage import FileStorage


class Test_FileStorage(unittest.TestCase):
    """ checks certain aspects of Amenity Class"""
    def test_equal(self):
        """ checks the sucess cases of Amenity """
        test_object = FileStorage()
        self.assertIsInstance(test_object, FileStorage)
        self.assertEqual(test_object.path(), 'file.json')
        test_dict = test_object.all()
        self.assertEqual()
        