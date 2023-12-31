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

from alfresco_search_api_client.models.request_highlight_fields_inner import RequestHighlightFieldsInner

class TestRequestHighlightFieldsInner(unittest.TestCase):
    """RequestHighlightFieldsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RequestHighlightFieldsInner:
        """Test RequestHighlightFieldsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RequestHighlightFieldsInner`
        """
        model = RequestHighlightFieldsInner()
        if include_optional:
            return RequestHighlightFieldsInner(
                field = '',
                snippet_count = 56,
                fragment_size = 56,
                merge_contiguous = True,
                prefix = '',
                postfix = ''
            )
        else:
            return RequestHighlightFieldsInner(
        )
        """

    def testRequestHighlightFieldsInner(self):
        """Test RequestHighlightFieldsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
