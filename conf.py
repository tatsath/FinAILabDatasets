import os

html_theme = 'press'

hoverxref_tooltip_maxwidth = 650
hoverxref_auto_ref = True

hoverxref_sphinxtabs = True
hoverxref_mathjax = True

extensions = [
	# "nbsphinx",
	"hoverxref.extension"
]

source_suffix = [".rst", ".md"]

# The master toctree document.
master_doc = 'index'

exclude_patterns = [
	'_build'
]
# nbsphinx_allow_errors = True
# learn how to make a theme