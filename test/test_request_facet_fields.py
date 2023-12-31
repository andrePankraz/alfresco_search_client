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

from alfresco_search_api_client.models.request_facet_fields import RequestFacetFields

class TestRequestFacetFields(unittest.TestCase):
    """RequestFacetFields unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RequestFacetFields:
        """Test RequestFacetFields
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RequestFacetFields`
        """
        model = RequestFacetFields()
        if include_optional:
            return RequestFacetFields(
                facets = [
                    alfresco_search_api_client.models.request_facet_field.RequestFacetField(
                        field = '', 
                        label = '', 
                        prefix = '', 
                        sort = 'COUNT', 
                        method = 'ENUM', 
                        missing = True, 
                        limit = 56, 
                        offset = 56, 
                        mincount = 56, 
                        facet_enum_cache_min_df = 56, 
                        exclude_filters = [
                            ''
                            ], )
                    ]
            )
        else:
            return RequestFacetFields(
        )
        """

    def testRequestFacetFields(self):
        """Test RequestFacetFields"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
