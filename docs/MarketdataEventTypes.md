# MarketdataEventTypes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**candle_type** | **str** | Required for Candle type. Candle type, one of next values: &lt;br /&gt; m (1 min) &lt;br /&gt; 5m (5 min) &lt;br /&gt; 15m (15 minutes) &lt;br /&gt; 30m (30 minutes) &lt;br /&gt; h (1 hour) &lt;br /&gt; 2h (2 hours) &lt;br /&gt; 4h (4 hours) &lt;br /&gt; d (Day) &lt;br /&gt; w (Week) &lt;br /&gt; mo (Month) &lt;br /&gt; | [optional] 
**count** | **int** | Maximum count of candles in response. If not defined, used value predefined on server side. &lt;br /&gt; If count of candles in [fromTime, toTime] period more, than count value, &lt;br /&gt; exactly count value of candles will be returned in response. More old candles will be filtered. | [optional] 
**format** | **str** | Quote and Candle type are supported | [optional] 
**from_time** | **datetime** | Required for Candle type. UTC time to get history from. | [optional] 
**to_time** | **datetime** | Required for Candle type. UTC time to get history to. | [optional] 
**type** | **str** | Now only COMPACT type is supported | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


