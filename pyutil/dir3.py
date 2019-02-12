#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Improve the :func:`dir()` by ignoring methods hidden by _.

Dir3
======

.. module:: dir3

:File: dir3.py
:Author: Faris Chugthai
:Github: https://github.com/farisachugthai

Background
-----------

:func:`dir()` is a phenomenal function for exploring both the global namespace
and the exported methods of an object.

However it can get incredibly messy, especially when :mod:`IPython`
displays the placeholder variables for every cell that has been
run in the session. I.E.:

.. literal::

    _i
    _ii
    _iii
    _1
    _29
    ...

This causes an incredibly long output that's difficult to parse quickly at
best, and at worst, the output truncates and all valuable
information is hidden. This function attempts to avoid that by
hiding all private and/or mangled
methods I.E. ones that begin with the characters ``_`` or ``__``.

It also takes inspiration from :func:`IPython.utils.dir2.dir2()`.


Attributes
-----------

ip (InteractiveShell): A global object representing the active IPython
                       session. Contains varying packages as well as the
                       current global namespace. Doesn't need to be defined
                       in advance during an interactive session.

.. code-block:: rst

    .. ipython::

        In[1]: dir3()
        Out[1]: ...  # ELLIPSES

.. todo::

    - Show some example usage.
    - Should this function import or in any way be based off of dir2 via import?
    - We'll probably need to import register_line_magic or something.


See Also
---------
dir2(obj) -> list of strings

    Extended version of the Python builtin dir(), which does a few extra
    checks.

    This version is guaranteed to return only a list of true
    strings, whereas :func:`dir()` returns anything that
    objects inject into themselves, even if they
    are later not really valid for attribute access (many
    extension libraries have such bugs).

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


def dir3():
    """Filter unnecessary information from :func:`dir()` output.

    Parameters
    ------------
    None

    Returns
    --------
    output : list
        All methods that don't begin with '_'. More stringent filters will come.

    .. note::

        This might need to become a class soon this is quickly
        getting unwieldy and as is requires a lot of state.
    """
    # This should silence the error from flake about ip being used but not
    # defined
    from IPython import get_ipython
    ip = get_ipython()

    args = sys.argv[:]
    if len(args) == 2:
        output = _interactive(args)
    elif len(args) < 2:
        global_namespace = ip.user_global_ns.keys()
        output = _interactive(global_namespace)
    else:
        for i in range(args):
            output.append(_interactive(args[i]))

    print(str(output))
    return output


def _interactive(args):
    """Define a private method for interactive use instead of ifmain block.

    As this file is currently used in IPython's startup, the
    ifmain block will execute on startup which is not desired.

    What we're looking for is more similar to an autoload feature.

    Parameters
    ------------
    args : (iterable)
        The object to inspect.

    Returns
    --------
    filtered : list
        All methods that don't begin with '_'. More stringent filters will come.
    """
    filtered = []
    for i in args:
        if not i.startswith('_'):
            print(i)
            filtered.append(i)

    return filtered
