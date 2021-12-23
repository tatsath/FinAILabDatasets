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



Fetching the data
---------------

-  `1. Historical Price and Volume for 1 Stock. <#1>`__
-  `2. Time Periods <#2>`__
-  `3. Frequency <#3>`__
-  `4. Split and Dividends <#4>`__
-  `5. Many Stocks <#5>`__
-  `6. Finanical Indices <#6>`__
-  `7. Currencies <#7>`_
- `8. Crypto <#8>`_
- `9. Mutual Funds <#9>`_
- `10. Treasury <#10>`_
- `11. Stock Fundamentals <#11>`_
- `12.   Financials <#12>`_
- `13. Put Call Options <#13>`_
- `14. Stream Real  Time Data <#14>`__

.. code:: ipython3

      import quandl


      # To get your API key, sign up for a free Quandl account.
      # Then, you can find your API key on Quandl account settings page.
      QUANDL_API_KEY = 'REPLACE-THIS-TEXT-WITH-A-REAL-API-KEY'


      # This is to prompt you to change the Quandl Key
      if QUANDL_API_KEY == 'REPLACE-THIS-TEXT-WITH-A-REAL-API-KEY':
      raise Exception("Please provide a valid Quandl API key!")

      # Set the start and end date
      start_date = '1990-01-01'
      end_date = '2018-03-01'


      # Set the ticker name
      ticker = 'AMZN'


      # Feth the data
      data = quandl.get('WIKI/'+ticker,
                    start_date=start_date,
                    end_date=end_date,
                    api_key=QUANDL_API_KEY)


      # Print the first 5 rows of the dataframe
data.head()



Historical Price and Volume for 1 Stock
----------

.. code:: ipython3
    import numpy as np
    import yfinance as yf
    ticker = 'GE'
    yf.download(ticker)

Adding Time Periods
----------

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
----------

.. code:: ipython3

    yf.download('GE',period='1mo',interval='1h')
    yf.download('GE',period='1mo',interval='5m')
    GE = yf.download('GE',period='5d',interval='5m')
    #Pre or post market data
    GE=yf.download('GE',prepost=True,period='5d',interval='5m')

Stock Split and dividends
----------

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
 ---------------

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

.. code:: ipython3

    #Tickers
    ticker1 = "EURUSD=X"
    ticker2 = "USDEUR=X"

.. code:: ipython3

    yf.download(ticker1,period='5y')

.. code:: ipython3

    yf.download(ticker2,period='5y')






Crypto
---------------

.. code:: ipython3

    #Tickers
    ticker1 = ["BTC-USD", "ETH-USD"]

.. code:: ipython3

    data = yf.download(ticker1,start='2019-08-01',end='2020-05-01')




Mutual Funds
---------------

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
---------------

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
---------------

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
