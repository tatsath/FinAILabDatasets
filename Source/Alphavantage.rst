.. _Alphavantage:

Alphavantage
============

Alpha Vantage provides enterprise-grade financial market data through a set of powerful and developer-friendly APIs. To set up this environment you will need to have an API key, it can be straightly taken from the documentation here.

To do:
Add all the details:
https://analyticsindiamag.com/top-python-libraries-to-get-historical-stock-data-with-code/
https://medium.com/codex/alpha-vantage-an-introduction-to-a-highly-efficient-free-stock-api-6d17f4481bf
https://github.com/RomelTorres/alpha_vantage

Fetching the data
-----------------

-  `1. Historical Price and Volume for 1 Stock. <#1>`_
-  `2. Time Periods <#2>`_
-  `3. Frequency <#3>`_
-  `4. Split and Dividends <#4>`_
-  `5. Many Stocks <#5>`_
-  `6. Finanical Indices <#6>`_
-  `7. Currencies <#7>`_
- `8. Crypto <#8>`_
- `9. Mutual Funds <#9>`_
- `10. Treasury <#10>`_
- `11. Stock Fundamentals <#11>`_
- `12.   Financials <#12>`_
- `13. Put Call Options <#13>`_
- `14. Stream Real  Time Data <#14>`_
- `15. Economic Indicators <#15>`_
- `16. Technical Indicators <#16>`_

.. code:: ipython3

    from alpha_vantage.timeseries import TimeSeries
    import pandas as pd
    import time
    import requests
    from io import BytesIO

Historical Price and Volume for 1 Stock
---------------------------------------

.. code:: ipython3

    data = {
    "function": "DIGITAL_CURRENCY_DAILY", # WEEKLY, MONTHLY possible
    "symbol": "ETH",
    "market": 'CNY',
    "apikey": key
    }
    r = requests.get(url, params=data)
    data = r.json()
    crypto_df = pd.DataFrame(data['Time Series (Digital Currency Daily)']).T.reset_index()
    crypto_df = crypto_df.rename(columns={"index": "Date"})
    crypto_df['Date'] = pd.to_datetime(crypto_df['Date'])

Adding Time Periods
-------------------

.. code:: ipython3

    weekly = {
    "function": "DIGITAL_CURRENCY_WEEKLY", # WEEKLY, MONTHLY possible
    "symbol": "ETH",
    "market": 'CNY',
    "apikey": key
    }

    monthly = {
    "function": "DIGITAL_CURRENCY_MONTHLY", # WEEKLY, MONTHLY possible
    "symbol": "ETH",
    "market": 'CNY',
    "apikey": key
    }

Frequency Setting
-----------------

.. code:: ipython3

    ticker = 'TSLA'
    interval = '1min'
    api_key = key

    api_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval={interval}&apikey={api_key}'
    raw_df = requests.get(api_url).json()
    df = pd.DataFrame(raw_df[f'Time Series ({interval})']).T
    df = df.rename(columns = {'1. open': 'open', '2. high': 'high', '3. low': 'low', '4. close': 'close', '5. volume': 'volume'})
    for i in df.columns:
        df[i] = df[i].astype(float)
    df.index = pd.to_datetime(df.index)
    df = df.iloc[::-1]
    df.tail()

Stock Split and dividends
-------------------------

.. code:: ipython3

    ticker = "IBM"
    url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol='+ticker+'&apikey={key}'
    r = requests.get(url)
    data = r.json()
    dividends = pd.DataFrame(data, index = ['Values'])
    dividends = dividends[['DividendPerShare', 'DividendYield', 'DividendDate', 'ExDividendDate']].T

Financial Indices
-----------------

.. code:: ipython3

    # premium feature, NOT FULLY TESTED
    index = "DJI" # FCHI, IXIC, ...
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol='+index+'&outputsize=full&apikey={key}'
    r = requests.get(url)
    data = r.json()


Currencies
---------------

