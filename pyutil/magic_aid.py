#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Create a script for searching through aliases.

IPython Aliases
---------------
By invoking ``%rehashx`` on :mod:`IPython`'s startup, there are
regularly more than 1000 aliases in the namespace.

This makes basic lookups slightly more involved.

As I've ran this script twice in the last 2 days I figured time to save it.
"""
import sys

from IPython import get_ipython


def search(char):
    """Do a simple search for aliased names in :mod:`IPython`.

    This function independently initializes IPython so that it can be
    easily imported and run.

    Parameters
    ----------
    char : str
        Character to search through available magics for.

    Returns
    -------
    results : list of strs
        All matching magics

    """
    _ip = get_ipython()

    alias = _ip.run_line_magic('alias', 'line')

    results = []
    for i in alias:
        if i[0].startswith(char):
            results.append(i)
    return results


if __name__ == "__main__":
    for i in sys.argv[1:]:
        search(i)
