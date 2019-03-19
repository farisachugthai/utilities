#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Initialize the package for all scripts used in IPython startup.

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

Still having tons of problems and it seems to be related to me not understanding
how python handles modules, paths and executable.

Currently this isn't working

.. code-block:: shell

    python setup.py test

However running ``make html`` inside of docs works, and ``python setup.py build_sphinx`` works as well.

Changes to scripts only seem to create a pronounced effect when ``python setup.py bdist_egg`` is run.

Not wheels. Not ``pip install -e .`` or ``setup.py develop``
This is so strange.

Holy hell. So everything I've been executing has been inside of a conda environment.

So running `conda develop .` fixed everything...

That's amazing and infuriating I spent WAY too much time on that.

But what to do about Termux?

Argparse
--------
On a completely different note is it a bad idea idea to subclass ArgParser, set up base options with version, a
general help message and junk and then initialize it in __init__? That would
let every module use it with no work.

Well regardless let IPython exist globally.

NOQA F401

"""
import logging
from logging import NullHandler
import os
import sys

import pkg_resources

from .__about__ import (  # noqa F401
    __author__, __copyright__, __description__, __docformat__, __license__,
    __title__,
)

logging.getLogger(__name__).addHandler(NullHandler())

PYUTIL_DIR = os.path.dirname(os.path.abspath('__init__.py'))

sys.path.insert(0, PYUTIL_DIR)

pkg_resources.declare_namespace('.')

from IPython import embed, get_ipython
