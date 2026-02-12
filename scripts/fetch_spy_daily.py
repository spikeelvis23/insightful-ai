import requests
import pandas as pd
from datetime import datetime
import os

API_KEY = "WBEX3NWSANDGK46N"
SYMBOL = "SPY"
filename = f"data/spy_daily_{datetime.now().date()}.csv"

URL = (
    "https://www.alphavantage.co/query"
    "?function=TIME_SERIES_DAILY"
    f"&symbol={SYMBOL}"
    f"&apikey={API_KEY}"
    "&outputsize=full"
)

print("1. Requesting data from Alpha Vantage...")
response = requests.get(URL)
data = response.json()

# Check if we got the data or an error message
if "Time Series (Daily)" in data:
    print("2. Data received! Transforming to table...")
    time_series = data["Time Series (Daily)"]
    
    # Create the DataFrame
    df = pd.DataFrame.from_dict(time_series, orient="index")
    df.index = pd.to_datetime(df.index)
    df.columns = [c.split(". ")[1] for c in df.columns]
    df = df.astype(float).sort_index()

    # Save the file
    os.makedirs("data", exist_ok=True)
    df.to_csv(filename)
    print(f"3. ✅ SUCCESS! Saved {len(df)} rows to {filename}")
    
elif "Note" in data:
    print("❌ API LIMIT REACHED: Alpha Vantage says you've used your 25 daily calls.")
    print(f"Message: {data['Note']}")
    
elif "Error Message" in data:
    print("❌ API ERROR: Something is wrong with the request.")
    print(f"Message: {data['Error Message']}")
    
else:
    print("❌ UNKNOWN ERROR: The API returned something unexpected.")
    print(data)
