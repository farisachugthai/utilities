#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Expedite documentation builds.

.. module:: make
    :synopsis: Expedite documentation builds.

We could, in addition to automatic documentation builds, attempt to automate
installation of the package with subcommands. Uhm well argparse doesn't really
give us that functionality so it'd be more like

.. sourcecode:: shell

    python make.py --install

But that works IMO.

Utilizing IPython's Sphinx plugin
---------------------------------
This never occured to me to do this...

.. code-block:: python3

    from IPython.sphinxext import ipython_directive, ipython_console_highlighting
    # Then initialize a sphinx instance to pass to the console one
    ipython_console_highlighting.setup(app)


.. todo::

    Document initializing a Sphinx instance. Off the top of my head, it
    requires setting src_dir and conf_dir so possibly gonna be easier
    to do in :ref:`conf.py`, but that file exports some constants
    so maybe we'll just scoop them up?

.. todo::

    Check that the f string syntax is correct.
    Possibly now need to import sys_checks and ensure that we have python > 3.6

.. todo::

    Copy the sources over to the right spot.
    And that static dir I guess. :func:`shutil.copytree()`

.. todo:: Fix the way logging is set up here.


Attributes
-----------
`builder` : str
    The filetype that ``make`` will invoke ``sphinx-build`` to create


"""
import argparse
import logging
import os
import shlex
import subprocess
import sys


def _parse_arguments():
    """Parse user arguments.

    .. todo:: Add a ton of arguments this isn't close to done.

    Returns
    -------
    args : str
        Arguments provided by the user.


    See Also
    --------
    :mod:`docutils.core`
        Shows a few good methods on how to programatically publish docs.


    Examples
    --------
    .. code-block:: python3

        from docutils.core import *
        help(publish_string)
        help(publish_file)
        help(publish_programatically)

    Should give some inspiration on easy ways to invoke docutils from
    within python. In addition we can use :mod:`runpy` to run sphinx-build
    directly.

    Or we can invoke the :mod:`sphinx` API to maximize customization.

    """
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument(
        '-b', '--builder', help='Builder to invoke sphinx-build to use')

    parser.add_argument(
        '-l',
        '--log',
        default=sys.stdout,
        type=argparse.FileType('w'),
        help='File to write logging messages to.')

    parser.add_argument(
        '-ll',
        '--log-level',
        dest=log_level,
        default='INFO',
        help='Log level. Defaults to INFO. Implies logging.')

    parser.add_argument('--version', action='version', version='0.0.1')

    args = parser.parse_args()

    return args


def run(cmd):
    """Execute the required command in a subshell.

    First the command is split using :mod:`shlex`.

    A new process is created, and from the resulting subprocess object
    the :func:`subprocess.Popen().wait()` is invoked.

    When the subprocess returns, any non-zero value will lead to a
    `SystemExit` with a passed value of `returncode`.

    Parameters
    ----------
    cmd : str
        The command to be called

    Returns
    -------
    process.returncode : int
        The returncode from the process.


    """
    cmd = shlex.split(cmd)
    logging.debug("Cmd is: " + str(cmd))
    process = subprocess.Popen(cmd)

    if process.wait():
        raise SystemExit(process.returncode)
    else:
        return process.returncode


if __name__ == "__main__":
    args = _parse_arguments()

    if args.log_level:
        log_level = args.log_level.upper()
        logging.basicConfig(level=logging.log_level)

    jobs = f'{os.cpu_count()}'

    logging.debug(jobs)

    run(f'make -j{jobs}')
# needs rewrite
try:
    shutil.copytree('_build/html/', '/data/data/com.termux/files/home/storage/downloads/html')
except FileExistsError:
    shutil.rmtree('/data/data/com.termux/files/home/storage/downloads/html')
else:
    shutil.rmtree('_build/html')
    
