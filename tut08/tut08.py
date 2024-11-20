import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mplfinance as mpf

df = pd.read_csv('infy_stock.csv', index_col='Date', parse_dates=True)
# df.head(10)
print(df.head(10))
df.isnull().sum()

plt.figure(figsize=(12, 6))
plt.plot(df['Close'], label='Closing Price', color='blue')
plt.title('Closing Price Over Time')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

# df=pd.DataFrame(df)

mpf.plot(df.head(50), type='candle', title='Candlestick Chart', style='yahoo', ylabel='Price', volume=False)

df['Daily_Return'] = ((df['Close'] - df['Open']) / df['Open']) * 100

average_return = df['Daily_Return'].mean()
median_return = df['Daily_Return'].median()
standard_deviation = df['Close'].std()

df.head(10)
print(df.head(10))
print('\n')
print(f"Average Daily Return: {average_return:.2f}%")
print(f"Median Daily Return: {median_return:.2f}%")
print(f"Standard Deviation of Closing Prices: {standard_deviation:.2f}")
df.to_csv('infy_stock.csv', index=False)

df['50_Day_MA'] = df['Close'].rolling(window=50).mean()
df['200_Day_MA'] = df['Close'].rolling(window=200).mean()

print(df[['Close', '50_Day_MA', '200_Day_MA']].tail())

plt.figure(figsize=(12, 6))
plt.plot(df['Close'], label='Closing Price', color='blue')
plt.plot(df['50_Day_MA'], label='50 Day MA', color='red')
plt.plot(df['200_Day_MA'], label='200 Day MA', color='green')
# plt.title('Volatility')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

df.to_csv('infy_stock.csv', index=False)

df['Daily_Return'] = ((df['Close'] - df['Open']) / df['Open']) * 100
df['30_Day_Volatility'] = df['Close'].rolling(window=30).std()

print(df[['Close', 'Daily_Return', '30_Day_Volatility']].tail())

plt.figure(figsize=(12, 6))
# plt.plot(df['Close'], label='Closing Price', color='blue')
plt.plot(df['30_Day_Volatility'], label='Volatility', color='red')
plt.title('Volatility')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

df.to_csv('infy_stock.csv', index=False)

df['Bullish_Trend'] = df['50_Day_MA'] > df['200_Day_MA']
df['Bearish_Trend'] = df['50_Day_MA'] < df['200_Day_MA']

print(df[['Close', '50_Day_MA', '200_Day_MA', 'Bullish_Trend', "Bearish_Trend"]].tail())

mpf.plot(df.head(100), type='candle', volume=False, style='charles',
         title='Candlestick Chart with Bullish and Bearish Trends',
         ylabel='Price', ylabel_lower='Volume',
         figratio=(10,6))

df.to_csv('infy_stock.csv', index=False)
