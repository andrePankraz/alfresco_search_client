# ResultBuckets


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The field name or its explicit label, if provided on the request | [optional] 
**buckets** | [**List[ResultBucketsBucketsInner]**](ResultBucketsBucketsInner.md) | An array of buckets and values | [optional] 

## Example

```python
from alfresco_search_api_client.models.result_buckets import ResultBuckets

# TODO update the JSON string below
json = "{}"
# create an instance of ResultBuckets from a JSON string
result_buckets_instance = ResultBuckets.from_json(json)
# print the JSON string representation of the object
print ResultBuckets.to_json()

# convert the object into a dict
result_buckets_dict = result_buckets_instance.to_dict()
# create an instance of ResultBuckets from a dict
result_buckets_form_dict = result_buckets.from_dict(result_buckets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


