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


class TestGetJson(unittest.TestCase):
    """
    Get json test class
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("requests.get")
    def test_get_json(self, input, expected, mock_get_json):
        """
        function for testing get_json function
        """
        mock_response = Mock()
        mock_response.json.return_value = expected
        mock_get_json.return_value = mock_response
        result = get_json(input)
        mock_get_json.assert_called_with(input)
        self.assertEqual(result, expected)


class TestMemoize(unittest.TestCase):
    """
    Class for testing memoize function
    """
    def test_memoize(self) -> None:
        """ test memoize """
        class TestClass:
            """
            look-up for def
            """

            def a_method(self):
                """
                returns 42
                """
                return 42

            @memoize
            def a_property(self):
                """
                Property
                """
                return self.a_method()

        with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,
        ) as memo:
            test_instance = TestClass()
            result1 = test_instance.a_property()
            result2 = test_instance.a_property()
            memo.assert_called_once()
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)


if __name__ == "__main__":
    unittest.main()
