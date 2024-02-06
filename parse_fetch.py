import requests

def fetch_order_book_gemini():
    response = requests.get('https://api.gemini.com/v1/book/btcusd')
    return response.json()

def fetch_order_book_kraken():
    response = requests.get('https://api.kraken.com/0/public/Depth?pair=XBTUSD')
    return response.json()

def parse_orders(order_book, order_type):
    return [{
        "price": float(order[0]),
        "amount": float(order[1]),
        "timestamp": int(order[2])
    } for order in order_book['result']['XXBTZUSD'][order_type]]

def parse_kraken_order_book(kraken_order_book):
    asks = parse_orders(kraken_order_book, 'asks')
    bids = parse_orders(kraken_order_book, 'bids')

    return {"asks": asks, "bids": bids}
