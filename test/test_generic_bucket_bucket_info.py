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

from alfresco_search_api_client.models.generic_bucket_bucket_info import GenericBucketBucketInfo

class TestGenericBucketBucketInfo(unittest.TestCase):
    """GenericBucketBucketInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GenericBucketBucketInfo:
        """Test GenericBucketBucketInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GenericBucketBucketInfo`
        """
        model = GenericBucketBucketInfo()
        if include_optional:
            return GenericBucketBucketInfo(
                start = '',
                start_inclusive = True,
                end = '',
                end_inclusive = True
            )
        else:
            return GenericBucketBucketInfo(
        )
        """

    def testGenericBucketBucketInfo(self):
        """Test GenericBucketBucketInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
