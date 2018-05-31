#/bin/bash

# so termux and dropbox don't sync automatically. quite honestly I'm sure that
# rclone is faster anyway. let's write a script that does all of this for us.

r='rclone copy --update --one-file-system --copy-links'

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
$r dropbox:.chest "$HOME/.cheat"

# I'm cool with all of python syncing
# gotta love vim with that :26,27s/\.cheat/python/gc
$r "$HOME/python" dropbox:python
$r dropbox:python "$HOME/python" 

# this should be good. get to a point where there are no symlinks 
# to dropbox it honestly doesn't work!!
# then configure for encryption. definitely do your research beforehand!!
