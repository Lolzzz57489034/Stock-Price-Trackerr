import requests
import streamlit as st
import pandas as pd
import datetime
import matplotlib.pyplot as plt

# Alpha Vantage API Key
API_KEY = "YOUR_API_KEY"
BASE_URL = "https://www.alphavantage.co/query"

# Streamlit App
st.title("📈 Stock Market Price Tracker")

# User input for stock symbol
stock_symbol = st.text_input("Enter Stock Symbol (e.g., RELIANCE.BSE, TCS.BSE):", "").strip().upper()

if st.button("Get Price"):
    if not stock_symbol:
        st.error("Please enter a stock symbol.")
    else:
        params = {
            "function": "TIME_SERIES_INTRADAY",
            "symbol": stock_symbol,
            "interval": "5min",
            "apikey": API_KEY
        }
        
        try:
            response = requests.get(BASE_URL, params=params)
            response.raise_for_status()
            data = response.json()
            
            if "Time Series (5min)" not in data:
                st.error("Invalid stock symbol or API limit exceeded.")
            else:
                time_series = data["Time Series (5min)"]
                timestamps = list(time_series.keys())[::-1]  # Reverse to show oldest first
                prices = [float(time_series[t]["4. close"]) for t in timestamps]

                current_price = prices[-1]
                st.subheader(f"Current Price: ₹{current_price:.2f}")

                # Convert data to DataFrame
                df = pd.DataFrame({"Time": timestamps, "Price": prices})
                df["Time"] = pd.to_datetime(df["Time"])
                
                # Plot the stock price trend
                fig, ax = plt.subplots(figsize=(10, 5))
                ax.plot(df["Time"], df["Price"], marker='o', linestyle='-', color='b', label=stock_symbol)
                ax.set_title(f"Stock Price Trend: {stock_symbol}")
                ax.set_xlabel("Time")
                ax.set_ylabel("Price in INR")
                ax.legend()
                plt.xticks(rotation=45)
                
                st.pyplot(fig)

        except requests.exceptions.RequestException as e:
            st.error(f"Network error: {e}")
