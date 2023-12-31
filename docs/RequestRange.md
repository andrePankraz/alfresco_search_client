# RequestRange

Facet range

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **str** | The name of the field to perform range | [optional] 
**start** | **str** | The start of the range | [optional] 
**end** | **str** | The end of the range | [optional] 
**gap** | **str** | Bucket size | [optional] 
**hardend** | **bool** | If true means that the last bucket will end at “end” even if it is less than “gap” wide. | [optional] 
**other** | **List[str]** | before, after, between, non, all | [optional] 
**include** | **List[str]** | lower, upper, edge, outer, all | [optional] 
**label** | **str** | A label to include as a pivot reference | [optional] 
**exclude_filters** | **List[str]** | Filter queries to exclude when calculating statistics | [optional] 

## Example

```python
from alfresco_search_api_client.models.request_range import RequestRange

# TODO update the JSON string below
json = "{}"
# create an instance of RequestRange from a JSON string
request_range_instance = RequestRange.from_json(json)
# print the JSON string representation of the object
print RequestRange.to_json()

# convert the object into a dict
request_range_dict = request_range_instance.to_dict()
# create an instance of RequestRange from a dict
request_range_form_dict = request_range.from_dict(request_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


