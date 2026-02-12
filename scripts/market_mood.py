import pandas as pd

# Load the news we just downloaded
try:
    df = pd.read_csv("data/market_news_latest.csv")
    
    # Calculate the average sentiment
    avg_sentiment = df['overall_sentiment_score'].mean()
    
    print("-" * 30)
    print(f"MARKET MOOD REPORT")
    print("-" * 30)
    
    # Translate the number into a human feeling
    mood = "Neutral"
    if avg_sentiment > 0.15: mood = "Bullish (Optimistic) 📈"
    elif avg_sentiment < -0.15: mood = "Bearish (Pessimistic) 📉"
    
    print(f"Overall Sentiment: {mood}")
    print(f"Average Score: {avg_sentiment:.2f}")
    print(f"Total Stories Analyzed: {len(df)}")
    print("-" * 30)
    
    # Show the top 3 most "important" headlines
    print("Top Headlines:")
    for i, row in df.head(3).iterrows():
        print(f"• {row['title']}")
        
except FileNotFoundError:
    print("Error: No news file found. Run 'fetch_market_news.py' first!")


