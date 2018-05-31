#!/usr/bin/env python3
#
# Script that moves all files and directories out of one dir and
# puts everything in another dir
# Interactive for the time being
# Found on Stack Overflow
# Doesn't distinguish between files or directories, and OS-agnostic
# Maintained by Faris Chugthai

import os, shutil

src = input("What is the path of the directory you would like to move?")
# Should create an error if not given a string.
dest = input("What is the path of the directory you want to move to?")

for f in os.listdir(src):
    try:
        shutil.rmtree(dest)
    except NotADirectoryError:
        try:
            os.unlink(dest)
        except FileNotFoundError:
            pass
    shutil.move(src, dest)
