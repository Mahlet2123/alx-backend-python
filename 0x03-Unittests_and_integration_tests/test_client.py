#!/usr/bin/env python3
""" test_client module """
import unittest
from parameterized import parameterized
from client import GithubOrgClient
from utils import get_json
from unittest.mock import patch, Mock, MagicMock


class TestGithubOrgClient(unittest.TestCase):
    """ test class to test client.GithubOrgClient class """
    @parameterized.expand([
        ('google', {"payload": True}),
        ('abc', {"payload": True})
        ])
    @patch('client.get_json')
    def test_org(
            self,
            org: str,
            data_response: dict,
            mock_get: MagicMock
            ) -> bool:
        """
        This method should test that GithubOrgClient.org
        returns the correct value.
        """
        mock_get.return_value = MagicMock(return_value=data_response)

        org_client = GithubOrgClient(org)
        self.assertEqual(org_client.org(), data_response)
        mock_get.assert_called_once_with(GithubOrgClient.ORG_URL.format(org = org))

    @patch('GithubOrgClient.org')
    def test_public_repos_url(
            self,
            mock_org: Mock
            ) -> bool:
        """
        method to unit-test GithubOrgClient._public_repos_url
        """
        data_response = {"payload": True}
        mock_org.return_value = data_response




if __name__ == '__main__':
    unittest.main()

