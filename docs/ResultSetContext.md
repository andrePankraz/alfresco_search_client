# ResultSetContext

Context that applies to the whole result set

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consistency** | [**ResponseConsistency**](ResponseConsistency.md) |  | [optional] 
**request** | [**SearchRequest**](SearchRequest.md) |  | [optional] 
**facet_queries** | [**List[ResultSetContextFacetQueriesInner]**](ResultSetContextFacetQueriesInner.md) | The counts from facet queries | [optional] 
**facets_fields** | [**List[ResultBuckets]**](ResultBuckets.md) | The counts from field facets | [optional] 
**facets** | [**List[GenericFacetResponse]**](GenericFacetResponse.md) | The faceted response | [optional] 
**spellcheck** | [**List[ResultSetContextSpellcheckInner]**](ResultSetContextSpellcheckInner.md) | Suggested corrections  If zero results were found for the original query then a single entry of type \&quot;searchInsteadFor\&quot; will be returned. If alternatives were found that return more results than the original query they are returned as \&quot;didYouMean\&quot; options. The highest quality suggestion is first.  | [optional] 

## Example

```python
from alfresco_search_api_client.models.result_set_context import ResultSetContext

# TODO update the JSON string below
json = "{}"
# create an instance of ResultSetContext from a JSON string
result_set_context_instance = ResultSetContext.from_json(json)
# print the JSON string representation of the object
print ResultSetContext.to_json()

# convert the object into a dict
result_set_context_dict = result_set_context_instance.to_dict()
# create an instance of ResultSetContext from a dict
result_set_context_form_dict = result_set_context.from_dict(result_set_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


