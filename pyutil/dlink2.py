#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
=========================
Directory Linker Rewrite
=========================

This is a rewrite of a script I've had for years, so I decided to go above
and beyond.

The idea behind it was to create something that would easily allow for
creating arbitrarily nested trees of symlinks.

.. todo:: Sep 17, 2019: Recursive option

    Currently doesnt work.

.. todo:: Logging doesnt log the right files.

"""
import argparse
import logging
import sys
from pathlib import Path

try:
    from IPython.core.error import UsageError
except (ImportError, ModuleNotFoundError):

    class UsageError(Exception):
        pass

    # TODO
    # def ensure_dir_exists(dir):

try:
    from pyutil.__about__ import __version__
except (ImportError, ModuleNotFoundError):
    __version__ = None


class PermissionsError(OSError):
    """Symlinking error typically from Windows."""

    def __call__(self, tb=None):
        if tb:
            return "{}".format(tb)


def _parse_arguments():
    parser = argparse.ArgumentParser(
        prog="Directory Linker 2.0",
        description="Iterate over a `dest` folder"
        " and create symlinks in directory "
        "`source`. If `source` is not provided use"
        " current working directory.",
    )

    parser.add_argument(
        "destination",
        metavar="destination",
        nargs="?",
        type=Path,
        help="Files to symlink to.",
    )

    parser.add_argument(
        "-s",
        "--source_directory",
        metavar="SOURCE_DIRECTORY",
        dest="source",
        nargs="?",
        default=Path().cwd(),
        help="Where to create the symlinks. Defaults to the cwd.",
    )

    parser.add_argument(
        "-g",
        "--glob-pattern",
        metavar="GLOB_PATTERN",
        default=None,
        help="Filter files in the destination dir with a glob pattern."
        " This ensures that only files that match GLOB_PATTERN in `dst`"
        " are symlinked in `src`.",
    )

    # so apparently without the metavar argument, args won't show their var
    # name in the help message?
    parser.add_argument(
        "-r",
        "--recursive",
        action="store_const",
        # nargs='?',
        default=False,
        const=True,
        metavar="RECURSIVE",  # and it causes an error too!
        help="Whether to recursively symlink the files in"
        " child directories below the destination folder as well.",
    )

    if __version__:
        parser.add_argument(
            "-V", "--version", action="version", version="%(prog)s" + __version__
        )

        if len(sys.argv) == 1:
            parser.print_help()
            sys.exit()

    return parser


def generate_dest(dest, glob_pattern=None):
    """Return a generator for all the files in the destination directory."""
    if not hasattr(dest, "iterdir"):
        dest = Path(dest)
    if not dest.exists():
        try:
            dest.mkdir()
        except PermissionsError:
            logging.error("Permissions issue in source directory."
                          "Can't create needed directories for recursive symlinks.")
        except OSError:
            logging.error("%s" % dest, exc_info=1)
    if glob_pattern:
        yield Path(dest).glob(glob_pattern)
    else:
        yield Path(dest).glob("*")


def get_basenames(directory):
    """Get the basenames of all the files in a directory."""
    if not hasattr(directory, "iterdir"):
        directory = Path(directory)
    return [i.stem + i.suffix for i in directory.iterdir()]


def dlink(destination_dir, source_dir=None, is_recursive=False, glob_pattern=None):
    """Symlink user provided files.

    The module doesn't immediately check for correct permissions or
    operating system.

    As a result, the onus is put on the user to ensure that the necessary
    requirements per OS are met.

    Namely on Windows 10, that if symlinks are allowed on the filesystem,
    whether they can only be created by an administrator. Recent enough
    versions of Windows 10 have introduced the ability for regular users
    to create symlinks as well as admins.

    Parameters
    ----------
    destination_dir : str
         Directory where symlinks point to.
    source_dir : str, optional
        Directory where symlinks are created.
    recursive : bool, optional
        Whether to recursively symlink directories beneath the
        `destination_dir`. Defaults to False.
    glob_pattern : str
        Only symlink files that match a certain pattern.

    """
    if source_dir is None:
        source_dir = Path.cwd()
    base_destination_files = sorted(get_basenames(destination_dir))

    if not hasattr(destination_dir, "iterdir"):
        destination_dir = Path(destination_dir)

    full_destination_files = sorted([j for j in destination_dir.iterdir()])

    full_source_files = sorted(
        Path(source_dir).joinpath(i) for i in base_destination_files
    )

    for idx, src_file in enumerate(full_source_files):
        logging.debug("\ni is {0!s}".format(src_file))
        # moat useful but way too long
        # logging.info("\nfull_destination_files is {!s}".format(full_destination_files))
        logging.debug("\nfull_source_files is {!s}".format(full_source_files))
        logging.debug("\nsource_dir is {}".format(source_dir))
        logging.debug("\nbase_destination_files: {!r}".format(base_destination_files))
        logging.debug("idx: {}\tsrc_file: {}\t".format(idx, src_file))
        if full_destination_files[idx].is_dir():
            src_dir = Path(src_file)
            if not src_dir.exists():
                src_dir.mkdir(0o755)

            # then call it recursively
            if src_file.is_dir():
                dlink(
                    destination_dir=src_file,
                    source_dir=source_dir.joinpath(src_file),
                    is_recursive=is_recursive,
                    glob_pattern=glob_pattern,
                )

        else:
            symlink(src_file, full_destination_files[idx])


def symlink(src, dest):
    """Execute the symlinking part of this."""
    try:
        src.symlink_to(dest)
    except FileExistsError:
        pass
    except OSError as e:
        # let's be a little more specific
        # except WindowsError: breaks linux
        raise PermissionsError(
            "{}".format(e) + "Ensure that you are running this script as an admin"
            " when running on Windows!"
        )


def main():
    """Call :func:`_parse_arguments` and the :func:`dlink` function."""
    logging.basicConfig(level=logging.INFO)
    user_arguments = _parse_arguments()
    args = user_arguments.parse_args()

    dest = args.destination

    if not dest.is_dir():
        sys.exit("Provided target not a directory. Exiting.")

    src = args.source or Path().cwd

    try:
        glob_search = args.glob_pattern
    except AttributeError:
        glob_search = None

    try:
        recursive = args.recursive
    except AttributeError:
        recursive = False

    dlink(dest, source_dir=src, is_recursive=recursive, glob_pattern=glob_search)


if __name__ == "__main__":
    main()
