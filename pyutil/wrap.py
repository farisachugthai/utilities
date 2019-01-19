#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Wrap text similarly to :func:`textwrap.dedent` but w/ multiple paragraphs

From IPython.utils.text
"""
import re
from textwrap import dedent, fill

def wrap_paragraphs(text, ncols=80):
    """Wrap multiple paragraphs to fit a specified width.

    This is equivalent to textwrap.wrap, but with support for multiple
    paragraphs, as separated by empty lines.

    Returns
    -------

    list of complete paragraphs, wrapped to fill `ncols` columns.
    """
    paragraph_re = re.compile(r'\n(\s*\n)+', re.MULTILINE)
    text = dedent(text).strip()
    paragraphs = paragraph_re.split(text)[::2]  # every other entry is space
    out_ps = []
    indent_re = re.compile(r'\n\s+', re.MULTILINE)
    for p in paragraphs:
        # presume indentation that survives dedent is meaningful formatting,
        # so don't fill unless text is flush.
        if indent_re.search(p) is None:
            # wrap paragraph
            p = fill(p, ncols)
        out_ps.append(p)
    return out_ps
