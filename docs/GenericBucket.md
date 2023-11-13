# GenericBucket

A bucket of facet results

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The bucket label | [optional] 
**filter_query** | **str** | The filter query you can use to apply this facet | [optional] 
**display** | **object** | An optional field for additional display information | [optional] 
**metrics** | [**List[GenericMetric]**](GenericMetric.md) | An array of buckets and values | [optional] 
**facets** | **List[object]** | Additional list of nested facets | [optional] 
**bucket_info** | [**GenericBucketBucketInfo**](GenericBucketBucketInfo.md) |  | [optional] 

## Example

```python
from alfresco_search_api_client.models.generic_bucket import GenericBucket

# TODO update the JSON string below
json = "{}"
# create an instance of GenericBucket from a JSON string
generic_bucket_instance = GenericBucket.from_json(json)
# print the JSON string representation of the object
print GenericBucket.to_json()

# convert the object into a dict
generic_bucket_dict = generic_bucket_instance.to_dict()
# create an instance of GenericBucket from a dict
generic_bucket_form_dict = generic_bucket.from_dict(generic_bucket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


