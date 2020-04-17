#!/bin/bash

alias tmux="tmux -u"

tmux_check() { # Check if we're inside tmux: {{{1
    if [[ -n $TMUX ]]; then
        echo "You're already in tmux."
        echo -e "Current tmux sessions: \n"
        tmux list-sessions | cut -d " " -f 1

        tmux detach
    fi
}  # }}}

tmux_new_session() {   # {{{1
    tmux start-server;
    if [[ -z $1 && $2 ]]; then
        "tmux new-session -s $1 -n $2"

    elif [[ -z $1 ]]; then
        "tmux new-session -s $1"

    else
        'tmux new-session "-s default" "-n ipython" -d';
        'tmux split-window "|" "-t default"'
    fi
}   # }}}

tmux_new_window() {  # {{{

    # a means append the window number to the previous
    # P means print window info after
    "tmux new-window -aP -n nvim -t default"

    # TODO: How to start running commands. I find that really confusing.
    # the new window command wont work with CLAs. assign it to a var.
    # do so before the loop and the whole thing simplifies
}  # }}}

# byobu_prompt_status: From byobu: {{{
byobu_prompt_status() { local e=$?; [[ "$e" != 0 ]] && echo -e "$e "; }

# }}}

tm() {  #: {{{

    # tm - create new tmux session, or switch to existing one.
    # Works from within tmux too.

    # NOTE: Requires fzf

    # `tm` will allow you to select your tmux session via fzf.

    # Parameters:
    # `tm irc` will attach to the irc session (if it exists), else it will create it.

    # Generalized this mean that `tm arg` will open a named session as arg.
    # additional arguments are currently ignored.

    # Jan 31, 2020: Checking if we're in tmux and starting a session first.
    [[ -z "$TMUX" ]] && test -x byobu  && byobu-tmux -s tm || tmux new-session -s tm && return
    
    [[ -n "$TMUX" ]] && change="switch-client" || change="attach-session"

    if [[ "$1" ]]; then
    
        tmux $change -t "$1" 2>/dev/null || (tmux new-session -d -s "$1" && tmux "$change" -t "$1"); return

    fi
  
    # TODO: dude a preview window would be so cool.
    session=$(tmux list-sessions -F "#{session_name}" 2>/dev/null | fzf --no-multi --exit-0) &&  tmux $change -t "$session" || echo "No sessions found."

}

# Complete this correctly
complete -F _tmux -o default -o bashdefault -o nospace tm

# Vim: set foldmethod=indent foldlevelstart=0:
