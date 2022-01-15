import os

html_theme = 'press'

# hoverxref_tooltip_maxwidth = 650
# hoverxref_auto_ref = True

# hoverxref_sphinxtabs = True
# hoverxref_mathjax = True

extensions = [
	"nbsphinx",
# 	   JupyterNotebooks/EOD.ipynb
#    JupyterNotebooks/finviz.ipynb
#    JupyterNotebooks/FRED.ipynb
#    JupyterNotebooks/FundamentalAnalysis.ipynb
#    JupyterNotebooks/FXCM.ipynb
#    JupyterNotebooks/IEX.ipynb
#    JupyterNotebooks/Oanda.ipynb
#    JupyterNotebooks/quandl.ipynb
#    JupyterNotebooks/stooq.ipynb
#    JupyterNotebooks/yahoofinancials.ipynb
#    JupyterNotebooks/yfinance.ipynb
	# "hoverxref.extension"
]

source_suffix = [".rst", ".md"]

# The master toctree document.
master_doc = 'index'

exclude_patterns = [
	'_build'
]
# nbsphinx_allow_errors = True
# learn how to make a theme