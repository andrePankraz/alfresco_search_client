# ResultBucketsBucketsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The bucket label | [optional] 
**filter_query** | **str** | The filter query you can use to apply this facet | [optional] 
**count** | **int** | The count for the bucket | [optional] 
**display** | **object** | An optional field for additional display information | [optional] 

## Example

```python
from alfresco_search_api_client.models.result_buckets_buckets_inner import ResultBucketsBucketsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ResultBucketsBucketsInner from a JSON string
result_buckets_buckets_inner_instance = ResultBucketsBucketsInner.from_json(json)
# print the JSON string representation of the object
print ResultBucketsBucketsInner.to_json()

# convert the object into a dict
result_buckets_buckets_inner_dict = result_buckets_buckets_inner_instance.to_dict()
# create an instance of ResultBucketsBucketsInner from a dict
result_buckets_buckets_inner_form_dict = result_buckets_buckets_inner.from_dict(result_buckets_buckets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


