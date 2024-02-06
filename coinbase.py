import json
from datetime import date, datetime

from kafka import KafkaProducer
from websocket import create_connection

def json_serializer(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise "Type %s not serializable" % type(obj)

def format_datetime(datetime_string: str) -> str:
    return (datetime
            .strptime(datetime_string,"%Y-%m-%dT%H:%M:%S.%fZ")
            .strftime("%Y-%m-%d %H:%M:%S")
    )

def coinbase_ws_producer(ws_uri,ws_channels,product_ids):

    ws = create_connection(ws_uri)
    ws.send(
        json.dumps(
                {
                    "type": "subscribe",
                    "product_ids": product_ids,
                    "channels": ws_channels,
                }
            )
    )

    while True:
        message = ws.recv()
        data = json.loads(message)
        if data["type"] == "snapshot":
            
            asks = [{
                  
                    "price": order[0],
                    "amount": order[1],
                    "timestamp": format_datetime(data["time"])
                    } for order in data["asks"]
                ]
            
            bids = [{
                    "price": order[0],
                    "amount": order[1],
                    "timestamp": format_datetime(data["time"])
                    } for order in data["bids"]
                ]
            
            order_book = {"asks":asks, "bids":bids}


            return order_book
