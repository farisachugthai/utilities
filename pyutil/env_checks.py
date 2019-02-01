#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Run simple checks to ensure that a user's environment has been set up.

Easier to group similar methods in one mod then have them scattered around. 

Below is a generic example of using the public methods to read in user 
defined configurations.

Example
---------

>>> from env_checks import check_xdg_config_home
>>> if check_xdg_config_home:
    >>> with open('module.conf') as f:
        >>> configs = f.readlines()

"""
import os


def check_xdg_config_home():
    """Check to see if $XDG_CONFIG_HOME has been defined.

    Usage
    ------
    TODO
    
    :param: None
    :returns: Bool
    """
    if os.environ.get('XDG_CONFIG_HOME'):
        return True
    else:
        return False


def check_xdg_env():
    """Check to see if $XDG_CONFIG_HOME has been defined.
    
    :param: None
    :returns: Bool
    """
    if os.environ.get('XDG_CONFIG_HOME'):
        return True
    else:
        return False
