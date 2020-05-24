#!/usr/bin/env python
"""Backup a directory by appending the date and time and copying over."""
import os
import subprocess
import sys
from time import strftime


def timestamped_dir(backup_dir, path="."):
    if os.name == "nt":
        shell_command = "move"

    elif os.name == "posix":
        shell_command = "mv"

    else:
        return [-1, "Not supported on %s platform" % os.name]

    cmd = subprocess.Popen(
        [shell_command, path, backup_dir],
        shell=True,
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    (out, err) = cmd.communicate()

    if len(err) != 0:
        return [-1, err]

    else:
        os.mkdir(path)
        return [0, None]


if __name__ == "__main__":
    args = sys.argv[:]

    # if len(args) == 2:

    for directory in args[1:]:
        path = args[directory]

        if os.path.exists(path):
            backup_dir = path + strftime("-%Y-%m-%d-%Hh%Mm%Ss")
            timestamped_dir(backup_dir)
