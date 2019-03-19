#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Initialize the package for all scripts used in IPython startup.

This module intends to establish a few different things.

    - Initialize logging in a general manner.
    - Use :mod:`pkg_resources` provided by :mod:`setuptools` in order to create the directory as a namespace package
    - Define generic dunder methods.
    - Extend the user's ``$PATH `` to include this directory even if it != os.cwd

Mar 19, 2019

So with our sys.path hack, we can now do the following successfully::

    from pyutil import g


However we still have a problem.

Scratch that!::

    import pyutil.env

Now successfully works!!!

Let it doctest!

>>> import pyutil
>>> import pyutil.ytdl
>>> from pyutil import g


NOQA F401

"""
import logging
from logging import NullHandler
import os
import sys

import pkg_resources

from pyutil.__about__ import (  # noqa F401
    __author__, __copyright__, __description__, __docformat__, __license__,
    __title__, __package_name__,
)

logging.getLogger(__name__).addHandler(NullHandler())

pyutil_d = os.path.dirname('__init__.py')

sys.path.insert(0, pyutil_d)

pkg_resources.declare_namespace('.')
