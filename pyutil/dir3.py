#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Improve the :func:`dir()` by ignoring methods hidden by _.

.. todo::

    We'll probably need to import register_line_magic or something.


See Also
---------

dir2(obj) -> list of strings

    Extended version of the Python builtin dir(), which does a few extra
    checks.

    This version is guaranteed to return only a list of true strings, whereas
    dir() returns anything that objects inject into themselves, even if they
    are later not really valid for attribute access (many extension libraries
    have such bugs).

.. code-block:: python

    # Start building the attribute list via dir(), and then complete it
    # with a few extra special-purpose calls.

    >>> try:
        >>> words = set(dir(obj))
    >>> except Exception:
        >>> # TypeError: dir(obj) does not return a list
        >>> words = set()

    >>> if safe_hasattr(obj, '__class__'):
        >>> words |= set(dir(obj.__class__))

    # filter out non-string attributes which may be stuffed by dir() calls
    # and poor coding in third-party modules

    >>> words = [w for w in words if isinstance(w, str)]
    >>> return sorted(words)
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
