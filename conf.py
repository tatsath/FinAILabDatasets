import sys, os

sys.path.insert(0, os.path.abspath('extensions'))

extensions = [
	"sphinx_design",
	"nbsphinx",
	'sphinx_tabs.tabs',
	'sphinx_panels',
	'sphinx.ext.autosectionlabel'
]

html_theme = 'press'

nbsphinx_allow_errors = True

html_sourcelink_suffix = ''

html_static_path = ['_static']
html_css_files = ['my-own-style.css']

# nbsphinx_prolog = """
# .. raw:: html

#     <style>
#         h1 {
#             color: chartreuse;
#         }
#     </style>
# """


source_suffix = [".rst", ".md", ".ipynb"]


# panels_add_bootstrap_css = False

# The master toctree document.
master_doc = 'index'

autosectionlabel_prefix_document = True
