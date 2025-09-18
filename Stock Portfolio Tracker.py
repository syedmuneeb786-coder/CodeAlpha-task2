# Hardcoded stock prices
stock_prices = {"AAPL": 180, "TSLA": 250, "MSFT": 310, "GOOG": 2800}

portfolio = {}
total_value = 0

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock in stock_prices:
        qty = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + qty
    else:
        print("❌ Stock not found.")

# Calculate total value
for stock, qty in portfolio.items():
    total_value += stock_prices[stock] * qty

print("\n📊 Portfolio Summary:")
for stock, qty in portfolio.items():
    print(f"{stock} - {qty} shares = ${stock_prices[stock] * qty}")

print("💰 Total Investment Value: $", total_value)

# Save result to file
with open("portfolio.txt", "w") as f:
    f.write("Portfolio Summary\n")
    for stock, qty in portfolio.items():
        f.write(f"{stock}: {qty} shares = ${stock_prices[stock] * qty}\n")
    f.write(f"Total Investment: ${total_value}\n")
