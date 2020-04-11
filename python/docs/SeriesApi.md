# father_ted_api.SeriesApi

All URIs are relative to *https://api.fatherted.irish*

Method | HTTP request | Description
------------- | ------------- | -------------
[**series_get**](SeriesApi.md#series_get) | **GET** /series | List available series.


# **series_get**
> list[str] series_get()

List available series.

### Example
```python
from __future__ import print_function
import time
import father_ted_api
from father_ted_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = father_ted_api.SeriesApi()

try:
    # List available series.
    api_response = api_instance.series_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SeriesApi->series_get: %s\n" % e)
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

