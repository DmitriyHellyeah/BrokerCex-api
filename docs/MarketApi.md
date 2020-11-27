# swagger_client.MarketApi

All URIs are relative to *https://broker.cex.io/api/public/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_market_info**](MarketApi.md#get_market_info) | **GET** /info | getMarketInfo
[**get_order_book**](MarketApi.md#get_order_book) | **GET** /orderbook | getOrderBook


# **get_market_info**
> InlineResponse200 get_market_info(body=body)

getMarketInfo

This API allows to request for market info.  Return status code 200

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['broAuth'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['broAuth'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MarketApi(swagger_client.ApiClient(configuration))
body = NULL # object |  (optional)

try:
    # getMarketInfo
    api_response = api_instance.get_market_info(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->get_market_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_book**
> InlineResponse2001 get_order_book(body=body)

getOrderBook

This API allows to request for orderbook.  Return status code 200

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['broAuth'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['broAuth'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MarketApi(swagger_client.ApiClient(configuration))
body = NULL # object |  (optional)

try:
    # getOrderBook
    api_response = api_instance.get_order_book(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->get_order_book: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

