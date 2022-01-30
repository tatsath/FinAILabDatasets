.. _Oanda:

Oanda
=====

.. note::
    Refer to `Oanda Jupyter Notebook <https://github.com/tatsath/FinAILabDatasets/blob/main/Docs/JupyterNotebooks/Oanda.ipynb>`_ for more details.

Table of Contents
-----------------

-  `Installation`_
-  `Usage`_
-  `Historical OHLA and Volume for 1 Currency`_
-  `Setting the Frequency`_

Installation
------------

Install with pip:

.. code:: ipython3

	pip install oandapyV20

Or install with Github:

.. code:: ipython3

	pip install git+https://github.com/hootnot/oanda-api-v20.git

Usage
-----

.. note::
	This library requires a config file for accessing the API.
	An example config file can be found `here <oanda_example.cfg>`_. 

	You also need to set up an account on `Oanda's Website <https://developer.oanda.com/rest-live-v20/introduction/>`_ 
	to receive an access token and username.

Import all necessary libraries:

.. code:: ipython3

    import pandas as pd
	import tpqoa

	api = tpqoa.tpqoa("oanda.cfg")

Historical OHLA and Volume for 1 Currency
-----------------------------------------

Outputs the OHLCV for the given ``ticker``, within the given ``start`` and ``end`` dates.

.. code:: ipython3

	ticker = "US30_USD"
	start = "2018-09-01"
	end = "2019-09-01"

	api.get_history(ticker, start, end, "D", "B")

Setting the Frequency
---------------------

Sets the frequency to every 1 minute, dented by ``M1``

.. code:: ipython3

	api.get_history("EUR_USD", "2019-08-01", "2019-09-01", "M1", "B")

Sets the frequency to about every 5 seconds, using ``S5``

.. code:: ipython3

api.get_history("EUR_USD", "2019-09-01", "2019-09-04", "S5", "B")