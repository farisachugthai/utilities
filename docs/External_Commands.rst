=================
External Commands
=================

.. module:: external_commands

.. highlight:: ipython

All commands in this section rely on another tool or piece of software.

The scripts therein collectively automate use of :command:`git`,
:command:`Neovim`, :command:`conda`, and :mod:`IPython`.


:mod:`g`
=============

.. automodule:: pyutil.g
    :members:
    :noindex:
    :undoc-members:
    :show-inheritance:


Nvim Profiler
=============

.. currentmodule:: nvim_profiling

Attaching to a remote instance from the REPL
--------------------------------------------

The below code displays how to attach to a remote neovim instance.::

    >>> if not os.environ.get('NVIM_LISTEN_ADDRESS'):  # we have no running nvim
        >>> subprocess.run(['nvim&'])  # are we allowed to do this?
    >>> import pynvim
    >>> vim = pynvim.attach('socket', path=os.environ.get('NVIM_LISTEN_ADDRESS'))
    >>> vim.command('edit $MYVIMRC')
    >>> vim_root = vim.current.buffer


Finding the initialization file to profile
------------------------------------------

Here's the help documentation on how to find an ``init.vim`` file 
assuming it's placed in the standard location I.E. ``~/.config/nvim`` or
:envvar:`USERPROFILE`\\AppData\\Local\\nvim.

.. code-block:: vim

    stdpath({what})                 *stdpath()* *E6100*
    Returns |standard-path| locations of various default files and directories.

    {what}       Type    Description ~
    cache        String  Cache directory. Arbitrary temporary
                         storage for plugins, etc.
    config       String  User configuration directory. The
                         |init.vim| is stored here.
    config_dirs  List    Additional configuration directories.
    data         String  User data directory. The |shada-file|
                         is stored here.
    data_dirs    List    Additional data directories.

    Example:
        :echo stdpath("config")


Roadmap
--------

In the future this module is going to move towards implementing a command
that will behave similarly to the following command run in the shell:

.. code-block:: shell-session

    nvim --startuptime test.txt test.py test.txt -c"bn"
    # Also we could make the base command
    nvim --clean --startuptime foo.log example_module.py foo.log -c'bn'


Nvim API Docs
-------------------------

.. automodule:: pyutil.nvim_profiling
    :synopsis: Automate the process of profiling neovim.
    :members:
    :undoc-members:
    :show-inheritance:


Shell
------

.. currentmodule:: pyutil.shell

Base class for shell commands.

Aug 11, 2019:

To make the interface more consistent it may help a lot to
check out the link `here <https://realpython.com/inheritance-composition-python/#an-overview-of-inheritance-in-python>`_.

The lead into the explanation for abstract base classes
particularly was really informative.

In it's current state the Command class is unusable but the 
`BaseCommand` class is interesting and a good starting point.

.. automodule:: pyutil.shell
    :synopsis: Create a base class that other commands can subclass.
    :members:
    :undoc-members:
    :show-inheritance:

