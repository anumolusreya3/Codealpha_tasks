# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 130,
    "MSFT": 320
}

# Variable to store total investment
total_investment = 0

print("📈 Stock Portfolio Tracker")

# Loop to take input from user
while True:

    stock_name = input("\nEnter stock name (or type 'done' to finish): ").upper()

    # Stop the loop
    if stock_name == "DONE":
        break

    # Check if stock exists
    if stock_name in stock_prices:

        quantity = int(input("Enter quantity: "))

        # Calculate investment
        investment = stock_prices[stock_name] * quantity

        # Add to total
        total_investment += investment

        print(f"{stock_name} Investment = ${investment}")

    else:
        print("Stock not found!")

# Final output
print("\n💰 Total Investment Value = $", total_investment)

# Optional: Save result to file
file = open("portfolio.txt", "w")

file.write(f"Total Investment Value = ${total_investment}")

file.close()

print("✅ Portfolio saved to portfolio.txt")
