# RequestHighlight

Request that highlight fragments to be added to result set rows The properties reflect SOLR highlighting parameters. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prefix** | **str** | The string used to mark the start of a highlight in a fragment. | [optional] 
**postfix** | **str** | The string used to mark the end of a highlight in a fragment. | [optional] 
**snippet_count** | **int** | The maximum number of distinct highlight snippets to return for each highlight field. | [optional] 
**fragment_size** | **int** | The character length of each snippet. | [optional] 
**max_analyzed_chars** | **int** | The number of characters to be considered for highlighting. Matches after this count will not be shown. | [optional] 
**merge_contiguous** | **bool** | If fragments over lap they can be  merged into one larger fragment | [optional] 
**use_phrase_highlighter** | **bool** | Should phrases be identified. | [optional] 
**fields** | [**List[RequestHighlightFieldsInner]**](RequestHighlightFieldsInner.md) | The fields to highlight and field specific configuration properties for each field | [optional] 

## Example

```python
from alfresco_search_api_client.models.request_highlight import RequestHighlight

# TODO update the JSON string below
json = "{}"
# create an instance of RequestHighlight from a JSON string
request_highlight_instance = RequestHighlight.from_json(json)
# print the JSON string representation of the object
print RequestHighlight.to_json()

# convert the object into a dict
request_highlight_dict = request_highlight_instance.to_dict()
# create an instance of RequestHighlight from a dict
request_highlight_form_dict = request_highlight.from_dict(request_highlight_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


