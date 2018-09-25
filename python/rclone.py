#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Rewriting rclone.sh as a python module.

Usage::
    TODO

Requires::
    rclone

Useful backup utility.
"""
import argparse
import os
import subprocess
import sys


def _parse_arguments():
    """Parse user-given arguments."""
    parser = argparse.ArgumentParser("Automate usage of rclone for simple backup creation.")
    parser.add_argument(dest=src,

    return parser


def rclone_base_case():
    """Noop. Simply here to track the best command to use."""
    pass


def rclone_follow(src, dest):
    """Follow symlinks."""
    args = ['rclone', 'copy', '--update', '--copy-links', src, dest]
    subprocess.run(args)


if __name__ == "__main__":
    args = _parse_arguments()
    args.parse_args()

    if args.follows:
        rclone_follow(src, dest)
