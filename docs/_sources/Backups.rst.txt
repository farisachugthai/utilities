================
Backup Utilities
================

.. module:: backups
    :synopsis: Move files from the home directory to the dotfiles repo.

All of the following modules are used for creating backups
for files in as painless a way as possible.

:mod:`mv_to_repo`
=================

Move files from the home directory to the dotfiles repo.

.. currentmodule:: pyutil.mv_to_repo

This is a script I've been using for the better part of a year, so while
the docstring formatting isn't consistent and there are a couple odd
sections, this script has served a very utilitarian purpose.

May refactor one day. But it continues to work.

.. note::
   This module assumes a python interpreter above version 3.4.


:mod:`backup_nt_and_posix`
==========================

.. module:: pyutil.backup_nt_and_posix
   :synopsis: Back up directories in a platform agnostic manner.


Motivation
----------
This script aims to be platform agnostic and in the long term will be used on
Windows, Linux, Mac and Android systems.

.. function:: timestamped_dir

    Create a backup of a directory. Append date and time to new dir name.

    .. todo::

      Change this so that it utilizes :func:`subprocess.check_call()` so we handle return codes in a better way.


   :param backup_dir: Directory to backup
   :type backup_dir: str
   :param path: Directory to back up to. Defaults to cwd.
   :type path: str, optional

   :returns response: (err_code, err_msg)
      Non-zero value indicates error code, or zero on success.
      Human readable error message, or None on success.
   :type response: tuple (int, str or None)



:mod:`rclone`
====================

.. automodule:: pyutil.rclone
    :members:
    :undoc-members:
    :show-inheritance:

