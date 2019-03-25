#!/usr/bin/env python
# Maintainer: Faris Chugthai
"""Automates downloading plain text files from the Web.

As implemented currently, it will only correctly handle plain text;
however, there are plans to implement the :mod:`mimetype` module and
properly handle a much wider range of files.

Both parameters, `url` and `output_fname` are required parameters.

Safety Features
---------------
If the filename already exists on the system it will NOT be overwritten,
and the script will safely exit.

:class:`collections.ChainMap`
-------------------------------
This module a perfect candidate for :ref:`collections.Chainmap`. Check env vars,
config files, command line args and user provided parameters.

"""
import argparse
from contextlib import closing
import logging
import os
import re
import sys

import requests

from pyutil.__about__ import __version__

# logger = logging.getlogger(__name__)
# handler =


def _parse_arguments():
    """Parse user input."""
    parser = argparse.ArgumentParser(prog='__name__', description=__doc__)

    parser.add_argument(
        "URL",
        nargs=1,
        type=str,
        help="The URL to download. Must be plaintext.")

    # Will need to learn how to parse and tokenize the URL to get a reasonable
    # guess for the filename though
    parser.add_argument(
        "fname",
        help="The name of the file to write to. Must not exist already.")

    parser.add_argument(
        "-ha",
        "--headers",
        nargs='*',
        help="Headers to send to the web server.")

    parser.add_argument(
        '-V', '--version', action='version', version='%(prog)s' + __version__)

    args = parser.parse_args()

    return args


def _get_page(URL):
    """Get the content at `URL`.

    Returns content if it is recognized HTML/XML. If not, return `None`.
    """
    try:
        with closing(requests.get(url, stream=True)) as res:
            if check_response(res):
                return res.content
            else:
                return None

    except requests.RequestException as e:
        # logger.something
        return None


def check_response(server_response):
    content = server_response.headers['Content-Type'].lower()
    if server_response.status_code == 200 and content is not None:
        return True
    else:
        # logger
        return server_response.status_code


def _parse_site(URL, *args, **kwargs):
    """Parse the given `URL`, remove tags and return plaintext.

    This should probably be modified to take the user agent and header args.

    Parameters
    ----------
    URL : str
        Page to download.

    Returns
    -------
    txt : str
        Plaintext view of the website.

    """
    res = requests.get(URL)
    res.raise_for_status()

    txt = res.text()
    return txt


def find_links(text):
    """Search body of text for URLs.

    Parameters
    ----------
    text : str
        Body of formatted text to search for URLs.

    Returns
    -------
    links : todo
        URLs found on site.

    """
    links = re.findall('"((http|ftp)s?://.*?)"', text)
    return links


def main(url, output_fname):
    """Download URL and write to disk.

    .. todo:: Add headers.

        .. code-block:: python3

            if res.headers['Content-Type']:
                 pass

    Well here's part of one of your todos. :mod:`youtube_dl` has these
    defined in their utils

    .. code-block:: python3

        std_headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-us,en;q=0.5',
        }


        USER_AGENTS = {
            'Safari': 'Mozilla/5.0 (X11; Linux x86_64; rv:10.0) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
        }


    .. todo::

        Could add in a check. if the file is over a certain size use :func:`requests.res.iter_chunk()`


    Parameters
    ----------
    url : str
        A url to download

    output_fname : str
        A path to write the downloaded content to.

    """
    txt = _parse_site(url)

    with open(output_fname, "xt") as f:
        f.write(txt)


if __name__ == "__main__":
    args = _parse_arguments()
    # With xt permissions the script crashes so no point raising anything.
    # Just bail
    if os.path.isfile(args.fname):
        raise FileExistsError
    # And if we're good, then bind the properties from the parser
    else:
        output_fname = args.fname
        url = args.URL

    std_headers = {
        'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
        'Accept':
        'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-us,en;q=0.5',
    }

    # ...??
    # USER_AGENTS = {
    #     'Safari':
    #     'Mozilla/5.0 (X11; Linux x86_64; rv:10.0) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
    # }

    try:
        headers = args.headers
    except Exception:
        headers = std_headers

    try:
        user_agent = args.user_agent
    except Exception:
        user_agent = USER_AGENTS

    main(url, output_fname)
