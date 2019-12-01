#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Initialize the package for all scripts used in IPython startup.

This module intends to establish a few different things.

    - Initialize logging in a general manner.
    - Use :mod:`pkg_resources` provided by :mod:`setuptools` in order to create the directory as a namespace package
    - Define generic dunder methods.
    - Extend the user's ``$PATH `` to include this directory even if it != os.cwd


NOQA F401

"""
from alabaster import _version as alabaster_version
import logging
from logging import NullHandler
import os
import sys
import pkg_resources

pkg_resources.declare_namespace('.')


from pyutil.__about__ import (  # noqa F401
    __author__,
    __copyright__,
    __description__,
    __docformat__,
    __license__,
)

logging.getLogger(__name__).addHandler(NullHandler())


def get_path():
    """Shortcut for users whose theme is next to their conf.py."""
    # Theme directory is defined as our parent directory
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def update_context(app, pagename, templatename, context, doctree):
    context["alabaster_version"] = alabaster_version.__version__


def setup(app):
    # add_html_theme is new in Sphinx 1.6+
    if hasattr(app, "add_html_theme"):
        theme_path = os.path.abspath(os.path.dirname(__file__))
        app.add_html_theme("alabaster", theme_path)
    app.connect("html-page-context", update_context)
    return {"version": alabaster_version.__version__, "parallel_read_safe": True}


sys.path.insert(0, get_path())
