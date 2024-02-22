#!/usr/bin/python3
""" Unittest for the console """
import unittest
from models import storage
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import os


class ConsoleTestCase(unittest.TestCase):
    """Console test case"""

    def setUp(self):
        """desc here"""
        """ Set up test environment """
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_normal_format(self):
        """Normal test"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
        obj = storage.all()
        self.assertFalse(len(obj) == 0)

    def test_good_format(self):
        """ """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State name=\"California\"")
        obj = storage.all()
        for key, value in obj.items():
            valuedic = value.to_dict()
            isPresent_att = 'name' in valuedic
            self.assertTrue(isPresent_att)
            self.assertTrue(type(valuedic['name'] is str))
            self.assertTrue(valuedic['name'] == "California")

    def test_good_format_many_param(self):
        """ """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("""create Place city_id="0001"
                    user_id="0001" name="My_little_house"
                    number_rooms=4 number_bathrooms=2
                    max_guest=10 price_by_night=300
                    latitude=37.773972 longitude=-122.431297""")
            obj = storage.all()
        for key, value in obj.items():
            valuedic = value.to_dict()
            isPresent_att = 'city_id' in valuedic
            self.assertTrue(isPresent_att)
            self.assertTrue(type(valuedic['city_id'] is str))
            self.assertTrue(valuedic['city_id'] == "0001")

            isPresent_att = 'user_id' in valuedic
            self.assertTrue(isPresent_att)
            self.assertTrue(valuedic['user_id'] == "0001")
            self.assertTrue(type(valuedic['user_id'] is str))

            isPresent_att = 'name' in valuedic
            self.assertTrue(isPresent_att)
            self.assertTrue(valuedic['name'] == "My little house")
            self.assertTrue(type(valuedic['name'] is str))

            isPresent_att = 'number_rooms' in valuedic
            self.assertTrue(isPresent_att)
            self.assertTrue(type(valuedic['number_rooms'] is int))
            self.assertTrue(valuedic['number_rooms'] == 4)

            self.assertTrue('latitude' in valuedic)
            self.assertTrue(type(valuedic['latitude'] is float))
            self.assertTrue(valuedic['latitude'] == 37.773972)

            self.assertTrue(valuedic['longitude'] == -122.431297)

    def test_bad_format_param(self):
        """Comment here"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place city_id")
        obj = storage.all()
        for key, value in obj.items():
            valuedic = value.to_dict()
            isPresent_att = 'city_id' in valuedic
            self.assertFalse(isPresent_att)

    def test_bad_format_many(self):
        """Comment here"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place city_id=\"0001\"\
                    user_id = \"001\"")
        obj = storage.all()
        for key, value in obj.items():
            valuedic = value.to_dict()
            self.assertTrue('city_id' in valuedic)
            self.assertFalse('user_id' in valuedic)
            self.assertFalse('=' in valuedic)
            self.assertFalse('001' in valuedic)

    def test_no_good_param(self):
        """All param are bad"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("""create State name = "StateName""")
        self.assertFalse(os.path.exists('file.json'))


if __name__ == "__main__":
    unittest.main()
