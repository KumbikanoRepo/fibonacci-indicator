import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
yf.pdr_override()

df = pd.read_csv("C:/Users/User\Desktop/sample output/Fibonacci indicator/data/MSFT.csv")


# Define the significant price move - specify the start and end points
start_price = df['Close'].iloc[0] 
end_price = df['Close'].iloc[-1]  

# Calculate Fibonacci retracement levels
fib_levels = [0.236, 0.382, 0.500, 0.618, 0.786, 1.000]
retracement_levels = [(start_price - (level * (start_price - end_price))) for level in fib_levels]

#fibonacci level line colours
line_colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Create a plot of the stock price data
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Close'], label='Stock Price', color='blue')

# Plot Fibonacci retracement levels as horizontal lines
for level, retracement_price, color in zip(fib_levels, retracement_levels, line_colors):
    plt.axhline(y=retracement_price, color=color, linestyle='--', label=f'{level*100}% Fibonacci Level')

#plot
plt.title('Stock Price with Fibonacci Retracement Levels')
plt.xlabel('Date')
plt.ylabel('Price')
plt.xticks(rotation = 60)
plt.legend()
plt.grid(True)
plt.show()
