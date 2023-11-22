#!/usr/bin/python3
"""
test_models/base_model.py of testing BaseModel class.
"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
import pycodestyle
import os
import uuid
from datetime import datetime



class TestAmenity(unittest.TestCase):
    """ Tests for Amenity class """
    @classmethod
    def setUpClass(cls):
        """ Setting up class instance """
        cls.a1 = Amenity()
        cls.a1.name = "Amenity1"

        cls.a2 = Amenity()
        cls.a2.name = "Amenity2"
        cls.d = cls.a2.to_dict()
        cls.a3 = Amenity(**cls.d)

    @classmethod
    def tearDownClass(cls):
        """ Tears down created instances """
        del cls.a1
        del cls.a2
        del cls.a3
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance(self):
        """ Testing for instances """
        self.assertIsInstance(self.a1, Amenity, "Not instance of Amenity")
        self.assertIsInstance(self.a2, Amenity, "Not instance of Amenity")
        self.assertIsInstance(self.a3, Amenity, "Not instance of Amenity")

    def test_subClass(self):
        """ Testing for a subclass """
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_save(self):
        """ Testing save updated_time """
        self.a1.save()
        self.assertNotEqual(self.a1.updated_at, self.a1.created_at)

