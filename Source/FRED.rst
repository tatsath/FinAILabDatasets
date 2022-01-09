.. _FRED:

FRED
=========
To Do:



To Do:
- Add more details from the website: https://github.com/mortada/fredapi
- Add more description into each of the component.
- Add the details about how to see the list of all tickers available for download in each section.
- Provide a link to the jupyter notebook for this.

Fetching the data
-----------------

-  `1. Historical Price and Volume for 1 Stock. <#1>`__
-  `2. Many Stocks <#2>`__
-  `3. Currencies <#3>`_
- `4. Crypto <#4>`_
- `5. Mutual Funds <#5>`_
- `6. Treasury <#6>`_


.. code:: ipython3

    import pandas_datareader as web
    import pandas as pd
    from matplotlib import pyplot as plt
    import seaborn as sns
    from datetime import datetime

    # specify time periods
    start = datetime(2010,1,1)
    end = datetime(2030,1,1)

    SP500 = web.DataReader('SP500','fred',start,end)

Historical Price for 1 Stock
----------------------------

.. code:: ipython3
    
    sns.set() #run this to overide matplotlib
    SP500['SP500'].plot(title='S&P 500 Price',figsize=(20, 6))

    #Use the below to save the chart as an image file
    plt.savefig('s&p500.png')

Many Stocks
-----------

.. code:: ipython3

    mkt_cap = web.DataReader(['WILLLRGCAPGR', 'WILLSMLCAP'], 'fred',start,end)
    mkt_cap.plot(title = 'Wilshire Large-Cap compared to Small-Cap', secondary_y = "DGS10", figsize=(20, 6))
    plt.tight_layout()
    
Currencies
---------------

.. code:: ipython3

    er = web.DataReader('AEXCHUS', 'fred',start,end)
    er.plot(title = 'Chinese Yuan Renminbi to U.S. Dollar Spot Exchange Rate', secondary_y = "DGS10", figsize=(20, 6))
    plt.tight_layout()

Crypto
---------------

.. code:: ipython3

    btc = web.DataReader('CBBTCUSD', 'fred',start,end)
    btc.plot(title = 'Bitcoin Price', secondary_y = "DGS10", figsize=(20, 6))
    plt.tight_layout()




Mutual Funds
---------------

.. code:: ipython3

    mf = web.DataReader('BOGZ1LM193064005Q', 'fred',start,end)
    mf.plot(title = 'Households; Corporate Equities and Mutual Fund Shares; Asset, Market Value Levels', secondary_y = "DGS10", figsize=(20, 6))
    plt.tight_layout()




Treasury Rates
---------------

.. code:: ipython3

    treasury = web.DataReader('TB3MS', 'fred',start,end)
    treasury.plot(title = '3-Month Treasury Bill Secondary Market Rate', secondary_y = "DGS10", figsize=(20, 6))
    plt.tight_layout()

