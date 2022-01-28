FinAILab's Datasets! - Free Financial data for building AI and Machine Learning in Finance
==========================================================================================


.. dropdown:: Panels in a drop-down
    :title: bg-success text-warning
    :open:
    :animate: fade-in-slide-down

    .. panels::
        :container: container-fluid pb-1
        :column: col-lg-6 col-md-6 col-sm-12 col-xs-12 p-2
        :card: shadow
        :header: border-0
        :footer: border-0

        ---
        :card: + bg-warning

        header
        ^^^^^^

        Content of the top-left panel

        ++++++
        footer

        ---
        :card: + bg-info
        :footer: + bg-danger

        header
        ^^^^^^

        Content of the top-right panel

        ++++++
        footer

        ---
        :column: col-lg-12 p-3
        :card: + text-center

        .. link-button:: panels/usage
            :type: ref
            :text: Clickable Panel
            :classes: btn-link stretched-link font-weight-bold

This documentation contains the information about the **Free financial dataset** for thousands
of asset classes, macroeconomic data, fundamentals and alternative data that can be used for building models on `FinAILab <http://finailab.com/>`_.

This doumentation shows you how to get massive amounts of Financial Data and explains how to **install required Libraries** and how to **download/import the data** with few lines of Python Code.

The data covered in this documentation include:
-----------------------------------------------
- Historical Price and Volume Data for 100,000+ Symbols/Instruments.
- 50+ Exchanges all around the world.
- Real-time and Historical Data (back to 1960s)
- High-frequency real-time Data
- Foreign Exchange (FOREX): 150+ Currency Pairs
- 500+ Cryptocurrencies
- Commodities (Crude Oil, Gold, Silver, etc.)
- Futures and Option data
- Macroeconomic variables
- Stock Options, Stock Splits and Dividends for 5000+ Stocks
- Fundamentals, Metrics and Ratios for Stocks, Bonds, Indexes, Mutual Funds and ETFs
- Balance Sheets, Cashflow and Profit and Loss Statements (P&L)
- 50+ Technical Indicators (i.e. SMA, Bollinger Bands).

Financial Datasets - Summary by source and types:
-------------------------------------------------

.. tabs::

   .. tab:: Equities
      
      Some.
      
   .. tab:: FX

      another.


.. panels::

    Content of the top-left panel

    ---

    Content of the top-right panel

    :badge:`example,badge-primary`

    ---

    .. dropdown:: :fa:`eye,mr-1` Bottom-left panel

        Hidden content

    ---

    .. link-button:: https://example.com
        :text: Clickable Panel
        :classes: stretched-link

.. tabbed:: Tab 4
    :selected:

    .. dropdown:: Nested Dropdown

        Some content

.. csv-table::
   :file: feature_tracker_table.csv
   :header-rows: 1
   :class: longtable
   :widths: auto

.. toctree::
   :maxdepth: 1
   :caption: Source

   Docs/YahooFinance
   Docs/Alphavantage
   Docs/FundamentalAnalysis
   Docs/quandl
   Docs/FRED
   Docs/Stooq
   Docs/IEX
   Docs/Oanda
   Docs/finviz

.. toctree::
   :maxdepth: 1
   :caption: Categories

   Docs/Equities
   Docs/FixedIncome
   Docs/FX
   Docs/Commodities
   Docs/Crypto
   Docs/Fundamentals
   Docs/OptionFuture
   Docs/Macroeconomic
   Docs/News
   Docs/AlternativeData
  
.. toctree::
   :maxdepth: 1
   :caption: Notebooks

   Docs/JupyterNotebooks/Alphavantage
   Docs/JupyterNotebooks/finviz
   Docs/JupyterNotebooks/FRED
   Docs/JupyterNotebooks/FundamentalAnalysis
   Docs/JupyterNotebooks/IEX
   Docs/JupyterNotebooks/Oanda
   Docs/JupyterNotebooks/quandl
   Docs/JupyterNotebooks/stooq
   Docs/JupyterNotebooks/yfinance


Contributing
------------

To any interested in making the FinAIML better, there are still some improvements
that need to be done.
A full TODO list is available in the `roadmap <https://github.com/users/tatsath/projects/4>`_.

If you want to contribute, please go through `CONTRIBUTING.md <https://github.com/tatsath/FinAILabDatasets/blob/master/CONTRIBUTING.md>`_ first.

Indices and tables
-------------------

* :ref:`genindex`
* :ref:`search`
* :ref:`modindex`
