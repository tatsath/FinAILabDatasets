.. _Oanda:

Oanda
=====

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

.. code:: ipython3

    import pandas as pd
	import tpqoa

	api = tpqoa.tpqoa("oanda.cfg")

Historical OHLA and Volume for 1 Currency
-----------------------------------------

.. code:: ipython3

	api.get_history("US30_USD", "2018-09-01", "2019-09-01", "D", "B")

Setting the Frequency
---------------------

.. code:: ipython3

	api.get_history("EUR_USD", "2019-08-01", "2019-09-01", "M1", "B")