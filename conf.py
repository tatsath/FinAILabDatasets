import sys, os

sys.path.insert(0, os.path.abspath('extensions'))

extensions = [
	"sphinx_design",
	"nbsphinx",
	'sphinx_tabs.tabs',
	'sphinx_panels',
	'sphinx.ext.autosectionlabel',

]



html_theme = 'press'

nbsphinx_allow_errors = True

source_suffix = [".rst", ".md"]


# panels_add_bootstrap_css = False

# The master toctree document.
master_doc = 'index'

autosectionlabel_prefix_document = True
