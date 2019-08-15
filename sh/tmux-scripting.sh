#!/usr/bin/env bash
# First attempt at tmux scripting
# Only realizing halfway through that sourcing a configuration file does the same thing.
# Oh well I finally wrote this.

# Prelimenary checks: {{{

if [[ "$1 == -h" || "$1 == --help" ]]; then
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

tmux start-server

if [[ -z $1 && $2 ]]; then
    tmux new-session -s $1 -n $2
elif [[ -z $1 ]]; then
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

<<<<<<< Updated upstream
# Some useful tmux functions

# byobu_prompt_status: From byobu: {{{1
byobu_prompt_status() { local e=$?; [ $e != 0 ] && echo -e "$e "; }

# tm - create new tmux session, or switch to existing one. {{{1
# Works from within tmux too.

# NOTE: Requires fzf

# `tm` will allow you to select your tmux session via fzf.
# `tm irc` will attach to the irc session (if it exists), else it will create it.
tm() {
  [[ -n "$TMUX" ]] && change="switch-client" || change="attach-session"
  if [ $1 ]; then
    tmux $change -t "$1" 2>/dev/null || (tmux new-session -d -s $1 && tmux $change -t "$1"); return
  fi
  session=$(tmux list-sessions -F "#{session_name}" 2>/dev/null | fzf --exit-0) &&  tmux $change -t "$session" || echo "No sessions found."
}

exit 0
# Vim: set foldmethod=marker :
