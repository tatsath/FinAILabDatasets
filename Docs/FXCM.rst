.. _FXCM:

FXCM
=========
FXCM provides a API to interact with its trading platform. Among others, it allows the retrieval of historical data as well as of streaming data. In addition, it allows to place different types of orders and to read out account information. The overall goal is to allow the implementation automated, algortithmic trading programs. fxcmpy.py is a Python wrapper package for that API.

.. note::
    Refer to `documentation <https://fxcm-api.readthedocs.io/en/latest/fxcmpy.html>`_ for more details.

Fetching the data
-----------------

.. code:: ipython3

    import numpy as np
    import yfinance as yf

Historical Price and Volume for 1 Stock
---------------------------------------

.. code:: ipython3

    import numpy as np
    import yfinance as yf
    ticker = 'GE'
    yf.download(ticker)

Adding Time Periods
-------------------

.. code:: ipython3

    yf.download(ticker, start = "2014-01-01", end = "2018-12-31")
    GE = yf.download(ticker, start = "2014-01-01", end = "2018-12-31")
    GE.info()


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



.. code:: ipython3

    yf.download(ticker, period = "ytd")
    yf.download(ticker, period = "1mo")
    yf.download(ticker, period = "5d")
    yf.download(ticker, period = "10y")


Frequency Setting
-----------------

.. code:: ipython3

    yf.download('GE',period='1mo',interval='1h')
    yf.download('GE',period='1mo',interval='5m')
    GE = yf.download('GE',period='5d',interval='5m')
    #Pre or post market data
    GE=yf.download('GE',prepost=True,period='5d',interval='5m')

Stock Split and dividends
-------------------------

.. code:: ipython3

    ticker = "AAPL"
    # action = True for dividend and Stock Split
    AAPL = yf.download(ticker, period="10y", actions = True)
    AAPL.head()

.. code:: ipython3

    AAPL[AAPL["Dividends"]>0]
    AAPL.loc["2019-08-05":"2019-08-15"].diff()
    AAPL[AAPL["Stock Splits"] > 0]
    ticker = ['GE', 'AAPL','FB']
     yf.download(ticker, period="5y")
.. code:: ipython3

     stock=yf.download(ticker, period="5y").Close


FInancial Indices
-----------------

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
----------

.. code:: ipython3

    #Tickers
    ticker1 = "EURUSD=X"
    ticker2 = "USDEUR=X"

.. code:: ipython3

    yf.download(ticker1,period='5y')

.. code:: ipython3

    yf.download(ticker2,period='5y')






Crypto
------

.. code:: ipython3

    #Tickers
    ticker1 = ["BTC-USD", "ETH-USD"]

.. code:: ipython3

    data = yf.download(ticker1,start='2019-08-01',end='2020-05-01')




Mutual Funds
------------

.. code:: ipython3

    #Tickers
    #20+Y Treasury Bobd ETF and Vivoldi Multi-Strategy Fund Class
    ticker1 = ["TLT", "OMOIX"]

.. code:: ipython3

    data = yf.download(ticker1,start='2019-08-01',end='2020-05-01')




Treasury Rates
---------------

.. code:: ipython3

    #10Y and 5Y Treasury Rates
    ticker1 = ["^TNX", "^FVX"]

.. code:: ipython3

    data = yf.download(ticker1,period="5y")


Stock Fundamentals
------------------

.. code:: ipython3

    ticker ="DIS"
    dis = yf.Ticker(ticker)

.. code:: ipython3

    dis.ticker


.. parsed-literal::

    'DIS'

.. code:: ipython3

    data=dis.history()

.. code:: ipython3

    ticker = ["MSFT","FB"]

.. code:: ipython3

    for i in ticker:
        df.loc["{}".format(i)] = pd.Series(yf.Ticker(i).info)

.. code:: ipython3

    df.info()

Import Financials
-----------------

.. code:: ipython3

    ticker ="DIS"
    dis = yf.Ticker(ticker)

.. code:: ipython3

    dis.balance_sheet

.. code:: ipython3

    dis.financials

.. code:: ipython3

    dis.cashflow

Put Call Option
---------------

.. code:: ipython3

    ticker ="DIS"
    dis = yf.Ticker(ticker)

.. code:: ipython3

    dis.option_chain()

.. code:: ipython3

    calls = dis.option_chain()[0]
    calls

.. code:: ipython3

    puts = dis.option_chain()[1]
    puts

 ### Stream Realtime Data

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
