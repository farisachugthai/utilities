#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Maintainer: Faris Chugthai

import sys
import os
from os import path

import mv_to_repo

home = path.join(os.expanduser("~"), "")


# TODO: Maybe import a good backup function if you have one around.
# Ooo and if you ever work out something good with globbing on that
# other file
def explicit_mv():
    pass
# TODO


def assume_mv():
    pass
# TODO


def main():
    if len(sys.argv) == 3:
        explicit_mv()
    elif len(sys.argv) == 2:
        assume_mv()
    else:
        sys.exit("Usage: ")


if __name__ == '__main__':
    try:
        dest: 'Path' = sys.argv[2]
    except IndexError as e:
        dest = path.join(home, "projects", "dotfiles", "unix")
        # The program doesn't have to crash just assume
    else:
        inputted: 'Path' = sys.argv[1]

    mv_to_repo.sys_checks()
    mv_to_repo.repo_dir_check()
    main()
