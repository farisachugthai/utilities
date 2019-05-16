#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Common functionality when working with paths.

Adds in logging functionality at initialization.
Assumes Python3.4 as it utilizes pathlib heavily.

Roadmap
-------
* Read through :mod:`pathlib`.
* Figure out what slots are. They're initialized in PurePath() but I
  don't get what they're doing
* Determine how we want to define __repr__ and __str__ because we should
  probably override at least __repr__
  * __str__ follows repr

"""
import logging
from pathlib import Path


class PathTools(Path):
    """Frequently used methods for :mod:`pathlib` bundled together.

    Here's a few interesting methods from the original implementation of
    :class:`pathlib.PurePath`::

        def as_posix(self):
            # Return the string representation of the path with forward (/)
            # slashes.
            f = self._flavour
            return str(self).replace(f.sep, '/')

        def __repr__(self):
            return "{}({!r})".format(self.__class__.__name__, self.as_posix())

    If we know for a fact that we're on Powershell, that shell accepts ``/``
    to my knowledge and we can use it. But it'll crash :command:`cmd`.

    """

    def __init__(self, log_level=logging.WARNING, **kwargs):
        """Initialize the PathTools object with an optional argument for logging."""
        self.log_level = log_level
        super().__init__(kwargs)

    def logger(self):
        """Initialize a named logger for the PathTools object."""
        self.logger = logging.getLogger(name=__name__)
        self.logger.setLevel(self.log_level)
        return self.logger

    def output_results(self, output_dir):
        """Checks that an directory exists and create it if not.

        Parameters
        ----------
        output_dir : str (path-like)
            Directory to store profiling results in.

        Returns
        -------
        Bool

        Raises
        -------
        SystemExit if there is an error while making a directory.

        """
        if self.joinpath(output_dir).exists() is False:
            try:
                self.mkdir(output_dir)
            except OSError:
                raise SystemExit
            else:
                return True
        else:
            if self.joinpath(output_dir).is_dir() is False:
                self.logger.error('The output directory exists but is not a directory.')
                return False
            else:
                return True
