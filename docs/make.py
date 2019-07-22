#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Expedite documentation builds.

.. module:: make
    :synopsis: Expedite documentation builds.

We attempt to automate documentation builds with this module.

"""
import argparse
import logging
import os
import shutil
import subprocess
import sys
import webbrowser

from pyutil.__about__ import __version__

DOC_PATH = os.path.dirname(os.path.abspath(__file__))
BUILD_PATH = os.path.join(DOC_PATH, '_build')
LOGGER = logging.getLogger(name=__name__)


def _parse_arguments(cmds=None):
    """Parse user arguments.

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


class DocBuilder:
    """Class to wrap the different commands of this script.

    All public methods of this class can be called as parameters of the
    script.

    Attributes
    -----------
    builder : str
        The filetype :command:`make` invokes :command:`sphinx-build` to create.

    """

    def __init__(self, num_jobs=1, verbosity=0, warnings_are_errors=False):
        self.num_jobs = num_jobs
        self.verbosity = verbosity
        self.warnings_are_errors = warnings_are_errors

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
        cmd = ['sphinx-build', '-b', kind, '-c', '.']
        if self.num_jobs:
            cmd += ['-j', str(self.num_jobs)]
        if self.warnings_are_errors:
            cmd += ['-W', '--keep-going']
        if self.verbosity:
            cmd.append('-{}'.format('v' * self.verbosity))
        cmd += ['-d', os.path.join(BUILD_PATH, 'doctrees'),
                DOC_PATH, os.path.join(BUILD_PATH, kind)]
        return subprocess.call(cmd)

    def _open_browser(self, single_doc_html):
        """
        Open a browser tab showing single
        """
        url = os.path.join('file://', DOC_PATH, 'build', 'html',
                           single_doc_html)
        webbrowser.open(url, new=2)


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


def main():
    """Set everything up."""
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
        logging.info('No jobs attribute in jobs.')
        jobs = f'{os.cpu_count()}'

    try:
        verbosity = args.verbosity
    except AttributeError:
        verbosity = None

    logging.debug(jobs)
    builder = args.builder

    if builder is None:
        argparse.ArgumentParser().print_help()

    DocBuilder(num_jobs=jobs, verbosity=verbosity).sphinx_build(kind=builder)

    if os.environ.get('ANDROID_ROOT'):
        termux_hack()


if __name__ == "__main__":
    main()
