import streamlit as st
import yfinance as yf
import datetime as dt

st.write(
    """
        # This is the demo of streamlit
        I am going to create stock tracker using streamlit and yfinance library. This is a simple stock tracker that will show you the daily closing range chart and volume of shares every day for a given stock ticker symbol.
"""
)

col1,col2 = st.columns(2)

with col1:
     strat_date = st.date_input("Please enter the start date", dt.date(2019,1,1))
with col2:
     end_date = st.date_input("Please enter the end date", dt.date(2026,11,7))

ticker_symbol = st.text_input("Enter stock symbol", "AAPL",key="Placeholder")

ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(
    start=strat_date,
    end=end_date
)


st.write(
    f"""
    ## {ticker_symbol}'s chart 
    """
)

st.dataframe(ticker_df)

st.write(
    f"""
    ## {ticker_symbol}'s daily closing range chart
    """
)
st.line_chart(ticker_df.Close)

st.write(
    f"""
    ## {ticker_symbol}'s volume of shares every day
    """
)
st.line_chart(ticker_df.Volume)