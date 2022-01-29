.. _YahooFinance:

Yahoo Finance
=============

To Do:
- Add more description into each of the component.
- Add the details about how to see the list of all tickers available for download in each section.

Yahoo! Finance is a component of Yahoo’s network. It is the most widely used business news website in the United States, featuring stock quotes, press announcements, financial reports, and original content, as well as financial news, data, and commentary. They provide market data, fundamental and option data, market analysis, and news for cryptocurrencies, fiat currencies, commodities futures, equities, and bonds, as well as fundamental and option data, market analysis, and news.

Refer to `Yahoo Finance Jupyter Notebook <https://github.com/tatsath/FinAILabDatasets/blob/main/Docs/JupyterNotebooks/yfinance.ipynb>`_ for more details


Table of Contents
-----------------
-  `Installation`_
-  `Usage`_
-  `Historical Price and Volume for 1 Stock`_
-  `Adding Time Periods`_
-  `Frequency Setting`_
-  `Stock Split and Dividends`_
-  `Importing Many Stocks`_
-  `Financial Indices`_
-  `Currencies`_
-  `Cryptocurrencies`_
-  `Mutual Funds`_
-  `Treasury Rates`_
-  `Stock Fundamentals`_
-  `Financials`_
-  `Put Call Options`_
-  `Stream Realtime Data`_

Installation
------------

Install yfinance using pip:

.. code:: ipython3

    pip install yfinance --upgrade --no-cache-dir

.. note::
    To install yfinance using conda, see `this <https://anaconda.org/ranaroussi/yfinance>`_

Usage
-----

.. note::
    YFinance automatically uses Pandas DataFrames.

Import all necessary libraries:

.. code:: ipython3

    import numpy as np
    import yfinance as yf

Historical Price and Volume for 1 Stock
---------------------------------------

Outputs a Pandas DataFrame containing the values for 
open, high, low, close, and volume (OHLCV) of an equity.

.. code:: ipython3

    ticker = 'GE'
    yf.download(ticker)

Adding Time Periods
-------------------

Uses ``start`` and ``end`` to denote a time period to get the data from above between.

.. code:: ipython3

    yf.download(ticker, start = "2014-01-01", end = "2018-12-31")
    GE = yf.download(ticker, start = "2014-01-01", end = "2018-12-31")
    GE.info()

Output structure:

.. parsed-literal::

    <class 'pandas.core.frame.DataFrame'>
    DatetimeIndex: 1257 entries, 2014-01-02 to 2018-12-28
    Data columns (total 6 columns):
    Open         1257 non-null float64
    High         1257 non-null float64
    Low          1257 non-null float64
    Close        1257 non-null float64
    Adj Close    1257 non-null float64
    Volume       1257 non-null int64
    dtypes: float64(5), int64(1)
    memory usage: 68.7 KB

Alternative, static time periods:

.. code:: ipython3

    yf.download(ticker, period = "ytd")
    yf.download(ticker, period = "1mo")
    yf.download(ticker, period = "5d")
    yf.download(ticker, period = "10y")


Frequency Setting
-----------------

Outputs a similar Pandas DataFrame that breaks the OHLCV down into smaller 
minute or hour intervals.


.. code:: ipython3

    yf.download('GE',period='1mo',interval='1h')
    yf.download('GE',period='1mo',interval='5m')
    GE = yf.download('GE',period='5d',interval='5m')

You can even get pre and post market data using ``prepost``:

.. code:: ipython3

    GE=yf.download('GE',prepost=True,period='5d',interval='5m')

Stock Split and Dividends
-------------------------

Gets the quarterly dividend data for the given ``ticker``.

.. code:: ipython3

    ticker = "AAPL"
    # action = True for dividend and Stock Split
    AAPL = yf.download(ticker, period="10y", actions = True)
    AAPL.head()

You can use Pandas to narrow the data down by date or other 
features, such as stock splits.

.. code:: ipython3

    AAPL[AAPL["Dividends"]>0]
    AAPL.loc["2019-08-05":"2019-08-15"].diff()
    AAPL[AAPL["Stock Splits"] > 0]

Importing Many Stocks
---------------------

Use an array to get data on more than one stock.

