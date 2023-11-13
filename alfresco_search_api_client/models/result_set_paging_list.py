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
from pydantic import BaseModel
from alfresco_search_api_client.models.pagination import Pagination
from alfresco_search_api_client.models.result_set_context import ResultSetContext
from alfresco_search_api_client.models.result_set_row_entry import ResultSetRowEntry
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ResultSetPagingList(BaseModel):
    """
    ResultSetPagingList
    """ # noqa: E501
    pagination: Optional[Pagination] = None
    context: Optional[ResultSetContext] = None
    entries: Optional[List[ResultSetRowEntry]] = None
    __properties: ClassVar[List[str]] = ["pagination", "context", "entries"]

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
        """Create an instance of ResultSetPagingList from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of pagination
        if self.pagination:
            _dict['pagination'] = self.pagination.to_dict()
        # override the default output from pydantic by calling `to_dict()` of context
        if self.context:
            _dict['context'] = self.context.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in entries (list)
        _items = []
        if self.entries:
            for _item in self.entries:
                if _item:
                    _items.append(_item.to_dict())
            _dict['entries'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ResultSetPagingList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pagination": Pagination.from_dict(obj.get("pagination")) if obj.get("pagination") is not None else None,
            "context": ResultSetContext.from_dict(obj.get("context")) if obj.get("context") is not None else None,
            "entries": [ResultSetRowEntry.from_dict(_item) for _item in obj.get("entries")] if obj.get("entries") is not None else None
        })
        return _obj


