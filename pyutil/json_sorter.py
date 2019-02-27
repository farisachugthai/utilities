#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Reorganizes a JSON file with the keys sorted and indentation standardized.

This module was originally used to fix my settings.json from VSCode.
:File: json_sorter.py
:Author: Faris Chugthai
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
import argparse
import logging
import json
import os
import sys


def _parse_arguments():
    """Parse arguments given by the user."""
    parser = argparse.ArgumentParser(description=__doc__)

    # TODO: Set to sys.stdin if empty.
    parser.add_argument(
        'input',
        required=True,
        type=argparse.FileType(''),
        help="File to parse.")

    parser.add_argument(
        '-o',
        '--output',
        default=sys.stdout,
        type=argparse.FileType(''),
        help="File to write to. Defaults to stdout.")

    parser.add_argument('-ll', '--loglevel', type=str,
                        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                        help='Set the logging level')

    args = parser.parseargs()

    if len(args) == 1:
        parser.print_help()
        sys.exit()

    return args


def main(file_obj):
    """Read in a JSON object, sorts it and then writes it back to a new file.

    By writing to a new file, the user is allowed the opportunity to inspect
    the file and ensure that the desired results have been achieved.

    Parameters
    ----------
    ``file_obj`` : path-like object
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
    args = _parse_arguments()

    logging.basicConfig(level=args.loglevel)

    fobj = args.input

    if os.path.isfile(fobj):
        main(fobj)
