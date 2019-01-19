# TODO.md

Not too dissimilar to the world's worst kanban board, this file is going to be a
manually created index for every TODO I write in this repo.

<<<<<<< .merge_file_UrsAQ3
Jan 16, 2019

- Stop using numbers its hard to reorder.
{Or start using Voom?}

- Run `rstcheck.py` on every rst file in ./docs. Can't do it from termux because
  python's multiprocessing module errors out.

**12/17/18**

So everything in this list is getting pushed down a notch.

What we need to do is get this entire directory to the point where it can pass a cursory flake8 lint.
Then I want a simple unit test suite created for all publicly exported functions.
Not a high bar, but an absolutely necessary one.
||||||| .merge_file_KmHQlY
**12/17/18**

So everything in this list is getting pushed down a notch.

What we need to do is get this entire directory to the point where it can pass a cursory flake8 lint.

Then I want a simple unit test suite created for all publicly exported functions.

Not a high bar, but an absolutely necessary one.
=======
This repository basically started with saying 'Hey that'd be nice to have'.
That continued until I had enough scripts I was happy with to make a git repo
for them!
>>>>>>> .merge_file_cS3X8M

2. Make a better downloader than the lazy downloader
  - Incorporate ytdl maybe or come up with a gitignore downloader
  - Identify file types based on the header. Also allow to the ability to
    override encoding and MIMEtype. Similar to how requests does it.

<<<<<<< .merge_file_UrsAQ3
3. Either add doctests, logging or unittests [IDK yet] to
[dlink.py](https://github.com/farisachugthai/utilities/python/dlink.py) so
that you feel confident enough to begin basing
[dot_sym.ipy](https://github.com/farisachugthai/utilities/python/dot_sym.ipy)
off of it and then begin basing [newbuntu](https://github.com/farisachugthai/newbuntu)
off of that.

4. Make a script that deletes empty dirs in `$PREFIX/tmp.` Termux has 100s now.
||||||| .merge_file_KmHQlY
3. Either add doctests, logging or unittests [idk yet] to [dlink.py](https://github.com/farisachugthai/utilities/python/dlink.py) so
that you feel confident enough to begin basing [dot_sym.ipy](https://github.com/farisachugthai/utilities/python/dot_sym.ipy) off of
it and then begin basing [newbuntu](https://github.com/farisachugthai/newbuntu) off of that.

4. Make a script that deletes empty dirs in `$PREFIX/tmp.` Termux has like 100
   of them now.
=======
3. Either add doctests, logging or unittests [idk yet] to
[dlink.py](https://github.com/farisachugthai/utilities/python/dlink.py) so
that you feel confident enough to begin basing
[dot_sym.ipy](https://github.com/farisachugthai/utilities/python/dot_sym.ipy)
off of it and then begin basing [newbuntu](https://github.com/farisachugthai/newbuntu)
off of that.
>>>>>>> .merge_file_cS3X8M

<<<<<<< .merge_file_UrsAQ3
5. A script that utilizes
[dlink.py](https://github.com/farisachugthai/utilities/python/dlink.py)
to update the scripts in `~/bin`. Quite annoying to do this manually.
  - Should this be a pre-commit script?
||||||| .merge_file_KmHQlY
5. A script that utilizes dlink to update the scripts in `~/bin`.
  Quite annoying to do this manually.
=======
4. Make a script that deletes empty dirs in `$PREFIX/tmp.` Termux has 100s now.
>>>>>>> .merge_file_cS3X8M

<<<<<<< .merge_file_UrsAQ3
6. This would work best as a vim macro but that would also entail
||||||| .merge_file_KmHQlY
6. A script where if a file doesn't have a filename extension, rename it to do
   so.
   Take a CLA to specify what extension.
   Start by doing every file in a dir. Work up to recursion.

7. Maybe this would work best as a vim macro but that woild also entail
=======
5. A script that utilizes
[dlink.py](https://github.com/farisachugthai/utilities/python/dlink.py)
to update the scripts in `~/bin`. Quite annoying to do this manually.

7. This would work best as a vim macro but that would also entail
>>>>>>> .merge_file_cS3X8M
   learning how to write one. Format a file to 'tldr' formatting. I'm looking
   at you cheat.

7. Rsync and rclone scripts aren't close to done.
  - part of that will be encrypting/archiving your notebooks and pulling
    them down on different devices.
