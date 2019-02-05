# -*- coding: utf-8 -*-
"""
    sphinxcontrib
    ~~~~~~~~~~~~~

    This package is a namespace package that contains all extensions
    distributed in the ``sphinx-contrib`` distribution.

    :copyright: Copyright 2007-2014 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""
import sys

from pkgutil import extend_path

__import__('pkg_resources').declare_namespace(__name__)

__path__ = extend_path(sys.path, __name__)
