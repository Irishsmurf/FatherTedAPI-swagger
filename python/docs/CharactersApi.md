# father_ted_api.CharactersApi

All URIs are relative to *https://api.fatherted.irish*

Method | HTTP request | Description
------------- | ------------- | -------------
[**characters_get**](CharactersApi.md#characters_get) | **GET** /characters | List available characters.


# **characters_get**
> list[str] characters_get()

List available characters.

### Example
```python
from __future__ import print_function
import time
import father_ted_api
from father_ted_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = father_ted_api.CharactersApi()

try:
    # List available characters.
    api_response = api_instance.characters_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CharactersApi->characters_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

