.. _Alphavantage:

Alphavantage
============

Alpha Vantage provides enterprise-grade financial market data through a set of powerful and developer-friendly APIs. To set up this environment you will need to have an API key, it can be straightly taken from the documentation here.


.. note::
    Refer to `Alphavantage Jupyter Notebook <https://github.com/tatsath/FinAILabDatasets/blob/main/Docs/JupyterNotebooks/Alphavantage.ipynb>`_ for more details.

Table of Contents
-----------------

-  `Installation`_
-  `Usage`_
-  `Symbol Search`_
-  `Historical Price and Volume for 1 Stock`_
-  `Adding Time Periods`_
-  `Frequency Setting`_
-  `Stock Splits and Dividends`_
-  `Foreign Exchange`_
-  `Cryptocurrencies`_
-  `Mutual Funds`_
-  `Treasury Rates`_
-  `Stock Fundamentals`_
-  `Financials`_
-  `Stream Realtime Data`_
-  `Economic Indicators`_
-  `Technical Indicators`_
-  `Sector Performance`_

.. _Jupyter Notebook: JupyterNotebooks/Alphavantage.ipynb

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

Import all necessary libraries:

.. code:: ipython3

    from alpha_vantage.timeseries import TimeSeries
    import pandas as pd
    import time
    import requests
    from io import BytesIO

.. code:: ipython3

    key = 'insert your unique key here'

Symbol Search
-------------

For checking to see if the equity, commodity, mutual fund, etc. you want is available on Alphavantage:

.. note::
    This example, and the following, also demonstrate how to convert an Alphavantage dictionary
    into a Pandas DataFrame for easier data analysis.

.. code:: ipython3

    symbol_to_search = 'TSLA'
    url = 'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords='+symbol_to_search+'&apikey={key}'
    r = requests.get(url)
    data = r.json()
    data = pd.DataFrame(data['bestMatches'])

Historical Price and Volume for 1 Stock
---------------------------------------




.. note::
    See the data dictionary for adjustments to time frame. Daily, weekly, and monthly time frames are available for equities.

.. code:: ipython3

    data = {
        "function": "TIME_SERIES_DAILY", # WEEKLY, MONTHLY possible
        "symbol": "TSLA",
        "apikey": key
    }
    r = requests.get(url, params=data)
    data = r.json()
    data = pd.DataFrame(data['Time Series (Daily)']).T

Adding Time Periods
^^^^^^^^^^^^^^^^^^^

Shown below are the adjusted dictionaries for weekly and monthly time frames.

.. code:: ipython3

    weekly = {
        "function": "DIGITAL_CURRENCY_WEEKLY",
        "symbol": "ETH",
        "market": 'CNY',
        "apikey": key
    }

    monthly = {
        "function": "DIGITAL_CURRENCY_MONTHLY",
        "symbol": "ETH",
        "market": 'CNY',
        "apikey": key
    }

Frequency Setting
-----------------

Outputs a similar Pandas DataFrame that breaks the OHLCV down into 1 minute intervals.

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

Stock Splits and Dividends
-------------------------

Outputs a Pandas DataFrame with the DPS, Yield, Dividend Date and ExDate for the given ticker.

.. code:: ipython3

    ticker = "IBM"
    url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol='+ticker+'&apikey={key}'
    r = requests.get(url)
    data = r.json()
    dividends = pd.DataFrame(data, index = ['Values'])
    dividends = dividends[['DividendPerShare', 'DividendYield', 'DividendDate', 'ExDividendDate']].T

Financial Indices
-----------------

.. note::
    This feature requires a premium subscription.

.. code:: ipython3

    index = "DJI" # FCHI, IXIC, ...
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol='+index+'&outputsize=full&apikey={key}'
    r = requests.get(url)
    data = r.json()


Foreign Exchange
----------------

Outputs a dictionary with the exchange rate's OHLC values on the given time interval.

.. code:: ipython3

    # Currency list: https://www.alphavantage.co/physical_currency_list/
    currency_a = 'EUR'
    currency_b = 'USD'
    interval = '5min' # 1min, 5min, 15min, 30min, 60min
    url = 'https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol=EUR&to_symbol=USD&interval=5min&apikey=demo'
    r = requests.get(url)
    data = r.json()

Alternatively, you can use the ``ForeignExchange`` library.

.. code:: ipython3

    from alpha_vantage.foreignexchange import ForeignExchange
    from pprint import pprint
    cc = ForeignExchange(key='YOUR_API_KEY')
    # There is no metadata in this call
    data, _ = cc.get_currency_exchange_rate(from_currency='BTC',to_currency='USD')
    pprint(data)

