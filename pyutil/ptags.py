#!/usr/bin/python3
"""Create a tags file for Python programs, usable with vi.

Currently uses a regex to create a tags file.

Files to tag
------------
- functions (even inside other defs or classes)
- classes
- filenames

Warns about files it cannot open.

No warnings about duplicate tags.

Snagged from the scripts dir in python3.6-examples.

.. todo:: Use ipdb and step through while watching the tags var.


Otherwise add in `PEP 257`_ compliant params.
Try different styles and see what you like.


.. _PEP 257:
    https://www.python.org/dev/peps/pep-0257

"""
import os
import re
import sys


def main():
    """Handle CLAs and work with writing the tags file."""
    args = sys.argv[1:]
    for filename in args:
        treat_file(filename)
    if tags:
        fp = open("tags", "w")
        tags.sort()
        for s in tags:
            fp.write(s)


def treat_file(filename):
    """Find usable matches for tags file.

    Parameters
    ----------
    filename : path-like object
        File to generate tags from.

    Returns
    -------
    None : None

    """
    try:
        fp = open(filename, "r")
    except Exception:
        sys.stderr.write("Cannot open %s\n" % filename)
        return
    base = os.path.basename(filename)
    if base[-3:] == ".py":
        base = base[:-3]
    s = base + "\t" + filename + "\t" + "1\n"
    tags.append(s)
    while 1:
        line = fp.readline()
        if not line:
            break
        m = matcher.match(line)
        if m:
            content = m.group(0)
            name = m.group(2)
            s = name + "\t" + filename + "\t/^" + content + "/\n"
            tags.append(s)


if __name__ == "__main__":
    tags = []
    expr = r"^[ \t]*(def|class)[ \t]+([a-zA-Z0-9_]+)[ \t]*[:\(]"
    matcher = re.compile(expr)
    main()
