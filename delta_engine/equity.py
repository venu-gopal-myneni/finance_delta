import yfinance as yf
import pandas as pd



def get_daily(start_date:str,end_date:str,symbol:str,country:str) -> pd.DataFrame:
    """
    :Parameters:
        period : str
            Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
            Either Use period parameter or use start and end
        interval : str
            Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
            Intraday data cannot extend last 60 days
        start_date: str
            Download start date string (YYYY-MM-DD) or _datetime, inclusive.
            E.g. for start="2020-01-01", the first data point will be on "2020-01-01"
        end_date: str
            Download end date string (YYYY-MM-DD) or _datetime, exclusive.
            E.g. for end="2023-01-01", the last data point will be on "2022-12-31"
        symbol: str
            Ticker symbols
            E.g. INFY,MSFT etc
        country: str
            Country code. Default is for USA
            E.g. IND
    """
    if country == "IND":
        ticker = yf.Ticker(f"{symbol}.ns")

    else:
        ticker=yf.Ticker(symbol)
    return ticker.history(start=start_date,end=end_date)

if __name__ =="__main__":
    print(get_daily("2023-01-01","2023-01-10","INFY","IND"))