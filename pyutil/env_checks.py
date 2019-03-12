#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Run simple checks to ensure that a user's environment has been set up.

Easier to group similar methods in one mod then have them scattered around.

Below is a generic example of using the public methods to read in user
defined configurations.

.. rubric:: Example

.. code-block:: python3

    >>> from env_checks import check_xdg_config_home
    >>> if check_xdg_config_home():
        >>> with open('module.conf', 'rt') as f:
            >>> configs = f.readlines()


Matplotlib Env Checks
---------------------
Mar 08, 2019

Just noticed today the following functions::

    try:
        import matplotlib as mpl
    except ImportError:
        pass
    mpl.get_home()
    mpl._get_xdg_cache_dir()
    mpl._get_xdg_config_dir()
    mpl._get_data_path()


Here's an interesting way to memoize return values.::

    def _logged_cached(fmt, func=None):
        \"\"\"
        Decorator that logs a function's return value, and memoizes that value.

        After ::

            @_logged_cached(fmt)
            def func(): ...

        the first call to *func* will log its return value at the DEBUG level using
        %-format string *fmt*, and memoize it; later calls to *func* will directly
        return that value.
        \"\"\"
        if func is None:  # Return the actual decorator.
            return functools.partial(_logged_cached, fmt)

        called = False
        ret = None

        @functools.wraps(func)
        def wrapper():
            nonlocal called, ret
            if not called:
                ret = func()
                called = True
                _log.debug(fmt, ret)
            return ret

        return wrapper


"""
import os


def check_xdg_config_home():
    """Check to see if ``$XDG_CONFIG_HOME`` has been defined.

    Returns
    -------
    bool

    Returns
    -------
    Bool

        >>> from env_checks import check_xdg_config_home
        >>> if check_xdg_config_home():
            >>> with open('module.conf', 'rt') as f:
                >>> configs = f.readlines()

    """
    if os.environ.get('XDG_CONFIG_HOME'):
        return True
    else:
        return False


def get_script_dir():
    """Determine the directory the script is in.

    Returns
    -------
    Directory the file is in : str

    """
    return os.path.dirname(os.path.realpath(__file__))


def env_check(env_var):
    """Search the current namescope for variable env_var.

    Parameters
    ----------
    env_var : str
        Environment variable to search for. Currently case-sensitive.

    Yields
    ------
    i : dict_key
        The environment variable searched for. Env vars are mapped as dicts.

    Example
    -------
    .. code-block:: python3

        >>> from env_checks import env_check
        >>> fzf = list(env_check('fzf'))
        [
                '_fzf_orig_completion_awk', '_fzf_orig_completion_cat',
                '_fzf_orig_completion_cd', '_fzf_orig_completion_cp',
                '_fzf_orig_completion_diff', '_fzf_orig_completion_du',
                '_fzf_orig_completion_ftp', '_fzf_orig_completion_grep',
                '_fzf_orig_completion_head', '_fzf_orig_completion_ld',
                '_fzf_orig_completion_less', '_fzf_orig_completion_ln',
                '_fzf_orig_completion_ls', '_fzf_orig_completion_mv',
                '_fzf_orig_completion_pushd', '_fzf_orig_completion_rm',
                '_fzf_orig_completion_rmdir', '_fzf_orig_completion_sed',
                '_fzf_orig_completion_sort', '_fzf_orig_completion_tail',
                '_fzf_orig_completion_tee', '_fzf_orig_completion_telnet',
                '_fzf_orig_completion_uniq', '_fzf_orig_completion_wc'
                ]

    """
    for i in sorted(dict(os.environ)):
        if i.find(env_var) > 0:
            yield i