Cryptocurrencies
----------------

There are multiple ways to view data on cryptocurrencies.

The first is using Alphavantage's API request which returns the OHLCV for the given crypto:

.. code:: ipython3

    ticker = 'ETH'
    url = 'https://www.alphavantage.co/query?function=CRYPTO_INTRADAY&symbol='+ticker+'&market=USD&interval=5min&apikey={key}'
    r = requests.get(url)
    data = r.json()

Another way is to import the ``CryptoCurrencies`` library, which allows for easy plotting:

.. code:: ipython3

    from alpha_vantage.cryptocurrencies import CryptoCurrencies
    import matplotlib.pyplot as plt

    cc = CryptoCurrencies(key='YOUR_API_KEY', output_format='pandas')
    data, meta_data = cc.get_digital_currency_daily(symbol='BTC', market='CNY')
    data['4b. close (USD)'].plot()
    plt.tight_layout()
    plt.title('Daily close value for bitcoin (BTC)')
    plt.grid()
    plt.show()

Lastly, we can view the excahnge rates for cryptos:

.. code:: ipython3

    data = {
    "function": "CURRENCY_EXCHANGE_RATE", # WEEKLY, MONTHLY possible
    "from_currency": "ETH",
    "to_currency": 'USD',
    "apikey": key
    }
    r = requests.get(url, params=data)
    data = r.json()

Mutual Funds
---------------

Outputs a dictionary of the OHLCV values for the given mutual fund.

.. code:: ipython3

    ticker = 'OMOIX'
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+ticker+'&apikey={key}'
    r = requests.get(url)
    data = r.json()

Treasury Rates
---------------

Outputs a dictionary of the daily, weekly, or monthly treasury rate.

.. code:: ipython3

    treasury_yield = {
        "function": "TREASURY_YIELD",
        "interval": "weekly", # daily, monthly
        "maturity": "3month", # OPTIONAL 5year, 10year, 30year
        "apikey": key
    }
    r = requests.get(url, params=treasury_yield)
    data = r.json()

Stock Fundamentals
------------------

Outputs a dictionary of various stock data, including: AssetType, Description,
Sector, Address, Market Cap, EBITDA, PE, EPS, RPS, Profit Margin, Moving Averages,
Revenue, and Beta.

.. code:: ipython3

    ticker = "IBM"
    url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol='+ticker+'&apikey={key}'
    r = requests.get(url)
    data = r.json()

Financials
----------

Outputs a dictionary containing the information for a company's balance sheet, cash flows, or income statement.

.. code:: ipython3

    document = 'INCOME_STATEMENT' # BALANCE_SHEET, CASH_FLOW
    url = 'https://www.alphavantage.co/query?function='+document+'&symbol=IBM&apikey=demo'
    r = requests.get(url)
    data = r.json()

Stream Realtime Data
--------------------

Each invocation of the below function will produce the most up-to-date data on the given symbol.

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

Below are a few dictionaries that contain different economic indicators that can be plugged
into the JSON request at the very bottom.

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

Below is the aforementioned JSON request, where you will replace the ``params`` variable.

.. code:: ipython3

    r = requests.get(url, params=unemployment) # REPLACE 'params' with desired dict
    data = r.json()
    df = pd.DataFrame(data['data'])
    df = crypto_df.set_index("date")

Technical Indicators
--------------------

Below is the JSON request approach to getting data on various technical indicators.

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

Alternatively, you can use the ``TechIndicators`` library to achieve similar results.

.. code:: ipython3

    from alpha_vantage.techindicators import TechIndicators
    import matplotlib.pyplot as plt

    ti = TechIndicators(key='YOUR_API_KEY', output_format='pandas')
    data, meta_data = ti.get_bbands(symbol='MSFT', interval='60min', time_period=60)
    data.plot()
    plt.title('BBbands indicator for  MSFT stock (60 min)')
    plt.show()

Sector Performance
------------------

Lastly, Alphavantage allows you to use the ``SectorPerformances`` library to
view the realtime performance, by sector:

.. code:: ipython3

    from alpha_vantage.sectorperformance import SectorPerformances
    import matplotlib.pyplot as plt

    sp = SectorPerformances(key='YOUR_API_KEY', output_format='pandas')
    data, meta_data = sp.get_sector()
    data['Rank A: Real-Time Performance'].plot(kind='bar')
    plt.title('Real Time Performance (%) per Sector')
    plt.tight_layout()
    plt.grid()
    plt.show()
