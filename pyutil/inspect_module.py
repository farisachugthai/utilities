#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Explore the namespace and attributes of a module.

If no argument is provided then use the name bound to the local IPython object.

However Python3.6 now has the builtin module 'pyclbr' so this entire script may be irrelevant.
"""

import sys
import importlib


def main(mod_name):
    """
    Credit for this function in particular goes entirely to:
    Vasudev Ram
    mod_attrs_and_types.py
    """
    print('Attributes and their types for module {}:\n'.format(mod_name))
    for num, attr in enumerate(dir(eval(mod_name))):
        print("{idx}: {nam:30}  {typ}".format(
            idx=str(num + 1).rjust(4),
            nam=(mod_name + '.' + attr).ljust(30),
            typ=type(eval(mod_name + '.' + attr))))


if __name__ == '__main__':
    # ip is the ipython object that's loaded immediately after the interpreter starts
    mod = sys.argv[1] if len(sys.argv) == 2 else "ip"

    if mod not in dir():
        try:
            importlib.import_module(mod)
        except ImportError as e:
            sys.exit("Not importable.")

    main(mod)
