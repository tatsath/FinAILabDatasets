.. _Alphavantage:

Alphavantage
============

Alpha Vantage provides enterprise-grade financial market data through a set of powerful and developer-friendly APIs. To set up this environment you will need to have an API key, it can be straightly taken from the documentation here.

To do:
Add all the details:
https://analyticsindiamag.com/top-python-libraries-to-get-historical-stock-data-with-code/
https://medium.com/codex/alpha-vantage-an-introduction-to-a-highly-efficient-free-stock-api-6d17f4481bf
https://github.com/RomelTorres/alpha_vantage

.. warning::
    Links to JupyterNBs are currently not working.

Table of Contents
-----------------

-  `Link to the Jupyter Notebook <../JupyterNotebooks/Alphavantage.ipynb>`
-  `Installation`_
-  `Usage`_
-  `Symbol Search`_
-  `Historical Price and Volume for 1 Stock`_
-  `Adding Time Periods`_
-  `Frequency Setting`_
-  `Stock Split and Dividends`_
-  `Currencies`_
-  `Cryptocurrencies`_
-  `Mutual Funds`_
-  `Treasury Rates`_
-  `Stock Fundamentals`_
-  `Financials`_
-  `Stream Realtime Data`_
-  `Economic Indicators`_
-  `Technical Indicators`_

Installation
------------

.. note::
    Before working with this API, you will need to obtain
    a key from `AlphaVantage's Website <https://www.alphavantage.co>`_

To install the package use:

.. code:: ipython3

    pip install alpha_vantage 

Or install with pandas support

.. code:: ipython3

    pip install alpha_vantage pandas

Or install from the source

.. code:: ipython3

    git clone https://github.com/RomelTorres/alpha_vantage.git
    pip install -e alpha_vantage

Usage
-----

.. code:: ipython3

    from alpha_vantage.timeseries import TimeSeries
    import pandas as pd
    import time
    import requests
    from io import BytesIO

    key = 'insert your unique key here'

Symbol Search
-------------

.. code:: ipython3

    symbol_to_search = 'TSLA'
    url = 'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords='+symbol_to_search+'&apikey={key}'
    r = requests.get(url)
    data = r.json()
    data = pd.DataFrame(data['bestMatches'])
    
Historical Price and Volume for 1 Stock
---------------------------------------

Link to the `historic price and volume of one stock <../JupyterNotebooks/Alphavantage.ipynb#historical-price-and-volume-for-1-stock>`_ JupyterNB cell.

Adjust the symbol using the dictionary below

.. code:: ipython3

    data = {
    "function": "TIME_SERIES_DAILY", # WEEKLY, MONTHLY possible
    "symbol": "TSLA",
    "apikey": key
    }
    r = requests.get(url, params=data)
    data = r.json()
    data = pd.DataFrame(data['Time Series (Daily)']).T
    data

Adding Time Periods
^^^^^^^^^^^^^^^^^^^

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
Link to the `intraday data`_ JupyterNB cell.

.. _intraday data: JupyterNotebooks/Alphavantage.ipynb#Intraday-Data

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
Link to the `dividends`_ JupyterNB cell.

.. _dividends: JupyterNotebooks/Alphavantage.ipynb#Dividends

.. code:: ipython3

    ticker = "IBM"
    url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol='+ticker+'&apikey={key}'
    r = requests.get(url)
    data = r.json()
    dividends = pd.DataFrame(data, index = ['Values'])
    dividends = dividends[['DividendPerShare', 'DividendYield', 'DividendDate', 'ExDividendDate']].T

Financial Indices
-----------------
Link to the `financial indices`_ JupyterNB cell.

.. _financial indices: JupyterNotebooks/Alphavantage.ipynb#Indices

.. code:: ipython3

    # premium feature, NOT FULLY TESTED
    index = "DJI" # FCHI, IXIC, ...
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol='+index+'&outputsize=full&apikey={key}'
    r = requests.get(url)
    data = r.json()


Currencies
----------
Link to the `currency exchange`_ JupyterNB cell.

.. _currency exchange: JupyterNotebooks/Alphavantage.ipynb#Currency-Exchange

.. code:: ipython3

    # Currency list: https://www.alphavantage.co/physical_currency_list/
    currency_a = 'EUR'
    currency_b = 'USD'
    interval = '5min' # 1min, 5min, 15min, 30min, 60min
    url = 'https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol=EUR&to_symbol=USD&interval=5min&apikey=demo'
    r = requests.get(url)
    data = r.json()

Cryptocurrencies
----------------
Link to the `cryptocurrencies`_ JupyterNB cell.

.. _cryptocurrencies: JupyterNotebooks/Alphavantage.ipynb#Cryptocurrencies

.. code:: ipython3

    ticker = 'ETH'
    url = 'https://www.alphavantage.co/query?function=CRYPTO_INTRADAY&symbol='+ticker+'&market=USD&interval=5min&apikey={key}'
    r = requests.get(url)
    data = r.json()




Mutual Funds
---------------
Link to the `mutual funds`_ JupyterNB cell.

.. _mutual funds: JupyterNotebooks/Alphavantage.ipynb#Mutual-Funds

.. code:: ipython3

    ticker = 'OMOIX'
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+ticker+'&apikey={key}'
    r = requests.get(url)
    data = r.json()

Treasury Rates
---------------
Link to the `treasury yield`_ JupyterNB cell.

.. _treasury yield: JupyterNotebooks/Alphavantage.ipynb#Treasury-Yield

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

Financials
----------
Link to the `financials`_ JupyterNB cell.

.. _financials: JupyterNotebooks/Alphavantage.ipynb#Financials

.. code:: ipython3

    document = 'INCOME_STATEMENT' # BALANCE_SHEET, CASH_FLOW
    url = 'https://www.alphavantage.co/query?function='+document+'&symbol=IBM&apikey=demo'
    r = requests.get(url)
    data = r.json()

Stream Realtime Data
--------------------
Link to the `realtime data`_ JupyterNB cell.

.. _realtime data: JupyterNotebooks/Alphavantage.ipynb#Realtime-Data

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
Link to the `economic indicators`_ JupyterNB cell.

.. _economic indicators: JupyterNotebooks/Alphavantage.ipynb#Economic-Indicators

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
Link to the `technical indicators`_ JupyterNB cell.

.. _Technical Indicators: JupyterNotebooks/Alphavantage.ipynb#Technical-Indicators

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