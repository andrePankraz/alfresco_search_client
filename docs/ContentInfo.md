# ContentInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mime_type** | **str** |  | 
**mime_type_name** | **str** |  | 
**size_in_bytes** | **int** |  | 
**encoding** | **str** |  | [optional] 
**mime_type_group** | **str** |  | [optional] 

## Example

```python
from alfresco_search_api_client.models.content_info import ContentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ContentInfo from a JSON string
content_info_instance = ContentInfo.from_json(json)
# print the JSON string representation of the object
print ContentInfo.to_json()

# convert the object into a dict
content_info_dict = content_info_instance.to_dict()
# create an instance of ContentInfo from a dict
content_info_form_dict = content_info.from_dict(content_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


