import yfinance as yf
import pandas as pd


stock = yf.Ticker('AAPL')
info = stock.info
print(info)
history = stock.history(period="ytd", interval="1d")
print(history)
#print(history.dtypes)
#history['Date'] = history['Date'] .dt.tz_localize(None)

# date_columns = history.select_dtypes(include=['datetime64[ns, EST]']).columns
# for date_column in date_columns:
#     history[date_column] = history[date_column].dt.date
    
#history.to_excel('out1.xlsx')