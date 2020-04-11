# father_ted_api.QuotesApi

All URIs are relative to *https://api.fatherted.irish*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quotes_get**](QuotesApi.md#quotes_get) | **GET** /quotes | Retrieve Quotes
[**quotes_random_get**](QuotesApi.md#quotes_random_get) | **GET** /quotes/random | Retrieve a Random Quote


# **quotes_get**
> list[Quote] quotes_get(series=series, episode=episode, character=character)

Retrieve Quotes

Retrieve quotes

### Example
```python
from __future__ import print_function
import time
import father_ted_api
from father_ted_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = father_ted_api.QuotesApi()
series = 'series_example' # str | Retrieve all quotes for a given series. (optional)
episode = 'episode_example' # str | Retrieve all quotes for a given episode title. (optional)
character = 'character_example' # str | Retrieve all quotes for a given character. (optional)

try:
    # Retrieve Quotes
    api_response = api_instance.quotes_get(series=series, episode=episode, character=character)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotesApi->quotes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series** | **str**| Retrieve all quotes for a given series. | [optional] 
 **episode** | **str**| Retrieve all quotes for a given episode title. | [optional] 
 **character** | **str**| Retrieve all quotes for a given character. | [optional] 

### Return type

[**list[Quote]**](Quote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quotes_random_get**
> Quote quotes_random_get(series=series, episode=episode, character=character)

Retrieve a Random Quote

Retrieves a single quote from the given parameters.

### Example
```python
from __future__ import print_function
import time
import father_ted_api
from father_ted_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = father_ted_api.QuotesApi()
series = 'series_example' # str | Retrieve all quotes for a given series. (optional)
episode = 'episode_example' # str | Retrieve all quotes for a given episode title. (optional)
character = 'character_example' # str | Retrieve all quotes for a given character. (optional)

try:
    # Retrieve a Random Quote
    api_response = api_instance.quotes_random_get(series=series, episode=episode, character=character)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotesApi->quotes_random_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series** | **str**| Retrieve all quotes for a given series. | [optional] 
 **episode** | **str**| Retrieve all quotes for a given episode title. | [optional] 
 **character** | **str**| Retrieve all quotes for a given character. | [optional] 

### Return type

[**Quote**](Quote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

