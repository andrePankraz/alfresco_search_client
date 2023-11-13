# ResultNode


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** | The name must not contain spaces or the following special characters: * \&quot; &lt; &gt; \\ / ? : and |. The character . must not be used at the end of the name.  | 
**node_type** | **str** |  | 
**is_folder** | **bool** |  | 
**is_file** | **bool** |  | 
**is_locked** | **bool** |  | [optional] [default to False]
**modified_at** | **datetime** |  | 
**modified_by_user** | [**UserInfo**](UserInfo.md) |  | 
**created_at** | **datetime** |  | 
**created_by_user** | [**UserInfo**](UserInfo.md) |  | 
**parent_id** | **str** |  | [optional] 
**is_link** | **bool** |  | [optional] 
**content** | [**ContentInfo**](ContentInfo.md) |  | [optional] 
**aspect_names** | **List[str]** |  | [optional] 
**properties** | **object** |  | [optional] 
**allowable_operations** | **List[str]** |  | [optional] 
**path** | [**PathInfo**](PathInfo.md) |  | [optional] 
**is_favorite** | **bool** |  | [optional] 
**search** | [**SearchEntry**](SearchEntry.md) |  | [optional] 
**archived_by_user** | [**UserInfo**](UserInfo.md) |  | [optional] 
**archived_at** | **datetime** |  | [optional] 
**version_label** | **str** |  | [optional] 
**version_comment** | **str** |  | [optional] 

## Example

```python
from alfresco_search_api_client.models.result_node import ResultNode

# TODO update the JSON string below
json = "{}"
# create an instance of ResultNode from a JSON string
result_node_instance = ResultNode.from_json(json)
# print the JSON string representation of the object
print ResultNode.to_json()

# convert the object into a dict
result_node_dict = result_node_instance.to_dict()
# create an instance of ResultNode from a dict
result_node_form_dict = result_node.from_dict(result_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


