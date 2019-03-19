#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Reorganizes a JSON file with the keys sorted and indentation standardized to 4 spaces.

This module was originally used to fix my settings.json from VSCode.

"""
import argparse
import json
import logging
import os
import sys

log_level = 'WARNING'


def _parse_arguments():
    """Parse arguments given by the user."""
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument(
        'input',
        type=argparse.FileType('r'),
        default=sys.stdin,
        help="File to parse.")

    parser.add_argument(
        '-o',
        '--output',
        default=sys.stdout,
        type=argparse.FileType(mode='w'),
        help="File to write to. Defaults to stdout.")

    parser.add_argument(
        '-l',
        '--log_level',
        dest=log_level,
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        help='Set the logging level')

    args = parser.parse_args()

    # Actually can't do this
    # if len(args) == 1:
    #     parser.print_help()
    #     sys.exit()

    return args


def main(file_obj, output_file=sys.stdout):
    """Read in a :mod:`json` object, sort it and write it back to a new file.

    By writing to a new file, the user is allowed the opportunity to inspect
    the file and ensure that the desired results have been achieved.

    Parameters
    ----------
    file_obj : str
        The file to read in
    output_file : str
        Text file to write formatted :mod:`json` to.
        It will only write to the file if the filename currently doesn't exist.

    """
    with open(file_obj) as f:
        settings = json.loads(f.read())

    json_str = json.dumps(settings, indent=4, sort_keys=True)

    with open(output_file, 'xt') as f:
        f.write(json_str)


if __name__ == "__main__":
    args = _parse_arguments()

    if args.log_level:
        log_level = args.log_level
        logging.basicConfig(level=log_level)

    fobj = args.input

    o_file = args.output

    if os.path.isfile(fobj):
        main(fobj, o_file)
    else:
        sys.exit("File not readable in current state. Exiting.")
