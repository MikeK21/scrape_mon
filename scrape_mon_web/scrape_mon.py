#!/usr/bin/python3
import urllib.request
import json
from datetime import date
from datetime import timedelta
import os

APIKEY = "C227WD9W3LUVKVV9"

def scrape_json(stockSymbol,nDays):

    with urllib.request.urlopen(f"https://www.alphavantage.co/query?apikey={APIKEY}&function=TIME_SERIES_DAILY_ADJUSTED&symbol={stockSymbol}") as url:
        data = json.loads(url.read().decode())
        #print(data['Time Series (Daily)']['2021-12-14'])
        #exit()
        
    dateList = []
    nDays = int(nDays) + 1
    for i in range(1,nDays):
        dateAdd = date.today() - timedelta(days=i)
        dateList.append(dateAdd.strftime("%Y-%m-%d"))
        
    #date.today().strftime("%Y-%m-%d")
    stockDict = {}
    stockDictMetrics = {}
    for i in dateList:
        try:
            stockDictMetrics[i] = data['Time Series (Daily)'][i]['4. close']
        except:
            print(f"Date: {i} not found")
            
    stockDict[stockSymbol] = stockDictMetrics
        
    print(stockDict)
    return stockDict 

def getUserRequest():
    
    try:
        stockSymbol = input("Enter Stock Symbol: ")
    except:
        print("Please enter valid Stock Symbol")
        
    try:
        nDays = input("Enter number of days to look back on: ")
    except:
        print("Please enter valid integer for date retrieval")
    
    scrape_json(stockSymbol, nDays) 
    
def getEnvRequest():
    
    try:
        os.environ['STOCKSYMBOL'] = "MSFT"
        stockSymbol = os.getenv("STOCKSYMBOL")
    except:
        print("Could not get stock symbol")
        
    try:
        os.environ['NDAYS'] = "3"
        nDays = os.getenv("NDAYS")
    except:
        print("Could not get days to look up")
        
    scrape_json(stockSymbol, nDays)
    

def main():
    #getUserRequest()
    getEnvRequest()

if __name__ == "__main__":
    main()
