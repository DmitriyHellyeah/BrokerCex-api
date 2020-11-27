# Body3

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contingency_type** | **str** | Contingency type of order group to cancel. Will appeared when create if-then order One of the following values (case-insensitive):  OCO – orders in the group are OCO orders. Once one order gets into a final state, the other ones are cancelled. For this group OPEN position effect and nonzero quantity should be set for both orders. Quantity equal for both orders. Note, OCO orders pair can be either traditional Limit/Stop pair with same side or pair with different sides, like Stop-Buy + Stop+Sell.  IF-THEN – orders in the group are parent and contingents. The first order is considered a parent(IF order) and the other ones become active after parent is filled. IF order should have OPEN position effect and nonzero quantity. THEN order(s) should have CLOSE position effect and either zero quantity (\&quot;position attached\&quot;) or quantity, equal by absolute value to IF order. The THEN orders should have opposite SIDE from the IF order. | [optional] 
**orders** | **list[str]** | Comma-separated list of order codes | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


