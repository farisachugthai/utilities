#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Module to check a user is utilizing the proper version of python.

Even outside of the 2 to 3 incompatibilities, the standard library
introduces new modules often enough that it's useful to check.

Utilized by importing as so.

.. code-block::

    # filename: must_be_three.py
    from syschecks import py_gt

    py_gt(3)

.. code-block: shell

    python2 must_be_three.py

.. todo:

    Uh actually execute the above because now I'm interested...

Assumes:

    All functions are imported as the module will immediately exit if directly
    executed.
"""
from platform import system
import sys


def py_gt(min_py_version):
    """Check a user's python version is higher than some floor value.

    For example, the :mod:`argparse` was only introduced in python3.2.

    Everything utilizing it as a result needs to check that the right version
    is setup.

    .. todo::

        Possibly change API so funcs return a value on success.

    :param min_py_version: The lowest version of python that can be used
    :return: None
    """
    if sys.version_info < min_py_version:
        sys.exit("Can not use python interpreter provided: "
                 + str(sys.version_info()))
        sys.exit("The following version of python and newer are required: "
                 + str(min_py_version))


def py_lt(max_py_version):
    """Check a user's python version is lower than some ceiling value.

    If you'll crash on python3.4 but work on 3.3, call this func with 3.3.

    :param max_py_version: The highest version of python that can be used
    :type: int or float or tuple
    :return: None
    """
    # unsure if necessary
    if type(max_py_version) not in (int, tuple, float):
        tuple(max_py_version)

    if sys.version_info > max_py_version:
        print("Can not use python interpreter provided: "
                + str(sys.version_info()))
        sys.exit("The following version of python and newer are required: "
                + str(max_py_version))


def test_linux():
    """Not a unit test but checks that the user is on Linux OS."""
    assert system() == 'Linux'


if __name__ == '__main__':
    sys.exit("Source this file don't run it directly!")
