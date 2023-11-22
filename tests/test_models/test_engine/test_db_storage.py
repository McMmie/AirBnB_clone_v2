#!/usr/bin/python3
"""
testing the storage to database
"""
import time
import unittest
import sys
from io import StringIO
from os import getenv
from console import HBNBCommand
from models.engine.db_storage import DBStorage
from models import storage
from models.user import User
from models.state import State

db = getenv("HBNB_TYPE_STORAGE")


@unittest.skipIf(db != 'db', "testing mysql database only")
class test_DBStorage(unittest.TestCase):
    """
    database class for testing
    """
    @classmethod
    def setUpClass(cls):
        """creates a set for the database"""
        cls.dbstorage = DBStorage()
        cls.output = StringIO()
        sys.stdout = cls.output

    @classmethod
    def tearDownClass(cls):
        """
        remove variables set by the set up method
        """
        del cls.dbstorage
        del cls.output

    def create(self):
        """ """
        return HBNBCommand()

    def test_dbstorage_all(self):
        """
        """
        storage.reload()
        res = storage.all()
        self.assertIsInstance(res, dict)
        self.assertEqual(len(res), 0)
        new_user = User(email="fake@email.com", password="xyz")
        cons = self.create
        cons.onecmd("create State name=Arizona")
        res = storage.all("State")
        self.assertTrue(len(res) > 0)

    def test_model_storage(self):
        """
        this method checks the type of storage
        """
        self.assertTrue(isinstance(storage, DBStorage))
