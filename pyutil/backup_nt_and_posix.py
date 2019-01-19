<<<<<<< .merge_file_1nAd0d
#!/usr/bin/env python3
"""Backup a directory by appending the date and time and copying over.

This script aims to be platform agnostic and in the long term will be used
on Windows, Linux, Mac and Android systems.

Original URL::
    `<http://pythonprogramming.language-tutorial.com/2012/10/fast-and-efficient-backup-script-that.html>`

Usage::
    python3 backup-nt-and-posix.py /path/to/dir

"""
import os
import os.path
import subprocess
import time


def backUpDir(path):
    """Create a backup of a directory. Use the date and time as new name.

    Returns:
        None: means no error occurred.
        0: to signify the success
        -1 : to signify the failure
        error string: the exact error string

    """
    if os.path.exists(path):
        # dir exists then backup old dir and create new
        backupDir = path + time.strftime('-%Y-%m-%d-%Hh%Mm%Ss')
        if os.name == "nt":
            # TODO: Does nt encapsulate all windows computers? DOS? win32/win64?
            # Am I thinking in the wrong language?
            # NT System  - used the DOS Command 'move' to rename the folder
            cmd = subprocess.Popen(
                ["move", path, backupDir],
                shell=True,
                stdout=subprocess.PIPE,
                stdin=subprocess.PIPE,
                stderr=subprocess.PIPE)
        elif os.name == "posix":
            # POSIX System - use, start_new_session=False, pass_fds=(),
            # encoding=None, errors=None)
            cmd = subprocess.Popen(
                ["mv", path, backupDir],
                shell=True,
                stdout=subprocess.PIPE,
                stdin=subprocess.PIPE,
                stderr=subprocess.PIPE)
        else:
            # Not supported on other platforms. // I mean is that true?
            # What systems would we not be able to support? Should work perfectly
            # On Macs and Androids. Without a device I can't confirm iphones but
            # I see no reason why not. TODO:
            return [-1, "Not supported on %s platform" % (os.name)]
        (out, err) = cmd.communicate()
        if len(err) != 0:
            return [-1, err]
        else:
            os.mkdir(path)
            return [0, None]
    else:
        os.mkdir(path)
        return [0, None]
||||||| .merge_file_ACQl8K
=======
#!/usr/bin/env python
"""Backup a directory by appending the date and time and copying over.

Motivation
============

This script aims to be platform agnostic and in the long term will be used
on Windows, Linux, Mac and Android systems.

Usage
------

.. code::

    python backup_nt_and_posix.py /path/to/dir

"""
import os
import subprocess
from time import strftime


def backUpDir(path):
    """Create a backup of a directory. Use the date and time as new name.

    Returns:
        None: means no error occurred.
        0: to signify the success
        -1 : to signify the failure
        error string: the exact error string

    """
    if os.path.exists(path):

        # dir exists then backup old dir and create new
        backup_dir = path + strftime('-%Y-%m-%d-%Hh%Mm%Ss')

        # Windows Specific Implementation
        if os.name == "nt":
            cmd = subprocess.Popen(
                ["move", path, backup_dir],
                shell=True,
                stdout=subprocess.PIPE,
                stdin=subprocess.PIPE,
                stderr=subprocess.PIPE)

        # POSIX
        elif os.name == "posix":
            cmd = subprocess.Popen(
                ["mv", path, backup_dir],
                shell=True,
                stdout=subprocess.PIPE,
                stdin=subprocess.PIPE,
                stderr=subprocess.PIPE)
        else:
            return [-1, "Not supported on %s platform" % (os.name)]

        (out, err) = cmd.communicate()

        if len(err) != 0:
            return [-1, err]

        else:
            os.mkdir(path)
            return [0, None]

    else:
        os.mkdir(path)
        return [0, None]
>>>>>>> .merge_file_yNBSBt
