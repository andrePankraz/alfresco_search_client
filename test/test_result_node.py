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

from alfresco_search_api_client.models.result_node import ResultNode

class TestResultNode(unittest.TestCase):
    """ResultNode unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResultNode:
        """Test ResultNode
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResultNode`
        """
        model = ResultNode()
        if include_optional:
            return ResultNode(
                id = '',
                name = '?x!u'K}qz^sEC)lJ*=-jQ+'6`%cClu,k'!'su[.',
                node_type = '',
                is_folder = True,
                is_file = True,
                is_locked = True,
                modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                modified_by_user = alfresco_search_api_client.models.user_info.UserInfo(
                    display_name = '', 
                    id = '', ),
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_by_user = alfresco_search_api_client.models.user_info.UserInfo(
                    display_name = '', 
                    id = '', ),
                parent_id = '',
                is_link = True,
                content = alfresco_search_api_client.models.content_info.ContentInfo(
                    mime_type = '', 
                    mime_type_name = '', 
                    size_in_bytes = 56, 
                    encoding = '', 
                    mime_type_group = '', ),
                aspect_names = [
                    ''
                    ],
                properties = alfresco_search_api_client.models.properties.properties(),
                allowable_operations = [
                    ''
                    ],
                path = alfresco_search_api_client.models.path_info.PathInfo(
                    elements = [
                        alfresco_search_api_client.models.path_element.PathElement(
                            id = '', 
                            name = '', )
                        ], 
                    name = '', 
                    is_complete = True, ),
                is_favorite = True,
                search = alfresco_search_api_client.models.search_entry.SearchEntry(
                    score = 1.337, 
                    highlight = [
                        alfresco_search_api_client.models.search_entry_highlight_inner.SearchEntry_highlight_inner(
                            field = '', 
                            snippets = [
                                ''
                                ], )
                        ], ),
                archived_by_user = alfresco_search_api_client.models.user_info.UserInfo(
                    display_name = '', 
                    id = '', ),
                archived_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                version_label = '',
                version_comment = ''
            )
        else:
            return ResultNode(
                id = '',
                name = '?x!u'K}qz^sEC)lJ*=-jQ+'6`%cClu,k'!'su[.',
                node_type = '',
                is_folder = True,
                is_file = True,
                modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                modified_by_user = alfresco_search_api_client.models.user_info.UserInfo(
                    display_name = '', 
                    id = '', ),
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_by_user = alfresco_search_api_client.models.user_info.UserInfo(
                    display_name = '', 
                    id = '', ),
        )
        """

    def testResultNode(self):
        """Test ResultNode"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
