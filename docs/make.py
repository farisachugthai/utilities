#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Expedite documentation builds.

.. module:: make
    :synopsis: Expedite documentation builds.

We, in addition to automatic documentation builds, attempt to automate
installation of the package with subcommands.

.. sourcecode:: shell

    python make.py --install

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
builder : str
    The filetype :command:`make` invokes :command:`sphinx-build` to create


"""
import argparse
import logging
import os
import shutil
import sys
import webbrowser

from pyutil.__about__ import __version__
from pyutil.shell import BaseCommand

DOC_PATH = os.path.dirname(os.path.abspath(__file__))
SOURCE_PATH = os.path.join(DOC_PATH, '_source')
BUILD_PATH = os.path.join(DOC_PATH, '_build')
LOGGER = logging.getLogger(name=__name__)


def _parse_arguments(cmds=None):
    """Parse user arguments.

    .. todo:: Add a ton of arguments this isn't close to done.

    Parameters
    ----------
    cmd : str
        Arguments provided by the user.

    Returns
    -------
    user_args : :class:`argparse.NameSpace`
        Argumemts as they've been interpreted by :mod:`argparse`.

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
    within python. In addition we can use :mod:`runpy` to run
    :command:`sphinx-build` directly.

    Or we can invoke the :mod:`sphinx` API to maximize customization.

    """
    cmds = [method for method in dir(DocBuilder) if not method.startswith('_')]

    parser = argparse.ArgumentParser(description="Pyutil doc builder.",
                                     epilog="Commands: {}".format(
                                         ','.join(cmds)))

    parser.add_argument('builder',
                        nargs='?',
                        default='html',
                        metavar='builder: (html or latex)',
                        help='command to run: {}'.format(', '.join(cmds)))

    parser.add_argument('-j',
                        '--num-jobs',
                        type=int,
                        default=os.cpu_count(),
                        help='number of jobs used by sphinx-build')

    parser.add_argument('-n',
                        '--no-api',
                        default=False,
                        help='Omit api and autosummary',
                        action='store_true')

    parser.add_argument('-s',
                        '--single',
                        metavar='FILENAME',
                        type=str,
                        default=None,
                        help=('filename of section or method name to build.'))

    parser.add_argument('-p',
                        '--python-path',
                        type=str,
                        default=os.path.dirname(DOC_PATH),
                        help='path')

    parser.add_argument('-l',
                        '--log',
                        default=sys.stdout,
                        type=argparse.FileType('w'),
                        help='File to write logging messages to.')

    parser.add_argument('-ll',
                        '--log-level',
                        dest='log_level',
                        default='INFO',
                        help='Log level. Defaults to INFO. Implies logging.')

    parser.add_argument('--version', action='version', version=__version__)

    user_args = parser.parse_args()

    return user_args


class DocBuilder(BaseCommand):
    """Class to wrap the different commands of this script.

    All public methods of this class can be called as parameters of the
    script.
    """

    def __init__(self, cmd):
        """Initialize self."""
        super().__init__(cmd)

    def sphinx_build(self, kind='html'):
        """Build docs.

        Parameters
        ----------
        kind : {'html', 'latex'}
            Kind of docs to build.

        Examples
        --------
        >>> DocBuilder(num_jobs=4).sphinx_build('html')

        """
        if kind not in ('html', 'latex'):
            raise ValueError('kind must be html or latex, '
                             'not {}'.format(kind))

        cmd = ['sphinx-build', '-b', kind]
        cmd += [
            '-d',
            os.path.join(BUILD_PATH, 'doctrees'), SOURCE_PATH,
            os.path.join(BUILD_PATH, kind)
        ]
        return self.run(cmd)


def termux_hack():
    """Android permissions don't allow viewing files in app specific files."""
    try:
        shutil.copytree(
            '_build/html/',
            '/data/data/com.termux/files/home/storage/downloads/html')
    except FileExistsError:
        shutil.rmtree(
            '/data/data/com.termux/files/home/storage/downloads/html')
        shutil.copytree(
            '_build/html/',
            '/data/data/com.termux/files/home/storage/downloads/html')
    except FileNotFoundError:
        logging.error("The build directory currently doesn't exist. Exiting.")


if __name__ == "__main__":
    args = _parse_arguments()

    try:
        log_level = args.log_level.upper()
    except Exception:
        logging.basicConfig(level=logging.WARNING)
    else:
        logging.basicConfig(level=log_level)

    try:
        jobs = args.jobs
    except AttributeError:
        logging.error('No jobs attribute in jobs.')
        jobs = f'{os.cpu_count()}'

    logging.debug(jobs)
    builder = args.builder

    if os.environ.get('ANDROID_ROOT'):
        termux_hack()
    else:
        DocBuilder(f'make -j{jobs} {builder}').sphinx_build(kind=builder)
