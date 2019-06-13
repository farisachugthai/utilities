#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Create a script for searching through aliases.

.. currentmodule:: magic_aid


=========
Magic Aid
=========

By invoking ``%rehashx`` on :mod:`IPython`'s startup, there are
regularly more than 1000 aliases in the user's namespace.

This makes basic lookups slightly more involved.

IPython Aliases
---------------

As a result, this exports an IPython magic that searches through
all listed aliases by checking the first letter provided.

.. let's see if the ipython doc generator can handle a magic!

Multiple letters can be provided as long as they are whitespace
separated. For example::

    %run magic_aid.py i p y

Combining the letters together in one string or leaving them separate
as different elements in a list; however, would not work.

"""
import sys

from IPython import get_ipython
from IPython.core.magic import line_magic

from pyutil.rclone import run


@line_magic
def phelp(obj, shell=None):
    """Pipe `obj` through :mod:`pydoc` to :mod:`pynvim` with ``ft`` set to man.

    Parameters
    ----------
    obj : object
        Object to view documentation for in :mod:`pynvim` with :mod:`pydoc`.
    shell : |ip|
        Global IPython instance.

    Examples
    --------
    ::

        >>> from pyutil.magic_aid import phelp
        >>> from IPython import get_ipython
        >>> import matplotlib as mpl
        >>> _ip = get_ipython()
        >>> object_of_interest = mpl
        >>> phelp(object_of_interest, _ip)

    """
    cmd = ['nvim', '-c', 'set ft=man']
    return_code = run(cmd)
    return return_code


def search(char, shell=None):
    """Do a simple search for aliased names in :mod:`IPython`.

    This function independently initializes IPython so that it can be
    easily imported and run.

    Parameters
    ----------
    char : str
        Character to search through available magics for.
    shell : |ip|
        Global IPython instance.

    Returns
    -------
    results : list of strs
        All matching magics

    Examples
    --------
    ::

        >>> from pyutil.magic_aid import search
        >>> from IPython import get_ipython
        >>> _ip = get_ipython()
        >>> g_aliases = search('g', shell=_ip)
        >>> print(len(g_aliases))

    The above produced a value of 111 for me!


    """
    _user_aliases = shell.run_line_magic('alias', '')

    results = []
    for each_alias in _user_aliases:
        if each_alias[0].startswith(char):
            results.append(each_alias)
    return results


if __name__ == "__main__":
    _ip = get_ipython()

    matches = []
    for arg in sys.argv[1:]:
        matches.append(search(arg, _ip))
