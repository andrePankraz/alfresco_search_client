# ResultSetPagingList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**context** | [**ResultSetContext**](ResultSetContext.md) |  | [optional] 
**entries** | [**List[ResultSetRowEntry]**](ResultSetRowEntry.md) |  | [optional] 

## Example

```python
from alfresco_search_api_client.models.result_set_paging_list import ResultSetPagingList

# TODO update the JSON string below
json = "{}"
# create an instance of ResultSetPagingList from a JSON string
result_set_paging_list_instance = ResultSetPagingList.from_json(json)
# print the JSON string representation of the object
print ResultSetPagingList.to_json()

# convert the object into a dict
result_set_paging_list_dict = result_set_paging_list_instance.to_dict()
# create an instance of ResultSetPagingList from a dict
result_set_paging_list_form_dict = result_set_paging_list.from_dict(result_set_paging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


