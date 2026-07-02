# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 330
}

portfolio = {}
total_value = 0

print("Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))

# Number of stocks to enter
n = int(input("How many different stocks do you own? "))

# Input stock details
for i in range(n):
    stock = input("\nEnter stock symbol: ").upper()

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))
        portfolio[stock] = quantity
    else:
        print("Stock not found in price list.")

# Calculate total investment value
print("\nPortfolio Summary")
print("-" * 30)

for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    total_value += value

    print(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${value}")

print("-" * 30)
print(f"Total Investment Value: ${total_value}")

# Optional: Save to a text file
save = input("\nDo you want to save the report? (yes/no): ").lower()

if save == "yes":
    with open("portfolio_report.txt", "w") as file:
        file.write("Portfolio Summary\n")
        file.write("-" * 30 + "\n")

        for stock, quantity in portfolio.items():
            value = stock_prices[stock] * quantity
            file.write(
                f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${value}\n"
            )

        file.write("-" * 30 + "\n")
        file.write(f"Total Investment Value: ${total_value}\n")

    print("Report saved as portfolio_report.txt")