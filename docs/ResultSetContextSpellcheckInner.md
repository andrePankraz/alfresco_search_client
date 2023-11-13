# ResultSetContextSpellcheckInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**suggestion** | **List[str]** | A suggested alternative query | [optional] 

## Example

```python
from alfresco_search_api_client.models.result_set_context_spellcheck_inner import ResultSetContextSpellcheckInner

# TODO update the JSON string below
json = "{}"
# create an instance of ResultSetContextSpellcheckInner from a JSON string
result_set_context_spellcheck_inner_instance = ResultSetContextSpellcheckInner.from_json(json)
# print the JSON string representation of the object
print ResultSetContextSpellcheckInner.to_json()

# convert the object into a dict
result_set_context_spellcheck_inner_dict = result_set_context_spellcheck_inner_instance.to_dict()
# create an instance of ResultSetContextSpellcheckInner from a dict
result_set_context_spellcheck_inner_form_dict = result_set_context_spellcheck_inner.from_dict(result_set_context_spellcheck_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


