.. _finviz:

FinViz
======

.. note:: 
	This library is ideal for fundamentals and sentiment analysis projects.


.. note::
    Refer to `FinViz Jupyter Notebook <https://github.com/tatsath/FinAILabDatasets/blob/main/Docs/JupyterNotebooks/finviz.ipynb>`_ for more details.

Table of Contents
-----------------

-  `Installation`_
-  `Usage`_
-  `Stock Fundamentals`_
-  `Ticker Description`_
-  `Multiple Tickers`_
-  `Sentiment and News`_
-  `Insider Trades`_

Installation
------------

Install with pip:

.. code:: ipython3

	pip install finvizfinance

Or install from github:

.. code:: ipython3

	git clone https://github.com/lit26/finvizfinance.git
	
Usage
-----

Import all necessary libraries:

.. code:: ipython3

	from finvizfinance.quote import finvizfinance
	import pandas as pd

.. code:: ipython3

	stock = finvizfinance('tsla')

Stock Fundamentals
------------------

Getting information (fundamentals, description, outer rating, stock news, inside trader) of an individual stock.

.. code:: ipython3

	chart = stock.ticker_charts()
	chart

.. code:: ipython3

	stock_fundament = stock.ticker_fundament()

Ticker Description
------------------

Outputs a brief description of the chosen stock. 'Tesla, Inc. designs, develops, manufactures, ...'

.. code:: ipython3

	description = stock.ticker_description()

Multiple Tickers 
----------------

Getting multiple tickers' information according to the filters.

.. code:: ipython3

	from finvizfinance.screener.overview import Overview

	foverview = Overview()
	filters_dict = {'Index':'S&P 500','Sector':'Basic Materials'}
	foverview.set_filter(filters_dict=filters_dict)
	df = foverview.screener_view()
	
Sentiment and News
------------------

Gets recent financial news, including a rating for sentiment.

.. code:: ipython3

	outer_ratings_df = stock.ticker_outer_ratings()

.. code:: ipython3

	news_df = stock.ticker_news()

.. code:: ipython3

	from finvizfinance.news import News

	fnews = News()
	all_news = fnews.get_news()

	all_news['news'].head() # 'blogs'

Insider Trades
--------------

Outputs a Pandas DataFrame of insider trades, their relationship, cost, value,
number of shares, and more.


.. code:: ipython3

	inside_trader_df = stock.ticker_inside_trader()

.. code:: ipython3

	from finvizfinance.insider import Insider

	finsider = Insider(option='top owner trade')
	# option: latest, top week, top owner trade
	# default: latest

	insider_trader = finsider.get_insider()
	


