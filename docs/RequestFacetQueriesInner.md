# RequestFacetQueriesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | A facet query | [optional] 
**label** | **str** | A label to include in place of the facet query | [optional] 

## Example

```python
from alfresco_search_api_client.models.request_facet_queries_inner import RequestFacetQueriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RequestFacetQueriesInner from a JSON string
request_facet_queries_inner_instance = RequestFacetQueriesInner.from_json(json)
# print the JSON string representation of the object
print RequestFacetQueriesInner.to_json()

# convert the object into a dict
request_facet_queries_inner_dict = request_facet_queries_inner_instance.to_dict()
# create an instance of RequestFacetQueriesInner from a dict
request_facet_queries_inner_form_dict = request_facet_queries_inner.from_dict(request_facet_queries_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


