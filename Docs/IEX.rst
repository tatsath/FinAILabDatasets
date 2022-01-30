.. _IEX:

.. note::
    Refer to `IEX Jupyter Notebook <https://github.com/tatsath/FinAILabDatasets/blob/main/Docs/JupyterNotebooks/IEX.ipynb>`_ for more details.

IEX
===

-  `Installation`_
-  `Usage`_
-  `Show all Functions`_
-  `Historical Price and Volume for 1 Stock`_
-  `Adding Time Periods or Frequency`_
-  `Stock Split and Dividends`_
-  `Sentiment and News`_
-  `Insider Trades`_`
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

.. note::
    This library will output a Pandas DataFrame when the function ends with "DF".
    Otherwise, they can easily be converted to a dataframe, as show in 
    the `Stream Realtime Data`_ section.

Import all necessary libraries:

.. code:: ipython3

    import pandas as pd
    import pyEX as p 
    import requests

Show all Functions
------------------

The following command shows all functions available, 
all of which follow the same structure as the examples below.

.. code:: ipython3

    [_ for _ in dir(p) if _.endswith('DF')]

Historical Price and Volume for 1 Stock
---------------------------------------

Outputs the OHLCV for the given ``ticker``.

.. code:: ipython3

    history = conn.chartDF(ticker)

Adding Time Periods or Frequency
--------------------------------

Changing the ``timeframe`` variable adjusts the time frame 
and frequency of the OHLCV data.

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

Sentiment and News
------------------

Outputs the headline, source, summary, URL and image of the given ``ticker``.

.. code:: ipython3

    news = conn.newsDF(ticker, count=10)

Insider Trades
--------------

.. warning:: 
    This feature requires a premium subscription

trades = conn.insiderTransactionsDF(ticker)

Stream Realtime Data
--------------------

Each invocation of this function outputs all current data available for the
``ticker``.

.. code:: ipython3

    ticker = 'GE'

    real_time = conn.quote(ticker)

    # convert to Pandas DataFrame
    real_time = pd.DataFrame(real_time, index = ['value']).T

