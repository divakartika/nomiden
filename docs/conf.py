# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'nomiden'
copyright = '2023, Diva K'
author = 'Diva K'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'autoapi.extension',
    'myst_parser',
    'nbsphinx'
]

autoapi_dirs = ["../nomiden"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["*test*", "*tests*", "nik.py", "kk.py"]
autoapi_ignore = ["*/test_*.py", "*/tests/", "*/test*", "*/nik.py", "*/kk.py"]

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'