#/bin/bash

# so termux and dropbox don't sync automatically. quite honestly I'm sure that
# rclone is faster anyway. let's write a script that does all of this for us.

r1='rclone copy --update --one-file-system --copy-links'
r2='rclone copy --update --track-renames'
# one file system is probably unnecessary and copy links should be optional
r3='rclone copy --update --track-renames --copy-links'

r="$r1"         # or whichever r you want

# projects sync
$r "$HOME/projects/utilities" dropbox:projects/utilities
$r dropbox:projects/utilities "$HOME/projects/utilities"

$r "$HOME/projects/chatistics" dropbox:projects/chatistics
$r dropbox:projects/chatistics "$HOME/projects/chatistics"

# also important to download from dropbox first if we don't have it
$r dropbox:projects/word-freq "$HOME/projects/word-freq"
$r "$HOME/projects/word-freq" dropbox:projects/word-freq

$r dropbox:projects/NewChat "$HOME/projects/NewChat"
$r "$HOME/projects/NewChat" dropbox:projects/NewChat

# .cheat
$r "$HOME/.cheat" dropbox:.cheat
$r dropbox:.cheat "$HOME/.cheat"

# I'm cool with all of python syncing
# gotta love vim with that :26,27s/\.cheat/python/gc
$r "$HOME/python" dropbox:python
$r dropbox:python "$HOME/python" 

# it was this late into the game he realized that --from-file foo.txt existed.
