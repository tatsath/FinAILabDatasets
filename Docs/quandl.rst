.. _quandl:

Quandl
=========

Quandl has many data sources to get different types of stock market data. However, some are free and some are paid. Wiki is the free data source of Quandl to get the data of the end of the day prices of 3000+ US equities. It is curated by Quandl community and also provides information about the dividends and split.

Quandl also provides paid data source of minute and lower frequencies.

To get the stock market data, you need to first install the quandl module if it is not already installed using the pip command as shown below.

You need to get your own API Key from quandl to get the stock market data using the below code. If you are facing issue in getting the API key then you can refer to this link.

After you get your key, assign the variable QUANDL_API_KEY with that key. Then set the start date, end date and the ticker of the asset whose stock market data you want to fetch.

The quandl get method takes this stock market data as input and returns the open, high, low, close, volume, adjusted values and other information.


To do- Add details from following sites
- https://blog.quantinsti.com/stock-market-data-analysis-python/
- https://towardsdatascience.com/python-i-have-tested-quandl-api-and-how-to-get-real-estates-economics-data-in-one-line-of-code-a13806ca9bb
- https://medium.datadriveninvestor.com/financial-data-431b75975bb#cc62
- Add more description into each of the component.
- Add the details about how to see the list of all tickers available for download in each section.
- Provide a link to the jupyter notebook for this.

Refer to `Quandl Jupyter Notebook <https://github.com/tatsath/FinAILabDatasets/blob/main/Docs/JupyterNotebooks/quandl.ipynb>`_ for more details.

Table of Contents
-----------------

- `Installation`_
- `Usage`_ 
- `Historical Price and Volume for 1 Stock`_
- `Adding Time Periods`_
- `Dividends`_
- `Cryptocurrencies`_
- `Mutual Funds`_
- `Treasury Rates`_
- `Stock Fundamentals`_
- `Futures and Options`_

Installation
------------

Install with pip:

.. code:: ipython3

    pip install quandl

Usage
-----

.. note::
    Before working with this API, you will need to obtain
    a key from `Nasdaq Data Link <https://data.nasdaq.com/users/login>`_

Quandl is the library used for accessing the `Nasdaq Data Link <https://data.nasdaq.com/search>`_ 
database, so all of the queries below follow a similar pattern that can be reproduced with 
any of the ID codes from the database.

Import all necessary libraries:

.. code:: ipython3

    import quandl
    import pandas as pd 
    import numpy as np 
    from datetime import datetime
    from matplotlib import pyplot as plt
    import seaborn as sns

.. code:: ipython3

    # To get your API key, sign up for a free Quandl account.
    # Then, you can find your API key on Quandl account settings page.
    QUANDL_API_KEY = 'REPLACE-THIS-TEXT-WITH-A-REAL-API-KEY'


    # This is to prompt you to change the Quandl Key
    if QUANDL_API_KEY == 'REPLACE-THIS-TEXT-WITH-A-REAL-API-KEY':
        raise Exception("Please provide a valid Quandl API key!")

.. code:: ipython3
    
    quandl.ApiConfig.api_key = QUANDL_API_KEY

Historical Price and Volume for 1 Stock
---------------------------------------

Outputs the OHLCV, as well as dividend data and adjusted OHLCV for the given ``ticker``.

.. code:: ipython3

    # Set the start and end date
    start_date = '1990-01-01'
    end_date = '2018-03-01'

    # Set the ticker name
    ticker = 'AMZN'
                
.. code:: ipython3

    data = quandl.get('WIKI/'+ticker)


Adding Time Periods
-------------------

Uses ``start`` and ``end`` to denote a time period for the query.

.. code:: ipython3

    data = quandl.get('WIKI/'+ticker,
              start_date=start,
              end_date=end)
    data.head()


Dividends
---------

Outputs the Dividend and Read Dividend.

.. code:: ipython3

    sp = quandl.get('YALE/SPCOMP', start_date='2015-04-01', end_date='2021-10-01')
    sp[['Dividend', 'Real Dividend']]


Cryptocurrencies
---------------

Outputs the date and price of bitcoin.

.. code:: ipython3

    # bitcoin price
    btc = quandl.get('BCHAIN/MKPRU', start_date='2020-12-29', end_date='2021-12-29')
    btc

Mutual Funds
---------------

Plots the mutual fund assests to GDP from the ``start_date`` to the ``end_date``.

.. code:: ipython3

    # Mutual Fund Assets to GDP for World
    mf = quandl.get('FRED/DDDI071WA156NWDB', start_date='1980-04-01', end_date='2020-10-01')
    mf.plot(title = 'Mutual Fund Assets to GDP', figsize=(20, 6))

Treasury Rates
---------------

Plots the real long-term treasury rates from the ``start_date`` to the ``end_date``.

.. code:: ipython3

    mf = quandl.get('USTREASURY/REALLONGTERM', start_date='2000-04-01', end_date='2020-10-01')
    mf.plot(title = 'Treasury Real Long-Term Rates', figsize=(20, 6))


Stock Fundamentals
------------------

Outputs earnings, CPI, price, long interest rate, and PE ratio.

.. code:: ipython3

    sp = quandl.get('YALE/SPCOMP', start_date='2015-04-01', end_date='2021-10-01')
    sp

Futures and Options
-------------------

Outputs various long, short, and spread data.

.. code:: ipython3
    
    fo = quandl.get('CFTC/1170E1_FO_ALL', start_date='2015-04-01', end_date='2021-10-01')
    fo

