#!/bin/sh

SESSION="vscode $(pwd | md5) "

# Either attach to the session I'm already running or start a new one
tmux attach-session -d -t $SESSION || tmux new-session -s $SESSION
# This is a kinda silly way to do this but whatever.
