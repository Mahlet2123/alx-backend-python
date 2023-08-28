#!/usr/bin/env python3
""" test_client module """
import unittest
from parameterized import parameterized
from client import GithubOrgClient
from utils import get_json
from unittest.mock import patch, Mock, PropertyMock


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
            mock_get: Mock
            ) -> bool:
        """
        This method should test that GithubOrgClient.org
        returns the correct value.
        """
        mock_get.return_value = Mock(return_value=data_response)

        org_client = GithubOrgClient(org)
        self.assertEqual(org_client.org(), data_response)
        mock_get.assert_called_once_with(GithubOrgClient.ORG_URL.format(org = org))

    @parameterized.expand([
        ('google', {'repos_url': "https://api.github.com/users/google/repos"}),
        ('abc', {'repos_url': "https://api.github.com/users/abc/repos"})
        ])
    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(
            self,
            org,
            data_response: dict,
            mock_org: Mock
            ) -> bool:
        """
        method to unit-test GithubOrgClient._public_repos_url
        """
        mock_org.return_value = data_response
        org_client = GithubOrgClient(org)
        self.assertEqual(org_client._public_repos_url, data_response['repos_url'])


if __name__ == '__main__':
    unittest.main()