.. code:: ipython3

    ticker = ['GE', 'AAPL','FB']
    yf.download(ticker, period="5y")

.. code:: ipython3

    stock=yf.download(ticker, period="5y").Close


Financial Indices
-----------------

Getting OHLCV data on multiple indices with the ``download`` function.

.. code:: ipython3

    index = ['^DJI', '^GSPC']

.. code:: ipython3

    stock = yf.download(index,period='10y').Close


.. code:: ipython3

    #Total Return
    index = ['^DJITR', '^SP500TR']

.. code:: ipython3

    indexes = yf.download(index,period='10y').Close



Currencies
---------------

Getting currency OHLCV data with the ``download`` function.

.. code:: ipython3

    #Tickers
    ticker1 = "EURUSD=X"
    ticker2 = "USDEUR=X"

.. code:: ipython3

    yf.download(ticker1,period='5y')

.. code:: ipython3

    yf.download(ticker2,period='5y')






Cryptocurrencies
----------------

Getting crypto OHLCV data with the ``download`` function.

.. code:: ipython3

    #Tickers
    ticker1 = ["BTC-USD", "ETH-USD"]

.. code:: ipython3

    data = yf.download(ticker1,start='2019-08-01',end='2020-05-01')




Mutual Funds
---------------

Getting mutual fund data with the ``download`` function.

.. code:: ipython3

    #Tickers
    #20+Y Treasury Bobd ETF and Vivoldi Multi-Strategy Fund Class
    ticker1 = ["TLT", "OMOIX"]

.. code:: ipython3

    data = yf.download(ticker1,start='2019-08-01',end='2020-05-01')




Treasury Rates
---------------

Getting treasury rates with the ``download`` function.

.. code:: ipython3

    #10Y and 5Y Treasury Rates
    ticker1 = ["^TNX", "^FVX"]

.. code:: ipython3

    data = yf.download(ticker1,period="5y")


Stock Fundamentals
------------------

To get fundamentals, use the ``Ticker`` object to instantiate new 
values.

.. code:: ipython3

    ticker ="DIS"
    dis = yf.Ticker(ticker)

Simply list the current ticker

.. code:: ipython3

    dis.ticker

.. parsed-literal::

    'DIS'

Outputs 150+ features on the ticker, including:
``sector``, ``website``, ``ebitda``, ``targetLowPrice``, ``currentRatio``, 
``currentPrice``, ``debtToEquity``, and ``totalRevenue``.

.. code:: ipython3

    data=dis.info

Summary of the information from the ``Ticker`` object.

.. code:: ipython3

    ticker = ["MSFT","FB"]

.. code:: ipython3

    for i in ticker:
        df.loc["{}".format(i)] = pd.Series(yf.Ticker(i).info)

.. code:: ipython3

    df.info()

Financials
----------

Designate your desired ticker.

.. code:: ipython3

    ticker ="DIS"
    dis = yf.Ticker(ticker)

Gets the balance sheet.

.. code:: ipython3

    dis.balance_sheet

Gets the income statement.

.. code:: ipython3

    dis.financials

Gets the statement of cash flows.

.. code:: ipython3

    dis.cashflow

Put Call Options
----------------

.. note:: 
    This output does not default to a Pandas DataFrame.

Designate your desired ticker.

.. code:: ipython3

    ticker = "DIS"
    dis = yf.Ticker(ticker)

Gets the ``call``, ``contractSymbol``, ``lastTradeDate``, ``strike``, 
``lastPrice``, ``bid``, and ``ask``.

.. code:: ipython3

    dis.option_chain()

.. code:: ipython3

    calls = dis.option_chain()[0]
    calls

.. code:: ipython3

    puts = dis.option_chain()[1]
    puts

Stream Realtime Data
--------------------

Continuously gets the latest data in 1 minute intervals.

.. code:: ipython3

    import time

.. code:: ipython3

    ticker1 ="EURUSD=X"
    data = yf.download(ticker1,interval = '1m', period='1d')
    print(data.index[-1], data.iloc[-1,3])
    #Every 5 second data corresponding to 5 seconds
    while True:
        time.sleep(5)
        data = yf.download(ticker1,interval = '1m', period='1d')
        print(data.index[-1], data.iloc[-1,3])
