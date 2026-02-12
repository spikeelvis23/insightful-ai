import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the data we prepared in the last step
file_path = "data/spy_with_indicators.csv"
if not os.path.exists(file_path):
    print(f"Error: {file_path} not found. Run calculate_indicators.py first.")
    exit()

df = pd.read_csv(file_path, index_col=0, parse_dates=True)

# We only want to plot the last 200 days so the chart isn't too crowded
df_recent = df.tail(200)

# Create a figure with two subplots (Price on top, RSI on bottom)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True, gridspec_kw={'height_ratios': [3, 1]})

# Plot 1: Price and SMA_50
ax1.plot(df_recent.index, df_recent['close'], label='Close Price', color='dodgerblue', alpha=0.8)
ax1.plot(df_recent.index, df_recent['SMA_50'], label='50-Day SMA', color='orange', linewidth=2)
ax1.set_title('SPY Price & 50-Day Moving Average (Last 200 Days)', fontsize=14)
ax1.set_ylabel('Price ($)')
ax1.legend(loc='upper left')
ax1.grid(True, alpha=0.2)

# Plot 2: RSI (Relative Strength Index)
ax2.plot(df_recent.index, df_recent['RSI'], label='RSI', color='purple')
ax2.axhline(70, linestyle='--', color='red', alpha=0.5)   # Overbought line
ax2.axhline(30, linestyle='--', color='green', alpha=0.5) # Oversold line
ax2.set_title('RSI Indicator', fontsize=12)
ax2.set_ylabel('Score')
ax2.set_ylim(0, 100)
ax2.grid(True, alpha=0.2)

# Save the image
os.makedirs("plots", exist_ok=True)
plot_path = "plots/spy_analysis.png"
plt.savefig(plot_path)
print(f"✅ Success! Chart saved to {plot_path}")

