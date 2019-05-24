#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module that finds jpg and jpegs files in the current dir.

.. module:: find_pics
    :synopsis: Module that finds jpg and jpegs files in the current dir.

.. todo:: Should accept command line arguments.

We'll say that another thing on the todo list is return a path-like object
from :func:`find_pics()`.

# print(os.path.abspath(match)

Considering generalizing the module as I just whipped this up in the interpreter.

.. todo::

    I was on this website https://regex101.com/r/fR9oL4/1/codegen?language=python
    and it literally solved our problem with this module.

:URL: https://regex101.com/library/fR9oL4

That's the URL to a regex that finds 2 duplicate words that are next to each other.
Sort the spellfile in nvim and clean it up with this regex and the script below!::

    " \b(\w+)\s+\1\b " gi

.. code-block:: python3

    # coding=utf8
    # the above tag defines encoding for this document and is for Python 2.x compatibility

    import re

    regex = r"\b(\w+)\s+\1\b"

    test_str = ""

    matches = re.finditer(regex, test_str, re.IGNORECASE)

    for matchNum, match in enumerate(matches, start=1):

        print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))

        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1

            print("Group {groupNum} found at {start}-{end}: {group}".
                   format(groupNum = groupNum, start = match.start(groupNum),
                   end = match.end(groupNum), group = match.group(groupNum)))

    # Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u""
    to prefix the test string and substitution.

"""
import re
import os


def find_text(path):
    """Attempt at using :mod:`re`.

    Parameters
    ----------
    path : str
        Path-like object

    Yields
    -------
    match : :class`re.match` object
        Actually need to double check this function works because off the top
        of my head :func:`os.scandir` doesn't return a generator or at least
        one that's immediately usable. I think you have to do something like::

            for i in os.scandir('.'):
                print(i.name)

        To use it's output...

    """
    haystack = list(os.scandir(path))
    compiled = re.compile('[0-9]+.[a-z]+$')
    for needle in haystack:
        match = compiled.match(needle.name)
        yield match


def _format_return_value(matches):
    """Remove all entries that weren't matches.

    Parameters
    ----------
    matches : list of :class:`re.match` objects
        The compiled list returned from find_text.

    Returns
    -------
    TODO


    Examples
    --------
    In a script one could use the functions as so::

        >>> from find_pics import find_text, _format_return_value
        >>> matches = list(find_text('/path/to/dir'))
        >>> cleaned_data = _format_return_value(matches)

    """
    compact_matches = [match for match in matches if match is not None]
    return compact_matches


def find_pics(picture):
    """Finds jpegs and jpgs.

    .. todo:: Format the match object so it's more usable


    Parameters
    ----------
    picture : str
        Path to a file that may or may not be a jpg/jpeg


    Yields
    ------
    matched : :class:`re.match()` object
        Filename that matches a jpg/jpeg regex.

    """
    matched = re.match(".*jp(e)?g", picture)
    if matched:
        yield matched


if __name__ == "__main__":
    cwd_files = os.listdir(".")

    matches = [f for f in cwd_files if find_pics(f)]
