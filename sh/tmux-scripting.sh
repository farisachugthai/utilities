#!/usr/bin/env bash
# First attempt at tmux scripting
# Only realizing halfway through that sourcing a configuration file does the same thing.
# Oh well I finally wrote this.

# Prelimenary checks: {{{

if [[ "$1" = "-h" || "--help" ]]; then
  echo -e "Usage: 'bash tmux-scripting.sh session_name window_name' \n"
  echo -e "Current tmux sessions: \n"
  tmux ls
  exit
fi


if [[ -n $TMUX ]]; then
    echo "You're already in tmux."
    echo -e "Current tmux sessions: \n"
    tmux ls
    exit 127
fi
# alternatively could we try tmux suspend-client?

echo -e "If there are active sessions here are their names."
tmux list-sessions | cut -d " " -f 1

echo -e "Alright let's script."
# }}}

tmux start-server

if $1 && $2 then
    tmux new-session -s $1 -n $2
elif $1
    tmux new-session -s $1
else
    tmux new-session -s default -n ipython -d
    tmux split-window | -t default
fi

# the new window command wont work with CLAs. assign it to a var.
# do so before the loop and the whole thing simplifies
# TODO: How to start running commands. I find that really confusing.

# a means append the window number to the previous
# P means print window info after
tmux new-window -aP -n nvim -t default

exit 0

# Vim: set foldmethod=marker :
