import streamlit as st
import yfinance as yf
import datetime

stock = st.text_input("Enter the stock name", "AAPL")

col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("START_DATE", value=datetime.datetime(2019, 1, 1))
with col2:
    end_date = st.date_input("END_DATE", value=datetime.datetime(2023, 1, 1))

data = yf.download(tickers=stock, start=start_date, end=end_date)

# st.write(data)
st.line_chart(data['Close'])
st.bar_chart(data['Volume'])