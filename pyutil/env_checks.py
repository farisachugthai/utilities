#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Run simple checks to ensure that a user's environment has been set up.

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
        '''
        Decorator that logs a function's return value, and memoizes that value.

        After ::

            @_logged_cached(fmt)
            def func(): ...

        the first call to *func* will log its return value at the DEBUG level using
        %-format string *fmt*, and memoize it; later calls to *func* will directly
        return that value.
        '''
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
import getpass
from pathlib import Path

# unix only
try:
    import pwd as _pwd
except ModuleNotFoundError:
    pass


def check_xdg_config_home():
    """Check to see if :envvar:`$XDG_CONFIG_HOME` has been defined.

    Returns
    -------
    Bool

    Examples
    --------
    .. code-block:: python3

        >>> from env_checks import check_xdg_config_home
        >>> if check_xdg_config_home():
            >>> with open('module.conf', 'rt') as f:
                >>> configs = f.readlines()

    """
    if os.environ.get('XDG_CONFIG_HOME'):
        return True


def get_script_dir(fobj):
    """Determine the directory the script is in.

    Parameters
    ----------
    fobj : str
        Path to file to check

    Returns
    -------
    Directory the file is in : str

    """
    return os.path.dirname(os.path.realpath(fobj))


def env_check(env_var):
    """Search the current namescope for variable `env_var`.

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


def get_home_3():
    """Return the user's home directory. Python3 only!

    Returns
    -------
    home : :class:`pathlib.Path`
        The user's home directory. Utilizes pathlib so requires Python 3.
        Returns `None` if the home directory isn't found.

    """
    try:
        return Path.home()
    except Exception:
        return None


def check_xdg_config_home_2(conf_file=None):
    """An implementation of check_xdg_config_home that works with Python2!

    Unfortunately the code is quite repetitive as it stands and needs refactoring.

    .. admonition:: Has not been tested on Python2.

    Parameters
    ----------
    conf_file : str, optional
        Path to a configuration file needed by another module.

    Returns
    -------
    user_conf_file : str
        Path to desired user configuration file. Returns None if the file can't
        be found.

    """
    xdg_config_home = os.getenv('XDG_CONFIG_HOME')
    if xdg_config_home:
        if conf_file:
            user_conf_file = os.path.join(xdg_config_home, conf_file)
            if os.path.isfile(user_conf_file):
                return user_conf_file
    else:
        xdg_config_dir = os.path.isdir(
            os.path.join(os.path.expanduser('~'), '.config'))
        if xdg_config_dir:
            if conf_file:
                user_conf_file = os.path.join(xdg_config_dir, conf_file)
                if os.path.isfile(user_conf_file):
                    return user_conf_file


def get_unix_username():
    """Get username. Unix only!

    Returns
    -------
    username : str
        User username

    """
    return _pwd.getpwuid(os.getuid()).pw_name


def get_username():
    """More cross-platform implementation of retrieving a username.


   This function checks the environment variables :envvar:`LOGNAME`,
   :envvar:`USER`, :envvar:`LNAME` and :envvar:`USERNAME`, in order, and
   returns the value of the first one which is set to a non-empty string.  If
   none are set, the login name from the password database is returned on
   systems which support the :mod:`pwd` module, otherwise, an exception is
   raised.

    In general, this function should be preferred over :func:`os.getlogin()`.
    """
    return getpass.getuser()
