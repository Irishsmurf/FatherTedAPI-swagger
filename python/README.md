# father-ted-api
REST API for hand-curated Father Ted Quotes

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import father_ted_api 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import father_ted_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import father_ted_api
from father_ted_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = father_ted_api.CharactersApi(father_ted_api.ApiClient(configuration))

try:
    # List available characters.
    api_response = api_instance.characters_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CharactersApi->characters_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.fatherted.irish*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CharactersApi* | [**characters_get**](docs/CharactersApi.md#characters_get) | **GET** /characters | List available characters.
*EpisodesApi* | [**episodes_get**](docs/EpisodesApi.md#episodes_get) | **GET** /episodes | List available episodes.
*QuotesApi* | [**quotes_get**](docs/QuotesApi.md#quotes_get) | **GET** /quotes | Retrieve Quotes
*QuotesApi* | [**quotes_random_get**](docs/QuotesApi.md#quotes_random_get) | **GET** /quotes/random | Retrieve a Random Quote
*SeriesApi* | [**series_get**](docs/SeriesApi.md#series_get) | **GET** /series | List available series.


## Documentation For Models

 - [Quote](docs/Quote.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author

dave@paddez.com
