#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""From the package "python3.6-examples" in the Ubuntu repositories.

Minor modifications for :mod:`flake8`, :mod:`pydocstyle` etc.

Mar 10, 2019:

    Added logging.

Make a copy of a directory tree with symbolic links to all files in the
original tree.

All symbolic links go to a special symbolic link at the top, so you
can easily fix things if the original source tree moves.

This would probably get a huge improvement in readability from pathlib.

See Also
--------
mkreal


"""
import argparse
import logging
import os
from pathlib import Path
import sys

logger = logging.getLogger(name=__name__)


def _parse_arguments():
    """Handle user inputs."""
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument('oldtree',
                        metavar='oldtree',
                        type=Path,
                        help='Starting directory tree to symlink'
                        'from.')

    parser.add_argument('newtree',
                        metavar='newtree',
                        type=Path,
                        help='Directory tree to symlink to ')

    parser.add_argument('-l', dest='linkto', metavar='linkto', help='Linkto')

    args = parser.parse_args()

    if not 3 <= len(sys.argv) <= 4:
        parser.print_help()

    return args


def _check_existence(directory):
    """Check that a directory exists."""
    return directory.isdir()


def main():
    """Handle user inputs and initialize arguments."""
    oldtree, newtree = sys.argv[1], sys.argv[2]

    if len(sys.argv) > 3:
        link = sys.argv[3]
        link_may_fail = 1
    else:
        link = LINK
        link_may_fail = 0

    if not os.path.isdir(oldtree):
        logging.warning(oldtree + ': not a directory')
        return 1

    try:
        os.mkdir(newtree, 0o777)
    except OSError as msg:
        logging.warning(newtree + ': cannot mkdir:', msg)
        return 1
    linkname = os.path.join(newtree, link)
    try:
        os.symlink(os.path.join(os.pardir, oldtree), linkname)
    except OSError as msg:
        if not link_may_fail:
            logging.warning(linkname + ': cannot symlink:', msg)
            return 1
        else:
            logging.warning(linkname + ': warning: cannot symlink:', msg)
    linknames(oldtree, newtree, link)
    return 0


def linknames(old, new, link):
    """Recursively symlink a directory tree."""
    if DEBUG:
        logging.info('linknames', str(old, new, link))

    try:
        names = os.listdir(old)
    except OSError as msg:
        logging.warning(old + ': warning: cannot listdir:', msg)

    for name in names:
        if name not in (os.curdir, os.pardir):
            oldname = os.path.join(old, name)
            linkname = os.path.join(link, name)
            newname = os.path.join(new, name)
            if DEBUG > 1:
                logging.debug(oldname, newname, linkname)
            if os.path.isdir(oldname) and \
               not os.path.islink(oldname):
                try:
                    os.mkdir(newname, 0o777)
                    ok = 1
                except Exception as msg:
                    logging.warning(newname + ': warning: cannot mkdir:', msg)
                    ok = 0
                if ok:
                    linkname = os.path.join(os.pardir, linkname)
                    linknames(oldname, newname, linkname)
            else:
                os.symlink(linkname, newname)


if __name__ == '__main__':
    logger.setLevel(logging.WARNING)

    LINK = '.LINK'  # Name of special symlink at the top.

    DEBUG = 0

    sys.exit(main())
