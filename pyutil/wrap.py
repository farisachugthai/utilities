#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Wrap text similarly to :func:`textwrap.dedent()` but with multiple paragraphs.

From :mod:`IPython.utils.text`.

Possibly going to convert sys.argv to `**kwargs` for the function.

Allow the user to input any parameters that are accepted by
:class:`textwrap.TextWrapper()`


"""
import re
import sys
from textwrap import dedent, fill


def wrap_paragraphs(text, ncols=80):
    """Wrap multiple paragraphs to fit a specified width.

    This is equivalent to :func:`textwrap.wrap()`, but with support for multiple
    paragraphs, as separated by empty lines.

    Considering initializing an instance of :class:`textwrap.TextWrapper()`
    for increased configurability.

    Parameters
    ----------
    text : str
        text to wrap using :mod:`re` and :func:`textwrap.dedent()`
    ncols : int
        column to wrap text at


    Returns
    -------
    wrapped_text : list of str
        list of complete paragraphs, wrapped to fill `ncols` columns.


    """
    paragraph_re = re.compile(r'\n(\s*\n)+', re.MULTILINE)
    text = dedent(text).strip()
    paragraphs = paragraph_re.split(text)[::2]  # every other entry is space
    wrapped_text = []
    indent_re = re.compile(r'\n\s+', re.MULTILINE)
    for p in paragraphs:
        # presume indentation that survives dedent is meaningful formatting,
        # so don't fill unless text is flush.
        if indent_re.search(p) is None:
            # wrap paragraph
            p = fill(p, ncols)
        wrapped_text.append(p)
    return wrapped_text


if __name__ == '__main__':
    args = sys.argv[:]
    if len(args) < 2:
        sys.exit('Requires a file to re-format.')
    else:
        sys.exit(wrap_paragraphs(args[1:]))

    # it might be easier to do the above.
    # can't do it like the below because then we have to hardcode the value of
    # ncols # so we could force some kw args for the script but it's then easier
    # for # the user to import the function and use it themselves.

    # if len(args) > 2:
    # for i in args[1:]:
    # wrap_paragraphs(i, 80)
