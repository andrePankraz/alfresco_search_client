# SearchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | [**RequestQuery**](RequestQuery.md) |  | 
**paging** | [**RequestPagination**](RequestPagination.md) |  | [optional] 
**include** | **List[str]** | Returns additional information about the node. The following optional fields can be requested:  * properties  * aspectNames  * path  * isLink  * allowableOperations  * association  * isFavorite  | [optional] 
**include_request** | **bool** | When true, include the original request in the response | [optional] [default to False]
**fields** | **List[str]** | A list of field names. You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth. The list applies to a returned individual entity or entries within a collection. If the **include** parameter is used aswell then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter. | [optional] 
**sort** | [**List[RequestSortDefinitionInner]**](RequestSortDefinitionInner.md) | How to sort the rows? An array of sort specifications. The array order defines the ordering precedence. | [optional] 
**templates** | [**List[RequestTemplatesInner]**](RequestTemplatesInner.md) | Templates usewd for query expansion. A template called \&quot;WOOF\&quot; defined as \&quot;%(cm:name cm:title)\&quot; allows WOOF:example to generate cm:name:example cm:name:example  | [optional] 
**defaults** | [**RequestDefaults**](RequestDefaults.md) |  | [optional] 
**localization** | [**RequestLocalization**](RequestLocalization.md) |  | [optional] 
**filter_queries** | [**List[RequestFilterQueriesInner]**](RequestFilterQueriesInner.md) | Filter Queries. Constraints that apply to the results set but do not affect the score of each entry. | [optional] 
**facet_queries** | [**List[RequestFacetQueriesInner]**](RequestFacetQueriesInner.md) | Facet queries to include | [optional] 
**facet_fields** | [**RequestFacetFields**](RequestFacetFields.md) |  | [optional] 
**facet_intervals** | [**RequestFacetIntervals**](RequestFacetIntervals.md) |  | [optional] 
**pivots** | [**List[RequestPivot]**](RequestPivot.md) |  | [optional] 
**stats** | [**List[RequestStats]**](RequestStats.md) |  | [optional] 
**spellcheck** | [**RequestSpellcheck**](RequestSpellcheck.md) |  | [optional] 
**scope** | [**RequestScope**](RequestScope.md) |  | [optional] 
**limits** | [**RequestLimits**](RequestLimits.md) |  | [optional] 
**highlight** | [**RequestHighlight**](RequestHighlight.md) |  | [optional] 
**ranges** | [**List[RequestRange]**](RequestRange.md) |  | [optional] 

## Example

```python
from alfresco_search_api_client.models.search_request import SearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SearchRequest from a JSON string
search_request_instance = SearchRequest.from_json(json)
# print the JSON string representation of the object
print SearchRequest.to_json()

# convert the object into a dict
search_request_dict = search_request_instance.to_dict()
# create an instance of SearchRequest from a dict
search_request_form_dict = search_request.from_dict(search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


