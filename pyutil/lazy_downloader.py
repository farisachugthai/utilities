#!/usr/bin/env python
# Maintainer: Faris Chugthai
"""Automates downloading plain text files from the Web.

.. module:: pyutil.lazy_downloader


As implemented currently, it will only correctly handle plain text; however,
there are plans to implement the :mod:`mimetype` module and properly handle
a much wider range of files.


Parameters
----------
url : str
    A url to download

``output_filename``: path-like object
    A path to write the downloaded content to.


.. _lazy-downloader-usage:
Usage
------
.. code-block:: shell

    lazy_downloader url output_filename

Both parameters are required parameters.

If the filename already exists on the system it will NOT be overwritten,
and the script will safely exit.


.. todo:: Can we check the MIME type and only import :mod:`requests` if we know we'll need to?

"""
import argparse
import os
import sys

import requests


def main(url, output_fname):
    """Download URL and write to disk.

    Parameters
    ----------
    url : str
        A url to download

    ``output_fname``: path-like object
        A path to write the downloaded content to.


    .. todo:: Figure out how to check that the file is plain text and not hit constant false positives

    .. todo:: Add headers.

        .. code-block:: python3

            if res.headers['Content-Type']:
                 pass


    .. todo:: Could add in a check. if the file is over a certain size use `:func:requests.res.iter_chunk()`

    """
    res = requests.get(url)
    res.raise_for_status()

    with open(output_fname, "xt") as f:
        f.write(res.text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='lazy_downloader', description=__doc__)

    parser.add_argument(
        "URL", required=True, help="The URL to download. Must be plaintext.")

    # Will need to learn how to parse and tokenize the URL to get a reasonable
    # guess for the filename though
    parser.add_argument(
        "fname",
        help="The name of the file to write to. Must not exist already.")
    args = parser.parse_args()

    # With xt permissions the script crashes so no point raising anything.
    # Just bail
    if os.path.isfile(args.fname):
        sys.exit('File already exists. Cannot overwrite. Exiting.')
    # And if we're good, then bind the properties from the parser
    else:
        output_fname = args.fname
        url = args.URL

    main(url, output_fname)
