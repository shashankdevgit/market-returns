# This code calculates the index returns if you buy a quant daily irrespective of the price fluctuation.

import pandas as pd


input_file = "historical_data/NIFTYBEES_2022_ALL.csv"
# input_file = "historical_data/BANKBEES_2023_ALL.csv"
# input_file = "historical_data/MAFANG_2023_ALL.csv"

df = pd.read_csv(input_file)
amt_invested = df['Close'].sum()
quant = df['Close'].count()
print("Total Quantity bought: ", quant)
print("Total Amount invested : ", amt_invested)

average_price = amt_invested/quant
print("Average price is: ", average_price)

latest_price = df['Close'].iloc[-1]
print("Current latest price is: ", latest_price)

profit_loss = ((latest_price-average_price)/average_price)*100
print("Profit/Loss is: ", round(profit_loss, 2), "%")
