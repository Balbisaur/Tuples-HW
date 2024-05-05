def closing_price(stock_data, stock_symbol):
    closing_prices = []
    for data in stock_data:
        symbol,_, closing_price = data
        if symbol == stock_symbol:
            closing_prices.append(closing_price)
    if closing_prices:
        average_price = sum(closing_prices) / len(closing_prices)
        return average_price
    else:
        return None

stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    
]


stock_symbol = "AAPL"
avg_price = closing_price(stock_data, stock_symbol)
if avg_price is not None:
    print(f"The average closing price of {stock_symbol} is {avg_price:.2f}")
else:
    print(f"No data found for {stock_symbol}")