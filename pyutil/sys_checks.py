#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Module to check a user is utilizing the proper version of python.

Even outside of the 2 to 3 incompatibilities, the standard library
introduces new modules often enough that it's useful to check what version oof
Python is being run.

.. rubric:: Assumes: All functions are imported as the module will immediately exit if directly executed.

If nothing else this is a lesson in how painful it becomes to maintain
nonsense names.

Expanding to Paths
------------------
This module is admittedly quite limited if we only check ``sys.executable``.

Let's do some general file checking with :mod:`pathlib`. This module itself
was added to the standard library recently, and as a result, we'll import it
with a try statement.

"""
import sys
try:
    from pathlib import Path
except ImportError:
    pass


def is_file(file_obj):
    """Check a file exists on the system.

    Examples
    --------
    ::

         >>> from pyutil.sys_checks import is_file
         >>> if is_file('path/to/file'):
             >>> pass

    """
    p = Path(file_obj)
    return p.is_file()


def py_gt_raise(min_py_version):
    """Raise an error if python interpreter is not above a certain version."""
    if sys.version_info < min_py_version:
        print("Can not use python interpreter provided: " +
              str(sys.version_info()))
        raise RuntimeError(
            "The following version of python and newer are required: " +
            str(min_py_version))


def py_gt_exit(min_py_version):
    """Check a user's python version is higher than some floor value.

    For example, the :mod:`argparse` was only introduced in python3.2.

    .. todo:: Possibly change API so funcs return a value on success.

    Parameters
    ------------
    min_py_version : int or float or tuple
        Value that represents the lowest version of python that can be used.

    """
    if sys.version_info < min_py_version:
        print("Can not use python interpreter provided: " +
              str(sys.version_info()))
        raise RuntimeError(
            "The following version of python and newer are required: " +
            str(min_py_version))


def py_lt_exit(max_py_version):
    """Check a user's python version is lower than some ceiling value.

    If you'll crash on python3.4 but work on 3.3, call this func with 3.3.

    Parameters
    ------------
    max_py_version : int or float or tuple
        The highest version of python that can be used

    """
    # unsure if necessary
    if not type(max_py_version) == int or float or tuple:
        tuple(max_py_version)

    if sys.version_info > max_py_version:
        print("Can not use python interpreter provided: " +
              str(sys.version_info()))
        sys.exit("The following version of python and newer are required: " +
                 str(max_py_version))


if __name__ == '__main__':
    sys.exit("Source this file don't run it directly!")
