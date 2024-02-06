
import argparse
from colorama import Fore
from coinbase import coinbase_ws_producer
from calculate import calculate_best_price
from combine_order_books import combine_order_books
from parse_fetch import fetch_order_book_gemini, fetch_order_book_kraken, parse_kraken_order_book

import argparse


parser = argparse.ArgumentParser()
# Define a command-line argument 'quantity' with a default value of 10
# It represents the quantity of Bitcoin to buy or sell
parser.add_argument('--quantity', type=float, default=10, help='Quantity of Bitcoin to buy or sell')
args = parser.parse_args()
quantity = args.quantity

# Define WebSocket configuration settings
ws_uri = "wss://ws-feed.exchange.coinbase.com"
ws_channels = ["level2_batch"]
product_ids = ["BTC-USD"]

# Create a dictionary 'order_books' to store order book data from different exchanges
order_books = {
    "coinbase": coinbase_ws_producer(ws_uri, ws_channels, product_ids),
    "gemini": fetch_order_book_gemini(),
    "kraken": parse_kraken_order_book(fetch_order_book_kraken())
}

order_books_combined = combine_order_books(order_books)
best_price_buy, orders_used_buy = calculate_best_price(order_books_combined, quantity, 'bids')
best_price_sell, orders_used_sell = calculate_best_price(order_books_combined, quantity, 'asks')
# The 'orders_used_buy' and 'orders_used_sell' variables are returned for possible future buy/sell operations


def display_results(best_price_buy, best_sell_price):
    print(f'{"Action":<5} | {"Quantity":>8} BTC | {"Price":>12}')
    print('-' * 50)

    print(f'{"Buy":<5}  | {quantity:>8} BTC | {Fore.GREEN}${best_price_buy:>10,.2f}{Fore.RESET}')
    print(f'{"Sell":<5}  | {quantity:>8} BTC | {Fore.GREEN}${best_sell_price:>10,.2f}{Fore.RESET}')

display_results(best_price_buy, best_price_sell)
