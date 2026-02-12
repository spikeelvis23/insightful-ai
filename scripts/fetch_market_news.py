import requests
import pandas as pd
import os

API_KEY = "WBEX3NWSANDGK46N"

# We want news specifically about finance and the market
URL = (
    "https://www.alphavantage.co/query"
    "?function=NEWS_SENTIMENT"
    "&tickers=AAPL,MSFT,SPY"  # Focus on SPY and top tech movers
    f"&apikey={API_KEY}"
    "&limit=50"
)

print("Fetching latest market news and sentiment...")

response = requests.get(URL)
data = response.json()

articles = data.get("feed", [])
if not articles:
    print("No news found or API limit reached.")
else:
    # Extract the info we actually care about
    news_list = []
    for item in articles:
        news_list.append({
            "title": item.get("title"),
            "time_published": item.get("time_published"),
            "summary": item.get("summary"),
            "overall_sentiment_score": item.get("overall_sentiment_score"),
            "url": item.get("url")
        })

    # Save to a CSV
    df = pd.DataFrame(news_list)
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/market_news_latest.csv", index=False)
    
    print(f"✅ Success! Captured {len(df)} news stories with sentiment scores.")
    print("\nSample Headline:")
    print(df['title'].iloc[0])


