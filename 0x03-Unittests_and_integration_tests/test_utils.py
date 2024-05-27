#!/usr/bin/env python3
"""
testing utils function
"""
from parameterized import parameterized
import unittest
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """
    class for testing access_nested_map function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])

    def test_access_nested_map(self, nestedMap, path, expected):
        """
        accessing nested map test case
        """
        self.assertEqual(access_nested_map(nestedMap, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
        ])
    def test_access_nested_map_exception(self, nestedMap, path, expected):
        """
        accessing exeption testcase
        """
        self.assertRaises(expected, access_nested_map, nestedMap, path)
