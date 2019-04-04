#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module that finds jpg and jpegs files in the current dir.

.. module:: find_pics
    :synopsis: Module that finds jpg and jpegs files in the current dir.

.. todo:: Should accept command line arguments.

We'll say that another thing on the todo list is
return a path-like object from :func:`find_pics()`.
# print(os.path.abspath(match)


Considering generalizing the module as I just whipped this up in the interpreter.

"""
import re
import os


def find_text(path):
    """Attempt at using re."""
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
    path = os.listdir(".")

    matches = [f for f in path if find_pics(f)]
