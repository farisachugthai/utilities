#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Explore the namespace and attributes of a module.

Written before :mod:`pyclbr` was created.
However Python3.6 now has the builtin module :mod:`pyclbr` so this entire
script may be irrelevant.

Parameters
----------
``mod_name`` : module to inspect
    If no argument is provided, then use the namespace bound to the global
    :class:`IPython.core.interactiveshell.InteractiveShell()` object.

Returns
-------
TODO

"""
import importlib
import sys

try:
    from IPython import get_ipython
except ImportError:
    pass
else:
    _ip = get_ipython()


def main(mod_name):
    """Show all available methods for the given object.

    It shouldn't prove difficult to refactor a few things and allow this
    function to also take list arguments. Then the user could either give a
    comma separated list of modules to explore, or they could give a file.

    Parameters
    ----------
    ``mod_name`` : module
        The provided module to inspect for the user.


    Returns
    --------
    ``mod_namespace`` : methods and attributes
        The provided module's namespace.


    """
    print('Attributes and their types for module {}:\n'.format(mod_name))
    mod_namespace = dir(eval(mod_name))

    for num, attr in enumerate(mod_namespace):

        print("{idx}: {name:30}  {attr_type}".format(
            idx=str(num + 1).rjust(4),
            name=(mod_name + '.' + attr).ljust(30),
            attr_type=type(eval(mod_name + '.' + attr))))

    return mod_namespace


if __name__ == '__main__':
    args = sys.argv[:]
    mod = args[1] if len(args) >= 2 else _ip

    if mod not in dir():
        # There's a couple different ways you can explore the user namespace,
        # and if we assume they're running in IPython i think they're immediately
        # available under the _ip class.
        try:
            importlib.import_module(mod)
        except ImportError:
            sys.exit("The module that was provided is not importable.")

    mod_namespace = main(mod)
