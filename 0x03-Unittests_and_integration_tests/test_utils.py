#!/usr/bin/env python3
""" test_utils module """
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from typing import Mapping, Sequence
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """ unit test for utils.access_nested_map """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self,
            nested_map: Mapping,
            path: Sequence, output: any
            ) -> bool:
        """
        method to test that the method returns what
        it is supposed to.
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, output)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Mapping,
            path: Sequence
            ) -> bool:
        """
        test that a KeyError is raised for the
        following inputs
        """
        with self.assertRaises(KeyError):
            result = access_nested_map(nested_map, path)

class TestGetJson(unittest.TestCase):
    """ test that utils.get_json """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(
            self,
            url: str,
            data_response: dict,
            mock_get: Mock
            ) -> bool:
        """
        method to test that utils.get_json returns the
        expected result.
        """
        mock_json = Mock()
        mock_json.json.return_value = data_response
        mock_get.return_value = mock_json

        result = get_json(url)
        self.assertEqual(result, data_response)


if __name__ == '__main__':
    unittest.main()
