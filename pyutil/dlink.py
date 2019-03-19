#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Symlink all of the files in one directory into another.

..module:: dlink
    :synopsis: Symlinks a directory of files from another.

Synopsis
--------
This module can be used to create individual symlinks to every file in a
directory. This is a huge convenience wen symlinking dotfiles or configuration
files held in a different location than where the software of interest expects
it.

This is quite easily one of my most frequently used scripts.

As an example, one can ``git clone dotfiles`` in a directory named `projects`
or `src`. The location of the git repository is irrelevant, and as such, we'll
refer to it as `src` from here, as `dest` as it's where the symlinks point to.

For example if wants symlinks pointing to ``/home/User/dotfiles/.vim``,
then running dlink.py in `/home/User/.vim` with $HOME/dotfiles/.vim as
an argument will create symlinks in $HOME/.vim pointing to $HOME/dotfiles/.vim.


Inspiration
------------
If the module is given 2 args, the intended response is for it to behave  similarly to the classic Unix idiom:

.. code-block:: shell

    ln -s path/to/dest/* [path/to/src]

or treat it similarly to :func:`os.symlink()`.

"""
import os
import sys


def dlink(dest, src):
    """Symlinks a directory from another one.

    Parameters
    ----------
    dest: str
        The directory where the original files are located.
    src : str
        Optional argument indicating the directory where the symlinks
        are to be created.
        If the `src` argument isn't provided, it is assumed that the current
        working directory is the `src` dir.


    """
    for i in os.listdir(dest):
        # First let's set up the relative paths for our destination and src
        dest_file = os.path.join(dest, i)
        src_file = os.path.join(src, i)
        if os.path.isdir(dest_file) and not os.path.isdir(src_file):
            # If the first item in dest is a dir, make sure it exists in src
            try:
                os.mkdir(src_file, 0o777)
            except IsADirectoryError:
                # If that dir exists already, move along.
                pass
        elif os.path.isfile(dest_file):
            try:
                os.symlink(dest_file, src_file)
            except Exception as e:
                if os.path.islink(src_file):
                    # If a symlink already exists, then we're okay
                    pass
                elif os.path.isfile(src_file):
                    # If there's a file, complain.
                    print(e)


if __name__ == '__main__':
    cwd = os.path.join(os.getcwd(), '')

    src = sys.argv[-1] if len(sys.argv) == 3 else cwd

    # If we don't get 2 args shut down.
    try:
        dest = sys.argv[1]
    except IndexError:
        sys.exit("What directory do you want to link to?")

    if not os.path.isdir(dest):
        sys.exit("Dir: " + dest + " is not a recognized directory. Exiting.")

    dlink(dest, src)
