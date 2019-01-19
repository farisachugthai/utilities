# TODO.md

Not too dissimilar to the world's worst kanban board, this file is going to be a
manually created index for every TODO I write in this repo.

This repository basically started with saying 'Hey that'd be nice to have'.
That continued until I had enough scripts I was happy with to make a git repo
for them!

1. [remove watermarks from itebook](github.com/ShadonSniper/RemoveWatermark)

2. Make a better downloader than the lazy downloader
  - Incorporate ytdl maybe or come up with a gitignore downloader
  - Identify file types based on the header. Also allow to the ability to
    override encoding and MIMEtype. Similar to how requests does it.

3. Either add doctests, logging or unittests [idk yet] to
[dlink.py](https://github.com/farisachugthai/utilities/python/dlink.py) so
that you feel confident enough to begin basing
[dot_sym.ipy](https://github.com/farisachugthai/utilities/python/dot_sym.ipy)
off of it and then begin basing [newbuntu](https://github.com/farisachugthai/newbuntu)
off of that.

4. Make a script that deletes empty dirs in `$PREFIX/tmp.` Termux has 100s now.

5. A script that utilizes
[dlink.py](https://github.com/farisachugthai/utilities/python/dlink.py)
to update the scripts in `~/bin`. Quite annoying to do this manually.

7. This would work best as a vim macro but that would also entail
   learning how to write one. Format a file to 'tldr' formatting. I'm looking
   at you cheat.

8. Rsync and rclone scripts aren't close to done.
  - part of that will be encrypting/archiving your notebooks and pulling
    them down on different devices.

9. Cleanup script for autocorrect.vim and spell files.
    - Luckily vim already has this functionality!
