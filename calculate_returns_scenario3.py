"""
Calculate returns based on the scenario below:
1. Buy the first day.
2. Now from the next day, buy if the closing price is less than the first day price.
3. Once we buy for the 2nd time, that price will be our least_price.
4. Now buy only on when the price of the index goes below the 'least_price'.
5. Until the price of the instrument does not go below the 'least_price', we do not buy.

Note: This is yet to be tested for different instruments and years.
"""


# Calculate index returns whenever there is a fall in today's closing price compared to the last day's closing price.

import pandas as pd

# input_file = r"C:\notebooks\Niftybees historical prices.csv"
input_file = "historical_data/NIFTYBEES_2022_ALL.csv"
# input_file = "historical_data/BANKBEES_2023_ALL.csv"
# input_file = "historical_data/MAFANG_2022_ALL.csv"

df = pd.read_csv(input_file)
initial_cost = df["Close"].iloc[0]
print("initial cost is: ", initial_cost)

# price_day_one = df["Close Price"].iloc[0]
amt_invested = initial_cost
quant = 1
current_price = initial_cost
quantity_to_add_everytime = 1  # this quantity can vary based on one's budget


for daily_close_price in df["Close"].iloc[1:]:
    if daily_close_price < current_price:  # Buy
        amt_invested += (daily_close_price * quantity_to_add_everytime)
        quant += quantity_to_add_everytime
        current_price = daily_close_price
        print("buying...")

print("Total Quantity bought: ", quant)
print("Total Amount invested : ", round(amt_invested, 2))

average_price = round(amt_invested/quant, 3)
print("Average price is: ", average_price)

latest_price = df['Close'].iloc[-1]
print("Current latest price is: ", latest_price)

profit_loss = ((latest_price-average_price)/average_price)*100
print("Profit/Loss is: ", round(profit_loss, 2), "%")
print("Current market Price of the investment: ", round(quant*latest_price, 0))
