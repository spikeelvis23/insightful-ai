import pandas as pd
import os
import glob

# Find the latest data file we downloaded
list_of_files = glob.glob('data/spy_daily_*.csv')
if not list_of_files:
    print("Error: No data files found in data/ folder.")
    exit()
latest_file = max(list_of_files, key=os.path.getctime)

print(f"Analyzing: {latest_file}")

# Load data
df = pd.read_csv(latest_file, index_col=0, parse_dates=True)

# 1. Simple Moving Average (50-day)
df['SMA_50'] = df['close'].rolling(window=50).mean()

# 2. RSI (Relative Strength Index) - Simple version
delta = df['close'].diff()
gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
rs = gain / loss
df['RSI'] = 100 - (100 / (1 + rs))

# Create a 'Signal' column for the AI
# If RSI < 30, it's 'Oversold' (Potential Buy)
# If RSI > 70, it's 'Overbought' (Potential Sell)
df['Signal'] = 'Neutral'
df.loc[df['RSI'] < 30, 'Signal'] = 'BUY (Oversold)'
df.loc[df['RSI'] > 70, 'Signal'] = 'SELL (Overbought)'

# Save the "Smart" data
output_file = "data/spy_with_indicators.csv"
df.to_csv(output_file)

print(f"✅ Indicators calculated! Saved to {output_file}")
print("\nLatest Signal Check:")
print(df[['close', 'SMA_50', 'RSI', 'Signal']].tail(5))

