#!/usr/bin/env python
# Maintainer: Faris Chugthai
"""Automating the process of grabbing plain text files from the internet.

Usage::
    lazy_downloader url output_filename

If filename already exists on the system it will NOT be overwritten,
and the script will crash.
"""
import argparse
import os
import sys

import requests


def main():
    """ Download URL and write to disk."""
    res = requests.get(args.URL)
    res.raise_for_status()

    #  if res.headers['Content-Type']:
    #      pass
    #  # TODO: figure out how to check that the file is plain text and not hit
    # constant false positives

    with open(args.fname, "xt") as f:
        f.write(res.text)


# could add in a check. if the file is over a certain size use res.iter_chunk()
if __name__ == "__main__":
    parser = argparse.ArgumentParser("A helper script to automate downloading \
                                     1 plain text file at a time.")
    parser.add_argument("URL", help="The URL to download. Must be plaintext.")

    # TODO: As this script currently stands, fname is required which is silly.
    # Should change to -o, --output and make optional
    # Will need to learn how to parse and tokenize the URL to get a reasonable
    #guess for the filename though
    parser.add_argument("fname", help="The name of the file to write to. \
                         Must not exist already.")
    args = parser.parse_args()

    # with xt permissions the script crashes so no point raising anything just bail
    if os.path.isfile(args.fname):
        sys.exit('File already exists. Cannot overwrite. Exiting.')
    main()
