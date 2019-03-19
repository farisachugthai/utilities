#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Take a :mod:`json` file and sort the keys and insert 4 spaces for indents.

This module was originally used to fix my settings.json from VSCode.

"""
import argparse
import json
import logging
import os
import sys
import yaml

LOG_LEVEL = 'logging.WARNING'


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
        '-y',
        '--yaml',
        dest='yaml',
        default=sys.stdout,
        type=argparse.FileType(mode='w'),
        help="YAML file to write to. Defaults to stdout.")

    parser.add_argument(
        '-l',
        '--log_level',
        dest='log_level',
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        help='Set the logging level')

    args = parser.parse_args()

    return args


def convert_to_yaml(file_obj):
    """Convert a :mod:`json` to YAML.

    Parameters
    ----------
    file_obj : str
        The file to read in

    """
    json_data = json.loads(open(file_obj))
    converted_json_data = json.dumps(json_data, sort_keys=True)
    # output yaml
    yaml_text = yaml.dump(yaml.load(converted_json_data), default_flow_style=False)
    return yaml_text


def sort_json(file_obj):
    """Read in a :mod:`json` object, sort it and write it back to a new file.

    By writing to a new file, the user is allowed the opportunity to inspect
    the file and ensure that the desired results have been achieved.

    Parameters
    ----------
    file_obj : str
        The file to read in

    """
    with open(file_obj) as f:
        settings = json.loads(f.read())

    json_str = json.dumps(settings, indent=4, sort_keys=True)

    logging.debug('Formatted json:\n' + str(json_str))
    return json_str


def text_writer(plaintext, output_file=sys.stdout):
    """Write the previously inputted text to a file.

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
    """foo."""
    args = _parse_arguments()

    try:
        log_level = args.log_level
    except Exception:
        logging.basicConfig(level=LOG_LEVEL)
    else:
        logging.basicConfig(level=log_level)

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
