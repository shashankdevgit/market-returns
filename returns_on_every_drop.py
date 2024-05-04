# Calculate index returns whenever there is a fall in today's closing price compared to the last day's closing price.

import pandas as pd

# input_file = r"C:\notebooks\Niftybees historical prices.csv"
input_file = "historical_data/NIFTYBEES_2022_ALL.csv"
# input_file = "historical_data/BANKBEES_2023_ALL.csv"
# input_file = "historical_data/MAFANG_2023_ALL.csv"

df = pd.read_csv(input_file)
initial_cost = df["Close"].iloc[0]
print("initial cost is: ", initial_cost)

# price_day_one = df["Close Price"].iloc[0]
amt_invested = initial_cost
quant = 1
current_price = initial_cost

for daily_close_price in df["Close"].iloc[1:]:
    if daily_close_price < current_price:  # Buy
        amt_invested += daily_close_price
        quant += 1

        print("buying...")
    else:
        print("Not buying...")

    current_price = daily_close_price

print("Total Quantity bought: ", quant)
print("Total Amount invested : ", amt_invested)

average_price = round(amt_invested/quant, 3)
print("Average price is: ", average_price)

latest_price = df['Close'].iloc[-1]
print("Current latest price is: ", latest_price)

profit_loss = ((latest_price-average_price)/average_price)*100
print("Profit/Loss is: ", round(profit_loss, 2), "%")
