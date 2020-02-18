#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Common functionality when working with paths.

Adds in logging functionality at initialization.
Assumes Python3.4 as it utilizes :mod:`pathlib` heavily.


"""
import logging
from pathlib import Path


class PathTools:
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
        """Initialize PathTools with an optional argument for logging."""
        self.log_level = log_level
        self._Path = Path(".")

    def __repr__(self):
        """Stolen from the stdlib."""
        return "{}({!r})".format(self.__class__.__name__, self._Path.as_posix())

    def logger(self, log_name="root"):
        """Initialize a named logger for the PathTools object."""
        self.log = logging.getLogger(name=log_name)
        self.log.setLevel(self.log_level)
        return self.log

    def dir_exists(self, output_dir):
        """Checks that an directory exists and create it if not.

        Parameters
        ----------
        output_dir : str (path-like)
            Directory to check.

        Returns
        -------
        Bool

        """
        if self._Path.joinpath(output_dir).exists() is False:
            try:
                self._Path.mkdir(output_dir)
            except OSError as e:
                self.logger.error(
                    "The directory {} does not exist but we can't create it because: {}".format(
                        output_dir, e
                    )
                )
            else:
                return True
        else:
            if self._Path.joinpath(output_dir).is_dir() is False:
                self.logger.error("The output directory exists but is not a directory.")
                return False
            else:
                return True
