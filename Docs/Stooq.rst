.. _Stooq:

Stooq
=========

Stooq is an odd one. This website looks about 20 years old but it is a real hidden gem.
By searching a ticker and going to ‘historical data’, you can get historical data going back over 20 years.
You can also download a .csv. Unfortunately, there is no API access but its a great resource nonetheless.

.. note::
    Refer to `Stooq Jupyter Notebook <https://github.com/tatsath/FinAILabDatasets/blob/main/Docs/JupyterNotebooks/stooq.ipynb>`_ for more details.

Table of Contents
-----------------

- `Installation`_
- `Usage`_
- `Historical Price and Volume for 1 Stock`_
- `Adding Time Periods`_
- `Mutual Funds`_

Installation
------------

Install with pip:

.. code:: ipython3

    pip install pandas-datareader

Usage
-----

Import all necessary libraries:

.. code:: ipython3

    import pandas as pd
    import numpy as np
    import pandas_datareader.data as web
    from datetime import datetime

.. note::
    Replace the ticker variable to whatever you would like from the `Stooq Website <https://stooq.com/q/?s=btc.v?>`_

Historical Price and Volume for 1 Stock
---------------------------------------

Gets the OHLCV for the given ``ticker``.

.. code:: ipython3
    
    # adjust the variables below
    ticker = 'AAPL'

    df = web.DataReader(ticker, 'stooq')
    df

Adding Time Periods
-------------------

Extends the previous call by using ``start`` and ``end`` to denote a timeframe.

.. code:: ipython3

    # adjust the variables below
    ticker = 'AAPL'
    start = datetime(1990,1,1)
    end = datetime(2020,1,1)

    df = web.DataReader(ticker, 'stooq', start, end)
    df

Mutual Funds
---------------

Another example showing this method can be called for more than equities.

.. code:: ipython3

    mutual_fund = 'SPY'
    start = datetime(1990,1,1)
    end = datetime(2020,1,1)

    df = web.DataReader(mutual_fund, 'stooq', start, end)
    df
