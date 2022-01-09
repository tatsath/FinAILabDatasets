.. _Stooq:

Stooq
=========

Stooq is an odd one. This website looks about 20 years old but it is a real hidden gem.
By searching a ticker and going to ‘historical data’, you can get historical data going back over 20 years.
You can also download a .csv. Unfortunately there is no API access but its a great resource nonetheless.

To Do:

- Add the details about how to see the list of all tickers available for download in each section.
- Provide a link to the jupyter notebook for this.

Fetching the data
-----------------

-  `1. Historical Price and Volume for 1 Stock. <#1>`__
-  `2. Time Periods <#2>`__
- `3. Mutual Funds <#3>`_



Replace the ticker variable to whatever you would like from: https://stooq.com/q/?s=btc.v

.. code:: ipython3

    import pandas as pd
    import numpy as np
    import pandas_datareader.data as web
    from datetime import datetime

Historical Price and Volume for 1 Stock
---------------------------------------

.. code:: ipython3
    
    # adjust the variables below
    ticker = 'AAPL'

    df = web.DataReader(ticker, 'stooq')
    df

Adding Time Periods
-------------------

.. code:: ipython3

    # adjust the variables below
    ticker = 'AAPL'
    start = datetime(1990,1,1)
    end = datetime(2020,1,1)

    df = web.DataReader(ticker, 'stooq', start, end)
    df

Mutual Funds
---------------

.. code:: ipython3

    ticker = 'SPY'
    start = datetime(1990,1,1)
    end = datetime(2020,1,1)

    df = web.DataReader(ticker, 'stooq', start, end)
    df
