#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Initialize the package for all scripts used in :mod:`IPython` startup.

Mar 19, 2019

So with our ``sys.path`` hack, we can now do the following successfully::

    from pyutil import g

Let it doctest!

>>> import pyutil
>>> import pyutil.ytdl
>>> from pyutil import g


NOQA F401

"""
import argparse
import logging
from logging import NullHandler
import os
import sys

import pkg_resources

from .__about__ import (  # noqa F401
    __author__, __copyright__, __description__, __docformat__, __license__,
    __title__, __version__, __version_info__)

logging.getLogger(__name__).addHandler(NullHandler())

# Should I just set up some blanket logging
logger = logging.basicConfig(level=logging.WARNING)

PYUTIL_DIR = os.path.dirname(os.path.abspath('__init__.py'))

sys.path.insert(0, PYUTIL_DIR)

del PYUTIL_DIR

pkg_resources.declare_namespace('.')


def __parse_arguments():
    """I doubt that this is the best way to do this but I'm curious.

    March 22, 2019

    Can we define a method in the __init__ file and just let every package below
    us import it?

    Because this would save me a lot of time.
    """
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument(
        '-V', '--version', action='version', version='%(prog)s' + __version__)

    parser.add_argument(
        '-l',
        '--log_level',
        dest='log_level',
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        help='Set the logging level')

    args = parser.parse_args()

    return args