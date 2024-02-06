import unittest

# Import the function you want to test
from main import calculate_best_price

class TestCalculateBestPrice(unittest.TestCase):

    def test_calculate_best_price_bids(self):
        order_books_combined = {
            'bids': [
                {'price': '5000', 'amount': '2'},
                {'price': '4900', 'amount': '3'},
                {'price': '4800', 'amount': '5'},
            ],
            'asks': [
                {'price': '5100', 'amount': '1'},
                {'price': '5200', 'amount': '2'},
                {'price': '5300', 'amount': '4'},
            ]
        }
        quantity = 7
        side = 'bids'

        total_price, included_orders = calculate_best_price(order_books_combined, quantity, side)

        self.assertEqual(total_price, 5000 * 2 + 4900 * 3 + 4800 * 2)  # Expected total price
        self.assertEqual(len(included_orders), 3)  # Expected number of included orders
        # You can add more specific assertions for included orders if needed

    def test_calculate_best_price_asks(self):
        order_books_combined = {
            'bids': [
                {'price': '5000', 'amount': '2'},
                {'price': '4900', 'amount': '3'},
                {'price': '4800', 'amount': '5'},
            ],
            'asks': [
                {'price': '5100', 'amount': '1'},
                {'price': '5200', 'amount': '2'},
                {'price': '5300', 'amount': '4'},
            ]
        }
        quantity = 7
        side = 'asks'

        total_price, included_orders = calculate_best_price(order_books_combined, quantity, side)

        self.assertEqual(total_price, 5100 * 1 + 5200 * 2 + 5300 * 4)  # Expected total price
        self.assertEqual(len(included_orders), 3)  # Expected number of included orders
        # You can add more specific assertions for included orders if needed

if __name__ == '__main__':
    unittest.main()
