#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Configuration file for the Sphinx documentation builder.

=========================
Sphinx Configuration File
=========================

.. currentmodule:: conf

.. highlight:: ipython

This file does only contain a selection of the most common options.
For a full list see the documentation:

:URL: `<http://www.sphinx-doc.org/en/master/config>`_

Path Setup
----------
If extensions (or modules to document with autodoc) are in another
directory, add these directories to :data:`sys.path` here.

If the directory is relative to the documentation root, use
:func:`os.path.abspath()` to make it absolute, like shown `here`_.::

    sys.path.insert(0, os.path.abspath('.'))

.. _here: `https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-source_suffix`

However, the filetype mapping came about in 1.8 so make sure to add
that ``needs-sphinx=version`` bit

Also note the setup() function modeled off of parameters described in
the `official documentation`_.

.. _official documentation: http://www.sphinx-doc.org/en/master/extdev/appapi.html

"""
from pyutil.__about__ import __version__
from datetime import datetime
import logging
import os
import sys

# So even though it sets off the linters this is needed to recognize numpydoc
# as a package
from numpydoc import numpydoc  # noqa
try:
    import flake8_rst  # noqa
except (ImportError, ModuleNotFoundError):
    flake8_rst = None

CONF_PATH = os.path.dirname(os.path.abspath(__file__))
BUILD_PATH = os.path.join(CONF_PATH, 'build')
SOURCE_PATH = os.path.join(CONF_PATH, '_source')
SOURCE_CODE = os.path.join('..', 'pyutil')

sys.path.insert(0, os.path.abspath(SOURCE_CODE))

logging.basicConfig(level=logging.WARNING)

sys.path.insert(0, os.path.abspath('.'))

# from .sphinxext import magics  # noqa

sys.path.insert(0, os.path.abspath(os.path.join(SOURCE_CODE, 'numerical')))

logging.debug("Path is currently: " + str(sys.path))

# -- Project information --------------------------------------------

# Does Sphinx use this while building the docs? Appears so from
# Sphinx.
project = u'pyutil'
copyright = u'2018-{}, Faris A Chugthai'.format(datetime.now().year)
author = u'Faris A Chugthai'

# The short X.Y version
version = __version__
# The full version, including alpha/beta/rc tags
release = version

# -- General configuration ------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# Just updated 1.8 because of app.add_js_fileg()
needs_sphinx = '1.8'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'IPython.sphinxext.ipython_console_highlighting',
    'IPython.sphinxext.ipython_directive',
    'numpydoc',
]

if flake8_rst:
    extensions.append('flake8_rst.sphinxext.custom_roles')

try:
    from sphinxext import magics  # noqa F401
except ImportError:
    logging.debug('Magics was not imported.')
else:
    logging.debug('Magics was imported.')
    extensions.append('docs.sphinxext.magics')

try:  # noqa F401
    import matplotlib  # noqa F401
except (ImportError, ModuleNotFoundError):
    pass
else:
    extensions.extend(
        [
            'matplotlib.sphinxext.plot_directive',
            'matplotlib.sphinxext.mathmpl'
        ]
    )

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:

source_suffix = ['.rst']
# source_suffix = ['.rst', '.md']
# or:
# source_suffix = {
#     '.rst': 'restructuredtext',
#     '.txt': 'restructuredtext',
#     '.md': 'markdown',
# }

# The encoding of source files.
source_encoding = 'utf-8'

# source_parsers = {
#     '.md': 'recommonmark.parser.CommonMarkParser',
#     '.rst': 'sphinx.parsers.Parser',
#     '.txt': 'sphinx.parsers.Parser'
# }

# The master toctree document.
master_doc = 'index'

rst_epilog = """
.. |ip| replace:: :class:`IPython.core.interactiveshell.InteractiveShell`
"""
# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
# language = None

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_domain = 'python'
default_role = 'py:obj'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
# So i overwrote the pygments.css file entirely so i wanna see what happens
pygments_style = 'sphinx'

# -- Options for HTML output ----------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "github_user": "Faris A. Chugthai",
    "github_repo": "utilities",
    "github_banner": True,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

# Modify alabaster with custom.css in this dir. Keeping this param the same
# is required.
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
html_sidebars = {
    '**':
        [
            'about.html',
            'relations.html',
            'globaltoc.html',
            'localtoc.html',
            'searchbox.html',
            'sourcelink.html',
        ]
}

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# -- Options for HTMLHelp output ------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'pyutil'

# -- Options for LaTeX output ---------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc, 'pyutil.tex', 'Pyutil Documentation', 'Faris A Chugthai',
        'manual'
    ),
]

# -- Options for manual page output ---------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, 'pyutil', 'Pyutil Documentation', [author], 1)]

manpages_url = 'https://linux.die.net/man/'

# -- Options for Texinfo output -------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc, 'Pyutil', 'Pyutil Documentation', author, 'Pyutil',
        'One line description of project.', 'Miscellaneous'
    ),
]

# -- Options for Epub output ----------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
# epub_identifier = ''

# A unique identification for the text.
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# -------------------------------------------------------------------
# -- Extension configuration ----------------------------------------
# -------------------------------------------------------------------

# -------------------------------------------------------------------
# -- Options for intersphinx extension ------------------------------
# -------------------------------------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'scipy': ('https://docs.scipy.org/doc/scipy/reference', None),
    'matplotlib': ('https://matplotlib.org', None), 'python':
        ('https://docs.python.org/3/', None), 'numpy':
            ('https://docs.scipy.org/doc/numpy/', None), 'ipython':
                ('https://ipython.readthedocs.io/en/stable/', None)
}

# -------------------------------------------------------------------
# -- Options for todo extension -------------------------------------
# -------------------------------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -------------------------------------------------------------------
# Autosummary
# -------------------------------------------------------------------

# import glob  # noqa F402
autosummary_generate = True

# -------------------------------------------------------------------
# Napoleon settings
# -------------------------------------------------------------------

napoleon_include_private_with_doc = True

viewcode_follow_imported_members = False

# -------------------------------------------------------------------
# Option for IPython directive
# -------------------------------------------------------------------

ipython_warning_is_error = False

# -------------------------------------------------------------------
# Numpydoc
# -------------------------------------------------------------------

numpydoc_show_class_members = False  # Otherwise Sphinx emits thousands of warnings
numpydoc_class_members_toctree = False


def setup(app):
    """Add custom css styling.

    .. admonition:: Warning for path names.

        Don't use :func:`os.path.abspath()` if you need to extend this.
        Pathmames that have a :kbd:`.` in them will be interpreted as packages
        and crash the build. I.E. the following won't work.:

            */data/data/com.termux/*

    """
    app.add_js_file(os.path.join('_static', '', 'sidebar.js'))
    return {
        'version': 'builtin',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
