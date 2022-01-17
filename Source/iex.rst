.. _IEX:

IEX
===

-  `Installation`_
-  `Usage`_
-  `Show all Functions`_
-  `Historical Price and Volume for 1 Stock`_
-  `Time Periods or Frequency`_
-  `Stock Split and Dividends`_
-  `News and Sentiment`_
-  `Stream Realtime Data`_


Installation 
------------

.. note::
    Before working with this API, you will need to obtain
    a key from `IEX Cloud <https://iexcloud.io/console/tokens/>`_

Install pyEX with pip:

.. code:: ipython3

    pip install pyEX

Usage
-----

.. code:: ipython3

    import pandas as pd
    import pyEX as p 
    import requests


Show all Functions
------------------

The following command shows all functions available, all of which follow the same structure as the examples below

.. code:: ipython3

    [_ for _ in dir(p) if _.endswith('DF')]

Historical Price and Volume for 1 Stock
---------------------------------------

.. code:: ipython3

    history = conn.chartDF(ticker)

Adding Time Periods or Frequency
--------------------------------

.. code:: ipython3

    timeframe = '5d' # up to 15 years, or minute-by-minute for the last 30 days
    history = conn.chartDF(ticker, timeframe=timeframe)

Stock Split and Dividends
-------------------------

.. warning:: 
    This feature requires a premium subscription

.. code:: ipython3

    timeframe = '6m'
    dividends = conn.dividendsDF(ticker)

News and Sentiment
------------------

.. code:: ipython3

    news = conn.newsDF(ticker, count=10)

Stream Realtime Data
--------------------

.. code:: ipython3

    ticker = 'GE'

    real_time = conn.quote(ticker)
    real_time = pd.DataFrame(real_time, index = ['value']).T

