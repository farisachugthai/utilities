#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
from textwrap import dedent, TextWrapper

try:
    from prompt_toolkit import print_formatted_text as print
except (ImportError, ModuleNotFoundError):
    pass

from pyutil.sys_checks import is_file


class ZimText(TextWrapper):

    def __init__(
        self,
        text=None,
        width=80,
        break_long_words=False,
        break_on_hyphens=False,
        **kwargs
    ):
        self.width = width
        self.break_long_words = break_long_words
        self.break_on_hyphens = break_on_hyphens
        super().__init__(**kwargs)

    def wrap_paragraphs(self):
        paragraph_re = re.compile(r"\n(\s*\n)+", re.MULTILINE)
        self.text = dedent(self.text).strip()
        paragraphs = paragraph_re.split(self.text)[::2]  # every other entry is space
        wrapped_text = []
        indent_re = re.compile(r"\n\s+", re.MULTILINE)
        for p in paragraphs:
            # presume indentation that survives dedent is meaningful formatting,
            # so don't fill unless text is flush.
            if indent_re.search(p) is None:
                # wrap paragraph
                p = self.fill(p)
            wrapped_text.append(p)
        return wrapped_text

    def string2lines(self, convert_whitespace=True):
        """Convert a string to a list of lines.

        Parameters
        -----------
        convert_whitespace : bool
            convert form feeds and vertical tabs to spaces

        Returns
        -------
        list of str
            Return a list of one-line strings with tabs expanded, no newlines, and
            trailing whitespace stripped.

        """
        if convert_whitespace:
            self.text = self._munge_whitespace(self.text)
        new_text = [s for s in self.text.splitlines()]
        return new_text

def main():
    args = sys.argv[:]
    if len(args) < 2:
        raise RuntimeError("Needs a file to reformat as an argument.")
    else:
        wrapper = ZimText()
        for i in args[1:]:
            if is_file(i):
                print("Rewrapping " + i)
                wrapper.wrap_paragraphs(args[1:])


if __name__ == "__main__":
    main()
