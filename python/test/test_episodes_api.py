# coding: utf-8

"""
    Father Ted API

    REST API for hand-curated Father Ted Quotes  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: dave@paddez.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import father_ted_api
from father_ted_api.api.episodes_api import EpisodesApi  # noqa: E501
from father_ted_api.rest import ApiException


class TestEpisodesApi(unittest.TestCase):
    """EpisodesApi unit test stubs"""

    def setUp(self):
        self.api = father_ted_api.api.episodes_api.EpisodesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_episodes_get(self):
        """Test case for episodes_get

        List available episodes.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()