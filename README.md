# Order Book Analyzer

The Order Book Analyzer is a Python script that fetches order book data from multiple cryptocurrency exchanges, calculates the best buy and sell prices, and displays the results. This tool is helpful for traders looking to make informed decisions in the cryptocurrency market.

## Prerequisites

- Python 3.11.7
- Required Python packages are listed in `pyproject.toml` and can be installed using Poetry.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/KatyaPrusakova/book_aggregator.git
   cd book_aggregator
   ```

2. Install the required packages using Poetry:
    ```bash
    poetry install
   ```

## Usage

To run the Order Book Analyzer, use the following command:
  ```bash
poetry run python main.py
   ```

This command will run the script, which will aggregate order book data from different exchanges, calculate the best buy and sell prices for a default quantity of 10 BTC (you can adjust the quantity using command-line arguments), and display the results.


## Command-line Arguments

You can customize the quantity of Bitcoin to buy or sell by providing a command-line argument. For example:


  ```bash
poetry run python main.py --quantity 5
   ```
This command will run the script with a quantity of 5 BTC.

## Code Structure

- `main.py`: The main script that orchestrates the order book analysis.
- `calculate.py`: Contains the logic for calculating the best buy and sell prices.
- `coinbase.py`: Contains the logic for fetching data from coinbase exchange.
- `combine_order_books.py`: Contains the function to combine order books from different exchanges.
- `parse_fetch.py`: Contains functions to fetch and parse order book data from specific exchanges.
- `test.py`: Unit tests for the functions in the code.

## Dependencies
This project uses the following Python libraries:

- **requests**: Used for making HTTP requests to fetch order book data.
- **argparse**: Used for parsing command-line arguments.
- **websocket-client**: Used for WebSocket communication.
- **colorama**: Used for colorizing console output.


## Tests
To run the tests for the code, use the following command:

  ```bash
    poetry run python test.py
   ```
This will execute the unit tests defined in the test.py file to ensure the functionality of the code.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request. I welcome contributions and improvements.