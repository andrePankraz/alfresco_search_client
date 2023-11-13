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

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
from alfresco_search_api_client.models.content_info import ContentInfo
from alfresco_search_api_client.models.path_info import PathInfo
from alfresco_search_api_client.models.user_info import UserInfo

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class Node(BaseModel):
    """
    Node
    """  # noqa: E501

    id: StrictStr
    name: Annotated[str, Field(strict=True)] = Field(
        description='The name must not contain spaces or the following special characters: * " < > \\ / ? : and |. The character . must not be used at the end of the name. '
    )
    node_type: StrictStr = Field(alias="nodeType")
    is_folder: StrictBool = Field(alias="isFolder")
    is_file: StrictBool = Field(alias="isFile")
    is_locked: Optional[StrictBool] = Field(default=False, alias="isLocked")
    modified_at: datetime = Field(alias="modifiedAt")
    modified_by_user: UserInfo = Field(alias="modifiedByUser")
    created_at: datetime = Field(alias="createdAt")
    created_by_user: UserInfo = Field(alias="createdByUser")
    parent_id: Optional[StrictStr] = Field(default=None, alias="parentId")
    is_link: Optional[StrictBool] = Field(default=None, alias="isLink")
    content: Optional[ContentInfo] = None
    aspect_names: Optional[List[StrictStr]] = Field(default=None, alias="aspectNames")
    properties: Optional[Union[str, Any]] = None
    allowable_operations: Optional[List[StrictStr]] = Field(
        default=None, alias="allowableOperations"
    )
    path: Optional[PathInfo] = None
    is_favorite: Optional[StrictBool] = Field(default=None, alias="isFavorite")
    __properties: ClassVar[List[str]] = [
        "id",
        "name",
        "nodeType",
        "isFolder",
        "isFile",
        "isLocked",
        "modifiedAt",
        "modifiedByUser",
        "createdAt",
        "createdByUser",
        "parentId",
        "isLink",
        "content",
        "aspectNames",
        "properties",
        "allowableOperations",
        "path",
        "isFavorite",
    ]

    @field_validator("name")
    def name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(
            r'^(?!(.*[\\"\*\\\>\<\?\/\:\|]+.*)|(.*[\.]?.*[\.]+$)|(.*[ ]+$))', value
        ):
            raise ValueError(
                r'must validate the regular expression /^(?!(.*[\\"\*\\\>\<\?\/\:\|]+.*)|(.*[\.]?.*[\.]+$)|(.*[ ]+$))/'
            )
        return value

    model_config = {"populate_by_name": True, "validate_assignment": True}

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Node from a JSON string"""
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
            exclude={},
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of modified_by_user
        if self.modified_by_user:
            _dict["modifiedByUser"] = self.modified_by_user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created_by_user
        if self.created_by_user:
            _dict["createdByUser"] = self.created_by_user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of content
        if self.content:
            _dict["content"] = self.content.to_dict()
        # override the default output from pydantic by calling `to_dict()` of path
        if self.path:
            _dict["path"] = self.path.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Node from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "name": obj.get("name"),
                "nodeType": obj.get("nodeType"),
                "isFolder": obj.get("isFolder"),
                "isFile": obj.get("isFile"),
                "isLocked": obj.get("isLocked")
                if obj.get("isLocked") is not None
                else False,
                "modifiedAt": obj.get("modifiedAt"),
                "modifiedByUser": UserInfo.from_dict(obj.get("modifiedByUser"))
                if obj.get("modifiedByUser") is not None
                else None,
                "createdAt": obj.get("createdAt"),
                "createdByUser": UserInfo.from_dict(obj.get("createdByUser"))
                if obj.get("createdByUser") is not None
                else None,
                "parentId": obj.get("parentId"),
                "isLink": obj.get("isLink"),
                "content": ContentInfo.from_dict(obj.get("content"))
                if obj.get("content") is not None
                else None,
                "aspectNames": obj.get("aspectNames"),
                "properties": obj.get("properties"),
                "allowableOperations": obj.get("allowableOperations"),
                "path": PathInfo.from_dict(obj.get("path"))
                if obj.get("path") is not None
                else None,
                "isFavorite": obj.get("isFavorite"),
            }
        )
        return _obj
