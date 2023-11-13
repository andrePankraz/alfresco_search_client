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

from alfresco_search_api_client.models.generic_metric import GenericMetric

class TestGenericMetric(unittest.TestCase):
    """GenericMetric unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GenericMetric:
        """Test GenericMetric
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GenericMetric`
        """
        model = GenericMetric()
        if include_optional:
            return GenericMetric(
                type = '',
                value = alfresco_search_api_client.models.value.value()
            )
        else:
            return GenericMetric(
        )
        """

    def testGenericMetric(self):
        """Test GenericMetric"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()