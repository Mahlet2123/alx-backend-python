#!/usr/bin/env python3
""" test_utils module """
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Mapping, Sequence


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


if __name__ == '__main__':
    unittest.main()
