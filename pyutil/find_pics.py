#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Finds all the jpegs and jpgs in the user's current directory."""
import re
import os


def find_pics(path):
    """Finds jpegs and jpgs.

    :param path: path to a directory to check
    :type path: str or path-like object

    :yields: an re-match object

    .. todo::

        Format the match object so it's more usable
    """
    matched = re.match(".*jp(e)?g", f)
    if matched:
        yield f


if __name__ == "__main__":
    path = os.listdir(".")
    # list comprehesion with a function?
    matches = []
    for f in path:
        matches.append(find_pics(f))
