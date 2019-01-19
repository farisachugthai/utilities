<<<<<<< .merge_file_ZJhGQH
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Symlink all of the files in one directory into another.

Double check that this is a directive.
Usage::

    `ln -s path/to/dest/* [path/to/src]`

"""
import os
import sys


def dlink(dest, src):
    """Symlinks a directory from another one.

    Utilize in an analogous way to Unix idiom `ln -s path/to/dir/*`

    :param dest: The directory where the original files are located.
    :param src: Optional argument indicating the directory where the symlinks
    are to be created.

    If the src argument isn't provided, it is assumed that the current working
    directory is the src dir.

    Returns:
        None
    """
    for i in os.listdir(dest):
        # First let's set up the relative paths for our destination and src
        dest_file = os.path.join(dest, i)
        src_file = os.path.join(src, i)
        if os.path.isdir(dest_file) and not os.path.isdir(src_file):
            # If the first item in dest is a dir, make sure it exists in src
            try:
                os.mkdir(src_file, 0o777)
            except IsADirectoryError as e:
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

    # If we're given 2 args, treat it with the same syntax as ln -s or os.symlink
    src = sys.argv[-1] if len(sys.argv) == 3 else cwd

    # If we don't get 2 args shut down.
    try:
        dest = sys.argv[1]
    except IndexError:
        sys.exit("What directory do you want to link to?")

    if not os.path.isdir(dest):
        sys.exit("Dir: " + dest + " is not a recognized directory. Exiting.")

    dlink(dest, src)
||||||| .merge_file_sOZEJY
=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Symlink all of the files in one directory into another.

Usage::

    `ln -s path/to/dest/* [path/to/src]`

"""
import os
import sys


def dlink(dest, src):
    """Symlinks a directory from another one.

    Utilize in an analogous way to Unix idiom::
        `ln -s path/to/dir/*`

    :param dest: The directory where the original files are located.
    :param src: Optional argument indicating the directory where the symlinks
    are to be created.

    If the src argument isn't provided, it is assumed that the current working
    directory is the src dir.

    :return: None
    """
    for i in os.listdir(dest):
        # First let's set up the relative paths for our destination and src
        dest_file = os.path.join(dest, i)
        src_file = os.path.join(src, i)
        if os.path.isdir(dest_file) and not os.path.isdir(src_file):
            # If the first item in dest is a dir, make sure it exists in src
            try:
                os.mkdir(src_file, 0o777)
            except IsADirectoryError as e:
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

    # If we're given 2 args, treat it with the same syntax as ln -s or os.symlink
    src = sys.argv[-1] if len(sys.argv) == 3 else cwd

    # If we don't get 2 args shut down.
    try:
        dest = sys.argv[1]
    except IndexError:
        sys.exit("What directory do you want to link to?")

    if not os.path.isdir(dest):
        sys.exit("Dir: " + dest + " is not a recognized directory. Exiting.")

    dlink(dest, src)
>>>>>>> .merge_file_jGCPrG
