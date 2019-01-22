# TODO.md

## Linting

- Run `rstcheck` on all of the rst files in ./docs. If you want to do it from
termux you'll need to specify `rstcheck -j 1` because the multiprocessing
module doesn't work.


- Also this needs to be able to pass a standard flake8 lint.

- Then I want a simple unit test suite created for all publicly exported functions.
  - Not a high bar, but a necessary one.

- Either add doctests, logging or unittests to
[dlink.py](https://github.com/farisachugthai/utilities/python/dlink.py) so
that you feel confident enough to begin basing
[dot_sym.ipy](https://github.com/farisachugthai/utilities/python/dot_sym.ipy)
off of it and then begin basing [newbuntu](https://github.com/farisachugthai/newbuntu)
off of that.

- Make a script that deletes empty dirs in `$PREFIX/tmp.` Termux has 100s now.

- A script that utilizes
[dlink.py](https://github.com/farisachugthai/utilities/python/dlink.py)
to update the scripts in `~/bin`. Quite annoying to do this manually.
  - Possibly make this a pre-commit script so that

- Cleanup script for autocorrect.vim and spell files.
    - Luckily vim already has this functionality!

From the help docs:

    SPELLFILE CLEANUP         *spellfile-cleanup*

    The |zw| command turns existing entries in 'spellfile' into comment lines.
    This avoids having to write a new file every time, but results in the file
    only getting longer, never shorter.  To clean up the comment lines in all
    ".add" spell files do this:

    `:runtime spell/cleanadd.vim`

    This deletes all comment lines, except the ones that start with "##".  Use
    "##" lines to add comments that you want to keep.

    You can invoke this script as often as you like.  A variable is provided to
    skip updating files that have been changed recently.  Set it to the number
    of seconds that has passed since a file was changed before it will be
    cleaned. For example, to clean only files that were not changed in the last
    hour:

    `let g:spell_clean_limit = 60 * 60`

    The default is one second.
