# -*- coding: utf-8 -*-
"""
    sphinxcontrib
    ~~~~~~~~~~~~~

    This package is a namespace package that contains all extensions
    distributed in the ``sphinx-contrib`` distribution.

    :copyright: Copyright 2007-2014 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""
import logging
from logging import NullHandler
import os
import sys

logging.getLogger(__name__).addHandler(NullHandler())

sys.path.insert(0, os.path.dirname(os.path.abspath('.')))
