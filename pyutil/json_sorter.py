#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Reorganizes a JSON file with the keys sorted and indentation standardized.

This module was originally used to fix my settings.json from VSCode.
:File: json_sorter.py
:Author: Faris Chugthai
:Email: farischugthai@gmail.com
`Github <https://github.com/farisachugthai>`_

Attributes
----------
fobj : path-like object
    The file to fix.

Example
-------
.. code:: bash

    python3 json_sorter.py /path/to/file.json


"""
import json
import os
import sys


def main(file_obj):
    """Read in a JSON object, sorts it and then writes it back to a new file.

    By writing to a new file, the user is allowed the opportunity to inspect
    the file and ensure that the desired results have been achieved.

    Parameters
    ----------
    fobj : path-like object
        The file to read in

    Returns
    -------
    None


    """
    with open(file_obj) as f:
        settings = json.loads(f.read())

    json_str = json.dumps(settings, indent=4, sort_keys=True)

    with open('settings.test.json', 'xt') as f:
        f.write(json_str)


if __name__ == "__main__":
    args = sys.argv[:]
    if len(args) == 2:
        fobj = sys.argv[1]
    else:
        sys.exit("Requires 1 file to fix.")

    if os.path.isfile(fobj):
        main(fobj)
