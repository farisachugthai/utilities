#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Expedite documentation builds.

:mod:`make`
===========

.. module:: make
    :synopsis: Expedite documentation builds.


:File: make.py
:Author: Faris Chugthai
`Github https://github.com/farisachugthai`_

We could, in addition to automatic documentation builds, attempt to automate
installation of the package with subcommands. Uhm well argparse doesn't really
give us that functionality so it'd be more like

:: shell

    python make.py --install

But that works IMO.

Utilizing IPython's Sphinx plugin
---------------------------------
This never occured to me to do this...

.. code-block:: python

    from IPython.sphinxext import ipython_directive, ipython_console_highlighting
    # Then initialize a sphinx instance to pass to the console one
    ipython_console_highlighting.setup(app)

.. todo:: Document initializing a Sphinx instance. Off the top of my head, it
          requires setting src_dir and conf_dir so possibly gonna be easier
          to do in :ref:`conf.py`, but that file exports some constants
          so maybe we'll just scoop them up?


"""
import argparse
import logging
import os
import shlex
# import shutil
import subprocess


def _parse_arguments():
    parser = argparse.ArgumentParser(description=__doc__)

    # parser
    return parser.parse_args()


def run(cmd):
    """Execute the required command in a subshell.

    First the command is splited used typical shell grammer.
    A new process is created, and from the resulting subprocess object,
    the :func:`subprocess.Popen().wait()`. This function returns the return
    code of split ``cmd``, so any non-zero value will lead to a
    ``SystemExit`` with a passed value of ``returncode``.

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
    logging.basicConfig()

    jobs = f'{os.cpu_count()}'

    logging.debug(jobs)

    _args = _parse_arguments()

    # TODO: Check that the f string syntax is correct. Possibly now need to import sys_checks and ensure that we
    # have python > 3.6
    run(f'make -j{jobs}')
    # TODO: Copy the sources over to the right spot. And that static dir I guess.
    # shutil.copytree(src, dst)
