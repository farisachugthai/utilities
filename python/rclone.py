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


def parse_arguments():
    """Parse user-given arguments."""
    pass


def rclone_base_case():
    """Noop. Simply here to track the best command to use."""
    pass


def rclone_follow(src, dest):
    """Follow symlinks."""
    args = ['rclone', 'copy', '--update', '--copy-links', src, dest]
    subprocess.run(args)


if __name__ == "__main__":
    rclone_follow(src, dest)
