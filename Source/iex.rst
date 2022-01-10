.. _iex:

IEX
=============

Fetching the data
-----------------

-  `1. Show all Functions <#1>`__
-  `2. Historical Price and Volume for 1 Stock <#2>`__
-  `3. Time Periods or Frequency<#3>`__
-  `4. Split and Dividends <#4>`__
-  `5. News <#5>`__
-  `6. Stream Real  Time Data <#6>`__

.. code:: ipython3

    import pandas as pd
    import pyEX as p 
    import requests

Show all functions
------------------

The following command shows all functions available, all of which follow the same structure as the examples below

- `Some require a premium substription`

.. code:: ipython3

    [_ for _ in dir(p) if _.endswith('DF')]

Historical Price and Volume for 1 Stock
---------------------------------------

.. code:: ipython3

    history = conn.chartDF(ticker)
    history



Adding Time Periods or Frequency
--------------------------------

.. code:: ipython3

    timeframe = '5d' # up to 15 years, or minute-by-minute for the last 30 days
    history = conn.chartDF(ticker, timeframe=timeframe)
    history

Stock Split and dividends
-------------------------

.. code:: ipython3

    # premium feature
    timeframe = '6m'
    dividends = conn.dividendsDF(ticker)
    dividends


News
----

.. code:: ipython3

    news = conn.newsDF(ticker, count=10)
    news

Stream Realtime Data
--------------------

.. code:: ipython3

    ticker = 'GE'

    real_time = conn.quote(ticker)
    real_time = pd.DataFrame(real_time, index = ['value']).T
    real_time
