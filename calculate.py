
def calculate_price(order_book, quantity, side):
    price = 0
    accumulated = 0

    for order in order_book[side]:
        try:
            if isinstance(order, dict):
                order_price = float(order['price'])
                order_quantity = float(order['amount'])
            else:
                print(f"Error: Order format not recognized {order}")
                continue
        except ValueError:
            print(f"Error: Unable to convert order price or quantity to float for order {order}")
            continue

        if accumulated + order_quantity >= quantity:
            price += (quantity - accumulated) * order_price
            break
        else:
            price += order_quantity * order_price
            accumulated += order_quantity

    return price

def calculate_prices_for_all_exchanges(order_books, quantity, side):
    prices = {}
    for exchange, book in order_books.items():
        try:
            prices[exchange] = calculate_price(book, quantity, side)
        except Exception as e:
            print(f"Error calculating price for {exchange}: {e}")
    return prices

def calculate_best_price(order_books_combined, quantity, side):
    total_price = 0
    accumulated_quantity = 0
    included_orders = []  # List to keep track of orders used

    # Sort orders: ascending for 'asks' to buy at lowest price, descending for 'bids' to sell at highest price
    orders = sorted(order_books_combined[side], key=lambda x: float(x['price']), reverse=(side == 'bids'))

    for order in orders:
        order_price = float(order['price'])
        order_quantity = float(order['amount'])

        # Determine how much of this order can be used
        usable_quantity = min(order_quantity, quantity - accumulated_quantity)
        total_price += usable_quantity * order_price
        accumulated_quantity += usable_quantity

        # Add the used portion of the order to the included_orders list
        included_order = order.copy()
        included_order['amount'] = str(usable_quantity)  # Update the quantity to the amount actually used
        included_orders.append(included_order)

        # If we've accumulated enough to satisfy the requested quantity, exit the loop
        if accumulated_quantity >= quantity:
            break

    # Check if we've met the desired quantity
    if accumulated_quantity < quantity:
        # Not enough quantity available to fulfill the order
        return None, []

    return total_price, included_orders