.. code:: ipython3

    # Currency list: https://www.alphavantage.co/physical_currency_list/
    currency_a = 'EUR'
    currency_b = 'USD'
    interval = '5min' # 1min, 5min, 15min, 30min, 60min
    url = 'https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol=EUR&to_symbol=USD&interval=5min&apikey=demo'
    r = requests.get(url)
    data = r.json()

Crypto
---------------

.. code:: ipython3

    ticker = 'ETH'
    url = 'https://www.alphavantage.co/query?function=CRYPTO_INTRADAY&symbol='+ticker+'&market=USD&interval=5min&apikey={key}'
    r = requests.get(url)
    data = r.json()




Mutual Funds
---------------

.. code:: ipython3

    ticker = 'OMOIX'
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+ticker+'&apikey={key}'
    r = requests.get(url)
    data = r.json()




Treasury Rates
---------------

.. code:: ipython3

    maturity = '10year' # 3month, 5year, 10year, 30year
    interval = 'daily' # weekly, monthly
    url = 'https://www.alphavantage.co/query?function=TREASURY_YIELD&interval='+interval+'&maturity='+maturity+'&apikey={key}'
    r = requests.get(url)
    data = r.json()


Stock Fundamentals
------------------

.. code:: ipython3

    ticker = "IBM"
    url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol='+ticker+'&apikey={key}'
    r = requests.get(url)
    data = r.json()

Import Financials
-----------------

.. code:: ipython3

    document = 'INCOME_STATEMENT' # BALANCE_SHEET, CASH_FLOW
    url = 'https://www.alphavantage.co/query?function='+document+'&symbol=IBM&apikey=demo'
    r = requests.get(url)
    data = r.json()

Stream Realtime Data
--------------------

.. code:: ipython3

    def get_live_updates(symbol):
        api_key = key
        api_url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'
        raw_df = requests.get(api_url).json()
        attributes = {'attributes':['symbol', 'open', 'high', 'low', 'price', 'volume', 'latest trading day', 'previous close', 'change', 'change percent']}
        attributes_df = pd.DataFrame(attributes)
        values = []
        for i in list(raw_df['Global Quote']):
            values.append(raw_df['Global Quote'][i])
        values_dict = {'values':values}
        values_df = pd.DataFrame(values).rename(columns = {0:'values'})
        frames = [attributes_df, values_df]
        df = pd.concat(frames, axis = 1, join = 'inner').set_index('attributes')
        return df

    ibm_updates = get_live_updates('IBM')
    ibm_updates

Economic Indicators
-------------------

.. code:: ipython3

    gdp = {
        "function": "REAL_GDP",
        "interval": "annual", # quarterly
        "apikey": key
    }
    treasury_yield = {
        "function": "TREASURY_YIELD",
        "interval": "weekly", # daily, monthly
        "maturity": "3month", # OPTIONAL 5year, 10year, 30year
        "apikey": key
    }
    federal_funds_rate = {
        "function": "FEDERAL_FUNDS_RATE",
        "interval": "weekly", # daily, monthly
        "apikey": key
    }
    cpi = {
        "function": "CPI",
        "interval": "weekly", # daily, monthly
        "apikey": key
    }
    inflation = {
        "function": "INFLATION",
        "interval": "weekly", # daily, monthly
        "apikey": key
    }
    consumer_sentiment = {
        "function": "CONSUMER_SENTIMENT",
        "apikey": key
    }
    unemployment = {
        "function": "UNEMPLOYMENT",
        "apikey": key
    }
    r = requests.get(url, params=unemployment) # REPLACE 'params' with desired dict
    data = r.json()
    df = pd.DataFrame(data['data'])
    df = crypto_df.set_index("date")

Technical Indicators
--------------------

.. code:: ipython3

    popular_ti = {
        "function": "ADX", # REPLACE: EMA, RSI, ADX, SMA
        "symbol": "IBM",
        "interval": "weekly",
        "time_period": "10",
        "series_type": "open",
        "apikey": key
    }

    r = requests.get(url, params=popular_ti)
    data = r.json()