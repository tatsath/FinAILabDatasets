import sys, os

sys.path.insert(0, os.path.abspath('extensions'))

extensions = [
	"sphinx_design",
	"nbsphinx",
	'sphinx_tabs.tabs',
	'sphinx_panels',
	'sphinx.ext.autosectionlabel',
	'sphinx.ext.autodoc',
	'sphinx.ext.mathjax',
	'IPython.sphinxext.ipython_console_highlighting',
]

# List of arguments to be passed to the kernel that executes the notebooks:
nbsphinx_execute_arguments = [
    "--InlineBackend.figure_formats={'svg', 'pdf'}",
    "--InlineBackend.rc=figure.dpi=96",
]

html_theme = 'press'

nbsphinx_allow_errors = True

html_sourcelink_suffix = ''


source_suffix = [".rst", ".md", ".ipynb"]


# panels_add_bootstrap_css = False

# The master toctree document.
master_doc = 'index'

autosectionlabel_prefix_document = True
