#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module comes directly from :mod:`flake8_rst`

As you can see it adds the IPython directive as an option for the following

``.. code-block:: rst``

    ``.. code-block:: ipython``


"""
from docutils.parsers.rst import directives
from sphinx.directives.code import CodeBlock

from ..sourceblock import ROLES as SOURCEBLOCK_ROLES
from ..checker import ROLES as CHECKER_ROLES

try:
    from IPython.sphinxext.ipython_directive import IPythonDirective
except ImportError:
    IPythonDirective = None


def add_custom_roles(directive_class):
    if not directive_class:
        return
    for role in SOURCEBLOCK_ROLES + CHECKER_ROLES:
        directive_class.option_spec['flake8-' + role] = directives.unchanged


def setup(app):
    add_custom_roles(CodeBlock)
    add_custom_roles(IPythonDirective)
