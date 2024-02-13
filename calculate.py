
def calculate_best_price(order_books_combined, quantity, side):
    total_price = 0
    accumulated_quantity = 0
    included_orders = []  # List to keep track of orders used
    limit_orders = {"coinbase": { "quantity":0, "price": 0}, 
                   "gemini": { "quantity":0, "price": 0}, 
                   "kraken": { "quantity":0, "price": 0}}

    # Sort orders: ascending for 'asks' to buy at lowest price, descending for 'bids' to sell at highest price
    orders = sorted(order_books_combined[side], key=lambda x: float(x['price']), reverse=(side == 'bids'))
    for order in orders:
        order_price = float(order['price'])
        order_quantity = float(order['amount'])
    
          # If we've accumulated enough to satisfy the requested quantity, exit the loop
        if accumulated_quantity >= quantity:
            break

        # Determine how much of this order can be used
        usable_quantity = min(order_quantity, quantity - accumulated_quantity)
        total_price += usable_quantity * order_price
        accumulated_quantity += usable_quantity

        # Add the used portion of the order to the included_orders list
        included_order = order.copy()
        included_order['amount'] = str(usable_quantity)  # Update the quantity to the amount actually used
        included_orders.append(included_order)

        limit_orders[order["exchange"]]["quantity"] +=  order_quantity
        limit_orders[order["exchange"]]["price"] = order['price']

    # Check if we've met the desired quantity
    if accumulated_quantity < quantity :
        # Not enough quantity available to fulfill the order
        return None, []

    print("limit_orders:")
    print(limit_orders)
    print("\n")
    return total_price, included_orders
