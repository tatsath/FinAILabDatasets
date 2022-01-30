.. _FundamentalAnalysis:

.. note::
    Refer to `FundamentalAnalysis Jupyter Notebook <https://github.com/tatsath/FinAILabDatasets/blob/main/Docs/JupyterNotebooks/FundamentalAnalysis.ipynb>`_ for more details.

FundamentalAnalysis
===================

-  `Installation`_
-  `Usage`_
-  `List all Commands`_
-  `Historical Price and Volume for 1 Stock`_
-  `Financial Ratios`_
-  `Stock Fundamentals`_
-  `Financials`_
-  `Key Metrics`_

Installation
------------

.. note::
    Before working with this API, you will need to obtain
    a key from `FinancialModellingPrep's API <https://site.financialmodelingprep.com/developer/docs/>`_

Install with pip:

.. code:: ipython3
    
    pip install FundamentalAnalysis

Usage
-----

.. note::
    FundamentalAnalysis automatically uses Pandas DataFrames.

Import all necessary libraries:

.. code:: ipython3

    import FundamentalAnalysis as fa
    import financedatabase as fd
    import pandas as pd

    ticker = "TSLA"
    api_key = "your api key"

List all Commands
-----------------

Gets all of the options from ``cryptocurrencies``, ``currencies``, ``equities``, ``etfs`` or ``funds`` 
that are available to be queried.

.. code:: ipython3

    # Options: 'cryptocurrencies', 'currencies', 'equities', 'etfs' or 'funds'
    options = fd.show_options('cryptocurrencies', equities_selection=None, country=None, sector=None, industry=None)
    options = pd.DataFrame(options)
    options

Lists all of the companies that the API offers to be queried.

.. code:: ipython3

    # Show the available companies
    companies = fa.available_companies(api_key)
    companies.sort_values('symbol')

Lists all of the exchanges available for access.

.. code:: ipython3

    companies.exchange.unique()

Historical Price and Volume for 1 Stock
---------------------------------------

Gets the OHLCV for one stock, given the ``period`` and ``interval``.

.. code:: ipython3

    # General stock data
    stock_data = fa.stock_data(ticker, period="ytd", interval="1d")

    # Detailed stock data
    stock_data_detailed = fa.stock_data_detailed(ticker, api_key, begin="2000-01-01", end="2020-01-01")
    stock_data_detailed

Financial Ratios
----------------

.. warning:: 
    This feature requires a premium subscription.

.. code:: ipython3

    
    # Large set of in-depth ratios
    financial_ratios_annually = fa.financial_ratios(ticker, api_key, period="annual")
    financial_ratios_quarterly = fa.financial_ratios(ticker, api_key, period="quarter")

Stock Fundamentals
------------------

.. code:: ipython3

    profile = fa.profile(ticker, api_key)
    profile

Financials
----------

.. warning:: 
    This feature requires a premium subscription.

.. code:: ipython3

    ticker ="DIS"

.. code:: ipython3

    # Balance Sheet statements
    balance_sheet_annually = fa.balance_sheet_statement(ticker, api_key, period="annual")
    balance_sheet_quarterly = fa.balance_sheet_statement(ticker, api_key, period="quarter")

.. code:: ipython3

    # Income Statements
    income_statement_annually = fa.income_statement(ticker, api_key, period="annual")
    income_statement_quarterly = fa.income_statement(ticker, api_key, period="quarter")

.. code:: ipython3

    # Cash Flow Statements
    cash_flow_statement_annually = fa.cash_flow_statement(ticker, api_key, period="annual")
    cash_flow_statement_quarterly = fa.cash_flow_statement(ticker, api_key, period="quarter")

Key Metrics
-----------

.. warning:: 
    This feature requires a premium subscription.

.. code:: ipython3

    # Key Metrics
    key_metrics_annually = fa.key_metrics(ticker, api_key, period="annual")
    key_metrics_quarterly = fa.key_metrics(ticker, api_key, period="quarter")

Sentiment
---------

Gets various ratings and scores for the given ``ticker``.

.. code:: ipython3

    ratings = fa.rating(ticker, api_key)

