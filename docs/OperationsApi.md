# swagger_client.OperationsApi

All URIs are relative to *https://broker.cex.io/api/public/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_order**](OperationsApi.md#cancel_order) | **POST** /operations/cancel-order | cancelOrder
[**cancel_order_group**](OperationsApi.md#cancel_order_group) | **POST** /operations/cancel-order-group | cancelOrderGroup
[**edit_account_order**](OperationsApi.md#edit_account_order) | **POST** /operations/edit-account-order | editOrder
[**get_account_metrics**](OperationsApi.md#get_account_metrics) | **POST** /operations/account-metrics | getAccountMetrics
[**get_market_data**](OperationsApi.md#get_market_data) | **POST** /marketdata | getMarketData
[**get_open_order_list**](OperationsApi.md#get_open_order_list) | **POST** /operations/open-orders-list | getOpenOrderList
[**get_order_history_list**](OperationsApi.md#get_order_history_list) | **POST** /operations/order-history | getOrderHistoryList
[**get_user_info**](OperationsApi.md#get_user_info) | **POST** /operations/user-info | getUserInfo
[**open_account_order**](OperationsApi.md#open_account_order) | **POST** /operations/place-account-order | placeOrder
[**open_account_order_group**](OperationsApi.md#open_account_order_group) | **POST** /operations/place-account-order-group | placeOrderGroup


# **cancel_order**
> CancelOrderHandlerResponse cancel_order(body=body)

cancelOrder

This API allows canceling order on an account. but can only cancel orders on behalf of other accounts if a special permission is set. The request can be used to cancel a single order.  Return status code 200

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
api_instance = swagger_client.OperationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body2() # Body2 |  (optional)

try:
    # cancelOrder
    api_response = api_instance.cancel_order(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->cancel_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body2**](Body2.md)|  | [optional] 

### Return type

[**CancelOrderHandlerResponse**](CancelOrderHandlerResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_order_group**
> CancelOrderGroupHandlerResponse cancel_order_group(body=body)

cancelOrderGroup

This API allows canceling order on an account. but can only cancel orders on behalf of other accounts if a special permission is set. The request can be used to cancel a multileg order.  Return status code 200

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
api_instance = swagger_client.OperationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body3() # Body3 |  (optional)

try:
    # cancelOrderGroup
    api_response = api_instance.cancel_order_group(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->cancel_order_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body3**](Body3.md)|  | [optional] 

### Return type

[**CancelOrderGroupHandlerResponse**](CancelOrderGroupHandlerResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_account_order**
> EditAccountOrderHandlerResponse edit_account_order(body=body)

editOrder

This API allows editing order details on an account.  The API is via POST and is idempotent. Only conditional requests are accepted.  Return status code 200

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
api_instance = swagger_client.OperationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body4() # Body4 |  (optional)

try:
    # editOrder
    api_response = api_instance.edit_account_order(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->edit_account_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body4**](Body4.md)|  | [optional] 

### Return type

[**EditAccountOrderHandlerResponse**](EditAccountOrderHandlerResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_metrics**
> AccountMetricsHandlerResponse get_account_metrics(body=body)

getAccountMetrics

This API allows viewing current \"metrics\" for an account, such as equity, margin, PnL etc.  Values in the API are fluent since they depend on current market data. So the client is either expected to poll the API to get current values or to make use of the notifications API (described in a separate document).  Return status code 200

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
api_instance = swagger_client.OperationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body1() # Body1 |  (optional)

try:
    # getAccountMetrics
    api_response = api_instance.get_account_metrics(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->get_account_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body1**](Body1.md)|  | [optional] 

### Return type

[**AccountMetricsHandlerResponse**](AccountMetricsHandlerResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_market_data**
> MarketDataHandlerResponse get_market_data(body=body)

getMarketData

This API allows to request for market data events. Supported Quote and Candle market data.  Return status code 200

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
api_instance = swagger_client.OperationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body() # Body |  (optional)

try:
    # getMarketData
    api_response = api_instance.get_market_data(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->get_market_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](Body.md)|  | [optional] 

### Return type

[**MarketDataHandlerResponse**](MarketDataHandlerResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_open_order_list**
> OpenOrderListHandlerResponse get_open_order_list(body=body)

getOpenOrderList

This API permits to view all the orders on your account.  Return status code 200

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
api_instance = swagger_client.OperationsApi(swagger_client.ApiClient(configuration))
body = NULL # object |  (optional)

try:
    # getOpenOrderList
    api_response = api_instance.get_open_order_list(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->get_open_order_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | [optional] 

### Return type

[**OpenOrderListHandlerResponse**](OpenOrderListHandlerResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_history_list**
> OrderHistoryListHandlerResponse get_order_history_list(body=body)

getOrderHistoryList

This API allows viewing historical orders (both working orders and orders in final state) on an account.  The API returns current state of the selected orders.  Return status code 200

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
api_instance = swagger_client.OperationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body5() # Body5 |  (optional)

try:
    # getOrderHistoryList
    api_response = api_instance.get_order_history_list(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->get_order_history_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body5**](Body5.md)|  | [optional] 

### Return type

[**OrderHistoryListHandlerResponse**](OrderHistoryListHandlerResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_info**
> UserInfoHandlerResponse get_user_info(body=body)

getUserInfo

This API permits to view details for a user  Return status code 200

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
api_instance = swagger_client.OperationsApi(swagger_client.ApiClient(configuration))
body = NULL # object |  (optional)

try:
    # getUserInfo
    api_response = api_instance.get_user_info(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->get_user_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | [optional] 

### Return type

[**UserInfoHandlerResponse**](UserInfoHandlerResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **open_account_order**
> OpenAccountOrderHandlerResponse open_account_order(body=body)

placeOrder

The API allows submitting a new order on an account.  The API is via POST, so it’s not idempotent.  To avoid issues with duplicate orders, a client is expected to submit a client-unique id of an order with the request. This id is used to track the order later on.  Return status code 200

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
api_instance = swagger_client.OperationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body6() # Body6 |  (optional)

try:
    # placeOrder
    api_response = api_instance.open_account_order(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->open_account_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body6**](Body6.md)|  | [optional] 

### Return type

[**OpenAccountOrderHandlerResponse**](OpenAccountOrderHandlerResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **open_account_order_group**
> OpenOrderGroupHandlerResponse open_account_order_group(body=body)

placeOrderGroup

The API allows submitting a group of orders on an account.  The API is via POST, so it’s not idempotent.  To avoid issues with duplicate orders, a client is expected to submit a client-unique id of an order with the request. This id is used to track the order later on.  Return status code 200

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
api_instance = swagger_client.OperationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body7() # Body7 |  (optional)

try:
    # placeOrderGroup
    api_response = api_instance.open_account_order_group(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->open_account_order_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body7**](Body7.md)|  | [optional] 

### Return type

[**OpenOrderGroupHandlerResponse**](OpenOrderGroupHandlerResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

