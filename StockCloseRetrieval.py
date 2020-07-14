#Using pandas data reader this program will print a table of close values for a list of stocks from a year from today up until today's date
#Note that I am retrieving the stock data using Yahoo Finance  

import pandas as pd
import pandas_datareader.data as pdr
import datetime as dt
#this list may be modified as desired and can include as many company ticker symbols as desired
tickers = ["AMZN", "RYCE", "DAL", "BNED", "NCBS", "C", "FAST", "WFC", "JPM"]

stock_df = pd.DataFrame()  #initialize the data frame for which we will put the data of each stock
completed = []
attempt = 0
while len(tickers) != 0 and attempt <=5:    #the attempts counter is a safety net in case the data isn't able to be received due to connection issues
    tickers = [j for j in tickers if j not in completed]    #add everything that isn't in the completed list to the list tickers
    for i in range(len(tickers)):
        try:
            temp = pdr.get_data_yahoo(tickers[i], dt.date.today()-dt.timedelta(365), dt.date.today())   #retrieve the data from Yahoo finance
            temp.dropna(inplace = True)
            stock_df[tickers[i]] = temp["Adj Close"]      #store the data in the stock data frame
            completed.append(tickers[i])
        except:     #in case we aren't able to receive the data
            print(tickers[i], ": Failed to fetch data...retrying")
            continue
    attempt += 1    
print(stock_df)
