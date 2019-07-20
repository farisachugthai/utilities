#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Take a :mod:`json` file and sort the keys and insert 4 spaces for indents.

==================
:mod:`json` sorter
==================

This module was originally used to fix my settings.json from VSCode.

One Line Solution
=================

>>> sorted((json.loads(open('settings.json').read()).items()), key=operator.getitemattr)

You definitely shouldn't implement it as a one liner, *as you can clearly see,*;
however 5 functions and a handful of instantiated classes and debugging, and
we're somehow barely closer to done.

The functions for reading and writing files could be refactored and used over the
entire package.

The logger **should** be set up that way.

This code is going to easily clear 100 lines when a JSON encoded object shouldn't
take more than a few lines to deserialize and work with.

This'll serve as a good template for testing out tools to build a simple
script with.

The problem is already solved. Let's see what we can't squeeze out of our tools
along the way.

----------

"""
import argparse
import json
import logging
import operator
import os
import sys
import yaml

from pyutil.__about__ import __version__

LOGGER = logging.Logger(name=__name__)


def _parse_arguments():
    """Parse arguments given by the user.

    This implementation still, somehow isn't done. An option for *inplace*
    modifications needs to be added.

    Unfortunately this will be mutually exclusive to the output file option.
    So we'll need to work on learning argparse.mutually_exclusive_groups.

    Returns
    -------
    args : :class:`argparse.NameSpace()`
        Arguments provided by the user and handled by argparse.
    """
    parser = argparse.ArgumentParser(prog="JSON sorter", description=__doc__)

    parser.add_argument('input',
                        type=argparse.FileType('r'),
                        default=sys.stdin,
                        help="File to parse. Defaults to stdin.")

    parser.add_argument('-o',
                        '--output',
                        default=sys.stdout,
                        type=argparse.FileType(mode='w'),
                        help="File to write to. Defaults to stdout.")

    parser.add_argument('-y',
                        '--yaml',
                        dest='yaml',
                        default=sys.stdout,
                        type=argparse.FileType(mode='w'),
                        help="YAML file to write to. Defaults to stdout.")

    # is there a way to have info printed with this from argparse?
    parser.add_argument('-l',
                        '--log',
                        action='store_true',
                        dest="log",
                        metavar="Enable logging",
                        default=False,
                        help='Turn logging on and print to console.')

    parser.add_argument(
        '-ll',
        '--log_level',
        dest='log_level',
        metavar='log level',
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        help='Set the logging level')

    parser.add_argument('-V',
                        '--version',
                        action='version',
                        version='%(prog)s' + __version__)

    args = parser.parse_args()

    return args


def convert_to_yaml(file_obj):
    """Convert a :mod:`json` to YAML.

    Parameters
    ----------
    file_obj : str
        The file to read in

    Returns
    -------
    yaml_object : str
        Converted :mod:`PyYAML` text.

    """
    converted_json_data = sort_json(file_obj)
    # output yaml
    yaml_text = yaml.dump(yaml.load(converted_json_data),
                          default_flow_style=False)
    return yaml_text


def sort_json(file_obj):
    """Read in a :mod:`json` object, sort it and write it back to a new file.

    By writing to a new file, the user is allowed the opportunity to inspect
    the file and ensure that the desired results have been achieved.

    Parameters
    ----------
    file_obj : str
        The file to read in

    Returns
    -------
    json_text : str
        Correctly formmated :mod:`json` text.

    """
    with open(file_obj) as f:
        settings = json.loads(f.read())

    json_str = sorted(json.dumps(settings, indent=4), key=operator.getitem())

    logging.debug('Formatted json: %s\n' % str(json_str))
    return json_str


def text_writer(plaintext, output_file=sys.stdout):
    """Write the previously inputted text to a file.

    This function could easily be utilized over the whole package though.

    Parameters
    ----------
    plaintext : str
        The file to read in
    output_file : str
        Text file to write formatted :mod:`json` to.
        It will only write to the file if the filename currently doesn't exist.

    """
    with open(output_file, 'xt') as f:
        f.write(plaintext)
        logging.info('File written is: ' + str(output_file))


def main():
    """Handles user args, sets up logging and calls other functions."""
    args = _parse_arguments()

    try:
        LOG_LEVEL = args.log_level
    except AttributeError as e:
        print(e)
        LOG_LEVEL = 'WARNING'

    if LOG_LEVEL is None:
        LOG_LEVEL = 'WARNING'

    LOGGER.setLevel(level=LOG_LEVEL)

    fobj = args.input
    o_file = args.output

    if os.path.isfile(o_file):
        raise FileExistsError
    else:
        try:
            yaml = args.yaml
        except Exception:
            plaintext = sort_json(fobj)
        else:
            plaintext = convert_to_yaml(yaml)

    logging.debug("Plaintext is: " + str(plaintext))
    text_writer(plaintext, o_file)


if __name__ == "__main__":
    main()
