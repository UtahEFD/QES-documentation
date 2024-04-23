# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'QES'
copyright = '2024, University of Utah'
author = 'UTAH EFD'
# The master toctree document.
root_doc = 'index'

#release = '1.0'
#version = '1.0.0'

# -- General configuration

extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.bibtex',
]

bibtex_bibfiles = ['refs.bib']
bibtex_reference_style = 'label'
bibtex_default_style = 'unsrt'

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output
html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- Options for LaTeX output
latex_documents = [
    (main, 'main.tex', 'QES Documentation',
     'QES', 'manual'),
]
