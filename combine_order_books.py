# Combine order books from different exchanges
def combine_order_books(order_books):
    combined = {
        'bids': [],
        'asks': []
    }

    for exchange, books in order_books.items():
        for bid in books['bids']:
            # Copy the bid to avoid modifying the original order_books data
            new_bid = bid.copy()
            new_bid['exchange'] = exchange
            combined['bids'].append(new_bid)

        for ask in books['asks']:
            # Copy the ask to avoid modifying the original order_books data
            new_ask = ask.copy()
            new_ask['exchange'] = exchange
            combined['asks'].append(new_ask)

    return combined
