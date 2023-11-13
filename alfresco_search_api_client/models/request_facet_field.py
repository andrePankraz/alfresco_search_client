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
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr, field_validator
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class RequestFacetField(BaseModel):
    """
    A simple facet field
    """ # noqa: E501
    field: Optional[StrictStr] = Field(default=None, description="The facet field")
    label: Optional[StrictStr] = Field(default=None, description="A label to include in place of the facet field")
    prefix: Optional[StrictStr] = Field(default=None, description="Restricts the possible constraints to only indexed values with a specified prefix.")
    sort: Optional[StrictStr] = None
    method: Optional[StrictStr] = None
    missing: Optional[StrictBool] = Field(default=False, description="When true, count results that match the query but which have no facet value for the field (in addition to the Term-based constraints).")
    limit: Optional[StrictInt] = None
    offset: Optional[StrictInt] = None
    mincount: Optional[StrictInt] = Field(default=None, description="The minimum count required for a facet field to be included in the response.")
    facet_enum_cache_min_df: Optional[StrictInt] = Field(default=None, alias="facetEnumCacheMinDf")
    exclude_filters: Optional[List[StrictStr]] = Field(default=None, description="Filter Queries with tags listed here will not be included in facet counts. This is used for multi-select facetting. ", alias="excludeFilters")
    __properties: ClassVar[List[str]] = ["field", "label", "prefix", "sort", "method", "missing", "limit", "offset", "mincount", "facetEnumCacheMinDf", "excludeFilters"]

    @field_validator('sort')
    def sort_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('COUNT', 'INDEX'):
            raise ValueError("must be one of enum values ('COUNT', 'INDEX')")
        return value

    @field_validator('method')
    def method_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ENUM', 'FC'):
            raise ValueError("must be one of enum values ('ENUM', 'FC')")
        return value

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
        """Create an instance of RequestFacetField from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of RequestFacetField from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "field": obj.get("field"),
            "label": obj.get("label"),
            "prefix": obj.get("prefix"),
            "sort": obj.get("sort"),
            "method": obj.get("method"),
            "missing": obj.get("missing") if obj.get("missing") is not None else False,
            "limit": obj.get("limit"),
            "offset": obj.get("offset"),
            "mincount": obj.get("mincount"),
            "facetEnumCacheMinDf": obj.get("facetEnumCacheMinDf"),
            "excludeFilters": obj.get("excludeFilters")
        })
        return _obj


