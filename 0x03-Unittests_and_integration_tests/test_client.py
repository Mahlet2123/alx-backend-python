#!/usr/bin/env python3
""" test_client module """
import unittest
from parameterized import parameterized
from client import GithubOrgClient
from utils import get_json
from unittest.mock import patch, Mock


class TestGithubOrgClient(unittest.TestCase):
    """ test class to test client.GithubOrgClient class """
    @parameterized.expand([
        ('google', {"payload": True}),
        ('abc', {"payload": True})
        ])
    @patch('requests.get')
    def test_org(
            self,
            org: str,
            data_response: dict,
            mock_get: Mock
            ) -> bool:
        """
        This method should test that GithubOrgClient.org
        returns the correct value.
        """
        mock_json = Mock()
        mock_json.json.return_value = data_response
        mock_get.return_value = mock_json

        result = get_json(GithubOrgClient.ORG_URL.format(org = org))
        self.assertEqual(result, data_response)
