#!/usr/bin/python3
""" test module for base model """
import unittest
import time
import io
import sys
import datetime
from models.city import City


class Test_City(unittest.TestCase):
    """ checks certain aspects of City Class"""
    def test_equal(self):
        """ checks the sucess cases of City """
        test_object = City()
        self.assertIsInstance(test_object, City)
        time.sleep(1)
        test_object.name = "My_First_Model"
        test_object2 = City(**test_object.to_dict())
        self.assertEqual(test_object.id, test_object.to_dict()["id"])
        self.assertEqual(test_object2.id, test_object2.to_dict()["id"])
        self.assertIsNot(test_object, test_object2)
        self.assertEqual(test_object2.id, test_object.id)
        self.assertIn("name", test_object.to_dict().keys())
        self.assertEqual(test_object.name, test_object.to_dict()["name"])
        self.assertNotEqual(test_object.created_at, test_object.updated_at)

    def test_instance(self):
        """ tests the instance of the various attributes """
        test_object = City()
        test_object2 = City(**test_object.to_dict())
        self.assertIsInstance(test_object, City)
        self.assertIsInstance(test_object.id, str)
        self.assertIsInstance(test_object.to_dict()["created_at"], str)
        self.assertIsInstance(test_object.to_dict()["updated_at"], str)
        self.assertIsInstance(test_object2.created_at, datetime.datetime)
        self.assertIsInstance(test_object2.updated_at, datetime.datetime)
        self.assertIsInstance(test_object2.to_dict()["created_at"], str)
        self.assertIsInstance(test_object2.to_dict()["updated_at"], str)
        self.assertIsInstance(test_object2.created_at, datetime.datetime)
        self.assertIsInstance(test_object2.updated_at, datetime.datetime)

    def test_print(self):
        """ tests functions that dont return but print """
        test_object = City()
        test_object2 = City(**test_object.to_dict())
        test_object_print = io.StringIO()
        sys.stdout = test_object_print
        print(test_object)
        sys.stdout = sys.__stdout__
        test_str = f"[City] ({test_object.id}) {test_object.__dict__}"
        self.maxDiff = None
        test_object_print.truncate(len(test_str))
        self.assertEqual(test_object_print.getvalue(), test_str)
