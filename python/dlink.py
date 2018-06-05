#!/usr/bin/env python3

import os
import sys

# TODO #2 : If you want to add some zest, import glob and let users wildcard it

cwd = os.path.join(os.getcwd(), '')
src = sys.argv[-1] if len(sys.argv) == 3 else cwd
dest = sys.argv[1]
# assert dest is type(string)       # no idea what the real syntax is 

print("Your variable src is: " + src + " and type: " + str(type(src)))
print("Your variable dest is: " + dest + " and type: " + str(type(dest)))
print("The files that we'll be symlinking to are: " + str(os.listdir(dest)))


def dlink(dest, src=cwd):
    """
    Usage:
    Utilize in an analogous way to the shell command
    ln -s path/to/dir/* path/to/src/

    Parameters:
    Dest is the directory where the real files are located.
    src is the directory where the symlinks are to be created.
    If the src argument isn't provided, it is assumed that the current working
    directory is the src dir.
    """

    for i in os.listdir(dest):
        dest_file = os.path.join(dest, i)
        src_file = os.path.join(src, i)
        try:
            os.symlink(dest_file, src_file)
        except FileExistsError as e:
            if os.path.islink(src_file):
                pass
            elif os.path.isdir(src_file):
                pass
            elif os.path.isfile(src_file):
                print(src_file + " is already a file in the src dir. We will not create a symlink.")
                pass
            else:
                print(e)
                sys.exit("Huh. Didn't see that coming.")

        print("symlinking: " + dest_file + " from " + src_file)


def main():
    dlink(dest, src=cwd)


if __name__ == '__main__':
    main()
