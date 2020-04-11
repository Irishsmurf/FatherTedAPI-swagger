# father_ted_api.EpisodesApi

All URIs are relative to *https://api.fatherted.irish*

Method | HTTP request | Description
------------- | ------------- | -------------
[**episodes_get**](EpisodesApi.md#episodes_get) | **GET** /episodes | List available episodes.


# **episodes_get**
> list[str] episodes_get()

List available episodes.

### Example
```python
from __future__ import print_function
import time
import father_ted_api
from father_ted_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = father_ted_api.EpisodesApi()

try:
    # List available episodes.
    api_response = api_instance.episodes_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EpisodesApi->episodes_get: %s\n" % e)
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

