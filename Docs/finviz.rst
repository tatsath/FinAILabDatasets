.. _finviz:

FinViz
======

.. warning::
    Links to JupyterNBs are currently not working.

Table of Contents
-----------------

-  `Installation`_
-  `Usage`_
-  `Fundamentals`_
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

.. code:: ipython3

	from finvizfinance.quote import finvizfinance
	import pandas as pd

Fundamentals
------------

.. code:: ipython3

	chart = stock.ticker_charts()
	chart

.. code:: ipython3

	stock_fundament = stock.ticker_fundament()

Ticker Description
------------------

.. code:: ipython3

	description = stock.ticker_description()

Multiple Tickers 
----------------

.. code:: ipython3

	from finvizfinance.screener.overview import Overview

	foverview = Overview()
	filters_dict = {'Index':'S&P 500','Sector':'Basic Materials'}
	foverview.set_filter(filters_dict=filters_dict)
	df = foverview.screener_view()
	
Sentiment and News
------------------

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

.. code:: ipython3

	inside_trader_df = stock.ticker_inside_trader()

.. code:: ipython3

	from finvizfinance.insider import Insider

	finsider = Insider(option='top owner trade')
	# option: latest, top week, top owner trade
	# default: latest

	insider_trader = finsider.get_insider()
	


