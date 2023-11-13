# coding: utf-8

"""
    Alfresco Content Services REST API

    **Search API**  Provides access to the search features of Alfresco Content Services. 

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from pydantic import Field
from alfresco_search_api_client.models.request_highlight_fields_inner import RequestHighlightFieldsInner
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class RequestHighlight(BaseModel):
    """
    Request that highlight fragments to be added to result set rows The properties reflect SOLR highlighting parameters. 
    """ # noqa: E501
    prefix: Optional[StrictStr] = Field(default=None, description="The string used to mark the start of a highlight in a fragment.")
    postfix: Optional[StrictStr] = Field(default=None, description="The string used to mark the end of a highlight in a fragment.")
    snippet_count: Optional[StrictInt] = Field(default=None, description="The maximum number of distinct highlight snippets to return for each highlight field.", alias="snippetCount")
    fragment_size: Optional[StrictInt] = Field(default=None, description="The character length of each snippet.", alias="fragmentSize")
    max_analyzed_chars: Optional[StrictInt] = Field(default=None, description="The number of characters to be considered for highlighting. Matches after this count will not be shown.", alias="maxAnalyzedChars")
    merge_contiguous: Optional[StrictBool] = Field(default=None, description="If fragments over lap they can be  merged into one larger fragment", alias="mergeContiguous")
    use_phrase_highlighter: Optional[StrictBool] = Field(default=None, description="Should phrases be identified.", alias="usePhraseHighlighter")
    fields: Optional[List[RequestHighlightFieldsInner]] = Field(default=None, description="The fields to highlight and field specific configuration properties for each field")
    __properties: ClassVar[List[str]] = ["prefix", "postfix", "snippetCount", "fragmentSize", "maxAnalyzedChars", "mergeContiguous", "usePhraseHighlighter", "fields"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of RequestHighlight from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in fields (list)
        _items = []
        if self.fields:
            for _item in self.fields:
                if _item:
                    _items.append(_item.to_dict())
            _dict['fields'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of RequestHighlight from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "prefix": obj.get("prefix"),
            "postfix": obj.get("postfix"),
            "snippetCount": obj.get("snippetCount"),
            "fragmentSize": obj.get("fragmentSize"),
            "maxAnalyzedChars": obj.get("maxAnalyzedChars"),
            "mergeContiguous": obj.get("mergeContiguous"),
            "usePhraseHighlighter": obj.get("usePhraseHighlighter"),
            "fields": [RequestHighlightFieldsInner.from_dict(_item) for _item in obj.get("fields")] if obj.get("fields") is not None else None
        })
        return _obj

