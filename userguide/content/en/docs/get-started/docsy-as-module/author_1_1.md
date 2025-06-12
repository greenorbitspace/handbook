---
weight: 2
date: '2025-06-12'
title: Author 1 1
aliases:
- /docs/author_1_1/
description: ''
linkTitle: Author 1 1
type: docs
---

# Author


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.author import Author

# TODO update the JSON string below
json = "{}"
# create an instance of Author from a JSON string
author_instance = Author.from_json(json)
# print the JSON string representation of the object
print(Author.to_json())

# convert the object into a dict
author_dict = author_instance.to_dict()
# create an instance of Author from a dict
author_from_dict = Author.from_dict(author_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


