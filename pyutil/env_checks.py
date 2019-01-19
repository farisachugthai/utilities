#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Run simple checks to ensure that a user's environment has been set up.

Easier to group similar methods in one mod then have them scattered around. 

"""
import os


def check_xdg_env():
    """Check to see if $XDG_CONFIG_HOME has been defined.
    
    :param: None
    :returns: Bool
    """
    if os.environ("$XDG_CONFIG_HOME"):
        return True
    else:
