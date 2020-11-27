import swagger_client
from BrokerAPIKeyAuthenticator import generate_signature

apiKey = "EH7tZeUqs5Bi"
apiSecret = "DiqZaC-koidsAIsan_XHlLb"

api = swagger_client.OperationsApi(swagger_client.ApiClient(swagger_client.Configuration()))

# GET ACCOUNT METRICS
acc_metrics_req_body = swagger_client.Body1()
acc_metrics_req_body.include_positions = True

message = api.api_client.sanitize_for_serialization(acc_metrics_req_body)

api.api_client.configuration.api_key = {"broAuth": "{},{}".format(apiKey, generate_signature(apiSecret, message))}
api.get_account_metrics(**{"body": {"data": {"include_positions": True}}})


# [SINGLE ORDER]
# PLACE ORDER [Single Limit Order]
# order_code must be unique for every new order
body = {
    "order_code": "0000000014",
    "type": "LIMIT",
    "instrument": "BTC/USD",
    "quantity": 0.001,
    "position_effect": "OPEN",
    "side": "BUY",
    "limit_price": 17551.50,
    "tif": "GTC"
}
place_order_req_body = swagger_client.Body6(**body)

message = api.api_client.sanitize_for_serialization(place_order_req_body)

api.api_client.configuration.api_key = {"broAuth": "{},{}".format(apiKey, generate_signature(apiSecret, message))}
api.open_account_order(**{"body": {"data": place_order_req_body}})


# CANCEL ORDER
cancel_order_req_body = swagger_client.Body2()
cancel_order_req_body.order_id = "0000000013"

message = api.api_client.sanitize_for_serialization(cancel_order_req_body)

api.api_client.configuration.api_key = {"broAuth": "{},{}".format(apiKey, generate_signature(apiSecret, message))}
api.cancel_order(**{"body": {"data": cancel_order_req_body}})


# PLACE ORDER [Single Market Order]
# order_code must be unique for every new order
body = {
    "order_code": "0000000035",
    "type": "MARKET",
    "instrument": "XRP/USD",
    "quantity": 1,
    "position_effect": "OPEN",
    "side": "BUY",
    "tif": "GTC"
}
place_order_req_body = swagger_client.Body6(**body)

message = api.api_client.sanitize_for_serialization(place_order_req_body)

api.api_client.configuration.api_key = {"broAuth": "{},{}".format(apiKey, generate_signature(apiSecret, message))}
api.open_account_order(**{"body": {"data": place_order_req_body}})


# PLACE ORDER [Single Stop Order]
# order_code must be unique for every new order
body = {
    "order_code": "0000000026",
    "type": "STOP",
    "instrument": "XRP/USD",
    "quantity": 1,
    "position_effect": "OPEN",
    "side": "BUY",
    "stop_price": 1.29500,
    "tif": "GTC"
}
place_order_req_body = swagger_client.Body6(**body)

message = api.api_client.sanitize_for_serialization(place_order_req_body)

api.api_client.configuration.api_key = {"broAuth": "{},{}".format(apiKey, generate_signature(apiSecret, message))}
api.open_account_order(**{"body": {"data": place_order_req_body}})


# PLACE ORDER [Single Market Order Closing Position]
# order_code must be unique for every new order
body = {
    "order_code": "0000000017",
    "type": "MARKET",
    "instrument": "XRP/USD",
    "quantity": 1,
    "position_effect": "CLOSE",
    "side": "BUY",
    "position_code": "123",
    "tif": "GTC"
}
place_order_req_body = swagger_client.Body6(**body)

message = api.api_client.sanitize_for_serialization(place_order_req_body)

api.api_client.configuration.api_key = {"broAuth": "{},{}".format(apiKey, generate_signature(apiSecret, message))}
api.open_account_order(**{"body": {"data": place_order_req_body}})



# PLACE ORDER GROUP [OCO]

body = {
        "orders": [
            {
                "orderCode": "ds_0000000061",
                "type": "LIMIT",
                "instrument": "XRP/USD",
                "quantity": "20",
                "positionEffect": "OPEN",
                "side": "BUY",
                "limitPrice": "1.32000",
                "tif": "GTC"
            },
            {
                "orderCode": "ds_0000000062",
                "type": "STOP",
                "instrument": "XRP/USD",
                "quantity": "20",
                "positionEffect": "OPEN",
                "side": "BUY",
                "stopPrice": "1.34000",
                "tif": "GTC"
            }
        ],
        "contingencyType": "OCO"
    }

place_order_req_body = swagger_client.Body7(**body)

message = api.api_client.sanitize_for_serialization(place_order_req_body)

api.api_client.configuration.api_key = {"broAuth": "{},{}".format(apiKey, generate_signature(apiSecret, message))}
api.open_account_order(**{"body": {"data": place_order_req_body}})


# PLACE ORDER GROUP [IF-THEN]
# Multileg Order Request

body = {
    "orders": [
        {
            "orderCode": "ds_0000000036",
            "type": "LIMIT",
            "instrument": "USD/CAD",
            "quantity": 30,
            "positionEffect": "OPEN",
            "side": "BUY",
            "limitPrice": 1.29500,
            "tif": "GTC"

        },
        {
            "orderCode": "ds_0000000037",
            "type": "LIMIT",
            "instrument": "USD/CAD",
            "quantity": 0,
            "positionEffect": "CLOSE",
            "side": "SELL",
            "limitPrice": 1.29500,
            "tif": "GTC"

        }
    ],
    "contingencyType": "IF-THEN"
}

place_order_req_body = swagger_client.Body7(**body)

message = api.api_client.sanitize_for_serialization(place_order_req_body)

api.api_client.configuration.api_key = {"broAuth": "{},{}".format(apiKey, generate_signature(apiSecret, message))}
api.open_account_order(**{"body": {"data": place_order_req_body}})

