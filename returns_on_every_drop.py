import pandas as pd

# input_file = r"C:\notebooks\Niftybees historical prices.csv"
input_file = "historical_data/NIFTYBEES_2023_ALL.csv"

df = pd.read_csv(input_file)
initial_cost = df["Close"].iloc[0]
print("initial cost is: ", initial_cost)

# price_day_one = df["Close Price"].iloc[0]
amt_invested = initial_cost
quant = 1
current_price = initial_cost

for item in df["Close"]:
    print("\nitem is: ", item)
    if current_price > item:  # Buy
        amt_invested += item
        quant += 1
        print("buying")

    else:
        # print("Not buying")
        pass

    current_price = item

print("Total Quantity bought: ", quant)
print("Total Amount invested : ", amt_invested)

average_price = amt_invested/quant
print("Average price is: ", average_price)

latest_price = df['Close'].iloc[-1]
print("Current latest price is: ", latest_price)

profit_loss = ((latest_price-average_price)/average_price)*100
print("Profit Loss is: ", round(profit_loss, 2), "%")
