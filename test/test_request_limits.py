# coding: utf-8

"""
    Alfresco Content Services REST API

    **Search API**  Provides access to the search features of Alfresco Content Services. 

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from alfresco_search_api_client.models.request_limits import RequestLimits

class TestRequestLimits(unittest.TestCase):
    """RequestLimits unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RequestLimits:
        """Test RequestLimits
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RequestLimits`
        """
        model = RequestLimits()
        if include_optional:
            return RequestLimits(
                permission_evaluation_time = 56,
                permission_evaluation_count = 56
            )
        else:
            return RequestLimits(
        )
        """

    def testRequestLimits(self):
        """Test RequestLimits"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
