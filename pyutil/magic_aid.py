#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Create a script for searching through aliases.

By invoking %rehashx on IPython's startup, there are regularly more than 1000 aliases in the namespace.
This makes basic lookups slightly more involved.

As I've ran this script twice in the last 2 days I figured time to save it.
"""
import sys

from IPython import get_ipython


def inspector(char):
    """Do a simple search for aliased names in IPython."""
    # Run line magic func?
    alias = %alias

    results = []
    for i in alias:
        if i[0].startswith(char):
            results.append(i)
    return results


if __name__ == "__main__":
    if len(sys.argv) == 2:
        char = sys.argv[1]

    matches = inspector(char)
    print(matches)
