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
        mock_get.assert_called_once_with(
                GithubOrgClient.ORG_URL.format(org=org)
                )

    def test_public_repos_url(self) -> bool:
        """
        method to unit-test GithubOrgClient._public_repos_url
        """
        with patch(
                'client.GithubOrgClient.org',
                new_callable=PropertyMock
                ) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/users/abc/repos",
            }
            org_client = GithubOrgClient('abc')
            self.assertEqual(
                org_client._public_repos_url,
                "https://api.github.com/users/abc/repos"
                )

    @patch('client.get_json')
    def test_public_repos(
            self,
            mock_get: Mock
            ) -> bool:
        """
        To unit-test GithubOrgClient.public_repos
        """
        test_payload = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {
                    "id": 7697149,
                    "name": "episodes.dart",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/episodes.dart",
                    "created_at": "2013-01-19T00:31:37Z",
                    "updated_at": "2019-09-23T11:53:58Z",
                    "has_issues": True,
                    "forks": 22,
                    "default_branch": "master",
                },
                {
                    "id": 8566972,
                    "name": "kratu",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/kratu",
                    "created_at": "2013-03-04T22:52:33Z",
                    "updated_at": "2019-11-15T22:22:16Z",
                    "has_issues": True,
                    "forks": 32,
                    "default_branch": "master",
                },
            ]

        }
        mock_get.return_value = test_payload["repos"]
        with patch(
                'client.GithubOrgClient._public_repos_url',
                new_callable=PropertyMock,
                ) as mock_public_repos:
            mock_public_repos.return_value = test_payload["repos_url"]
            self.assertEqual(
                GithubOrgClient("google").public_repos(),
                [
                    "episodes.dart",
                    "kratu",
                ],
            )
            mock_public_repos.assert_called_once()
        mock_get.assert_called_once()


if __name__ == '__main__':
    unittest.main()
