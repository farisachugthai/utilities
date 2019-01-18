#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Improve the :func:`dir()` by ignoring methods hidden by _.

.. todo::

    We'll probably need to import register_line_magic or something.

"""
import sys

from IPython.utils import dir2


def dir3(obj_meth):
    """Lets upgrade dir2 from ipy a lil.

    Uh so far no params.
    Oh I guess the object you feed it.
    So maybe this would work better as a line magic?
    Idk.
    """
    public_methods = []
    for i in obj_meth:
        if not i.startswith('_'):
            public_methods.append(i)
            print(i)

    return public_methods


if __name__ == "__main__":
    obj_meth = dir2(sys.argv[1])

    dir3(obj_meth)
