#!/usr/bin/env python3
# From:
# http://pythonprogramming.language-tutorial.com/2012/10/fast-and-efficient-backup-script-that.html

import os
import os.path
import subprocess
import time


def backUpDir(path):
    """
    Creates a backup of a directory.
    Uses the date and time as the name of the new file.
    On success, returns a list consising of two values:
        0: to signify the success
        None: means no error occurred.

    On error, return a list consisting of two values:
        -1 : to signify the failure
        error string: the exact error string
    """

    if os.path.exists(path) is True:
        # dir exists then backup old dir and create new
        backupDir = path + time.strftime('-%Y-%m-%d-%Hh%Mm%Ss')
        if os.name == "nt":
            # NT Sysyem  - used the DOS Command 'move' to rename the folder
            cmd = subprocess.Popen(
                ["mov", path, backupDir],
                shell=True,
                stdout=subprocess.PIPE,
                stdin=subprocess.PIPE,
                stderr=subprocess.PIPE)
        elif os.name == "posix":
            # POSIX System - use, start_new_session=False, pass_fds=(), encoding=None, errors=None)
            cmd = subprocess.Popen(
                ["mv", path, backupDir],
                shell=True,
                stdout=subprocess.PIPE,
                stdin=subprocess.PIPE,
                stderr=subprocess.PIPE)
            pass
        else:
            # Not supported on other platforms
            return [-1, "Not supported on %s platform" % (os.name)]
        (out, err) = cmd.communicate()
        if len(err) != 0:
            return [-1, err]
        else:
            os.mkdir(path)
            return [0, None]
    else:
        # create new dir
        os.mkdir(path)
        return [0, None]
