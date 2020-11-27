# Body6

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expire_date** | **str** | Order expiration date in UTC. Must be present if tif field is GTD. Otherwise must be omitted. | [optional] 
**instrument** | **str** | Symbol of the instrument. | 
**limit_price** | **float** | Limit order price per unit of quantity (use stopPrice for stop orders). Should be absent for Market and Stop orders | [optional] 
**order_code** | **str** | For Place orders it is unique id assigned by the client. The id is expected to be unique among all orders on an account  example of usage:  0000000005 / order_0000000005 | 
**position_code** | **str** | ID of a position that should be modified by this order. Used for position based trading. Must be present when positionEffect is ‘Close’ and omitted otherwise. | [optional] 
**position_effect** | **str** | Possible values:  OPEN  CLOSE | [optional] 
**price_link** | **str** | Price link for protection orders. Possible values:  TRIGGERED_STOP stop price of order will be taken from parent trigger order’s fill price  TRIGGERED_LIMIT limit price of order will be taken from parent trigger order’s fill price  Now we have field for order type: type, and priceLink should be equal to this field. But in the future another types of protection orders might be created, which don’t guarantee equal of type and priceLink. | [optional] 
**price_offset** | **float** | Price offset for protection orders. When parent order is triggered, either stop or limit price of protection order will be taken from parent trigger order’s fill price with price offset. If this value is not null, priceLink field must be present | [optional] 
**quantity** | **float** | Initial quantity of the order | [optional] 
**side** | **str** | Order operation. Possible values are:  BUY  SELL | 
**stop_price** | **float** | Stop order price per unit of quantity (use limitPrice for limit orders). Should be absent for Market and Limit orders | [optional] 
**tif** | **str** | Time in force (expiration time for the order). One of:  DAY  GTC  IOC  FOK  GTD (requires expireDate field)  Default value depends on the platform configuration.  Value are case-insensitive. | [optional] 
**type** | **str** | Order type. Possible values:  MARKET  LIMIT  STOP | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


