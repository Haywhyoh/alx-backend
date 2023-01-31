#!/usr/bin/python3
""" Parameterize a unit test, Mock HTTP calls, Parameterize and patch """
import unittest
from parameterized import parameterized
import utils


class TestAccessNestedMap(unittest.TestCase):
    """ TESTCASE """
    """ to test the function for following inputs """
    @parameterized.expand([
        ({"a": 1}, ("a",)),
        ({"a": {"b": 2}}, ("a",)),
        ({"a": {"b": 2}}, ("a", "b"))
    ])
    def test_access_nested_map(self, nested_map, path, answer):
        """ method to test that the method returns what it is supposed to """
        self.assertEqual(utils.access_nested_map(nested_map, path), answer)
