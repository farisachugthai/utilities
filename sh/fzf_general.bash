#!/usr/bin/env bash
# Maintainer: Faris Chugthai

# set -euo pipefail

# Feb 26, 2019: Idea on how to decide to use fzf or fzf-tmux: {{{1

# [[ -n $TMUX ]] means not in tmux

# [[ -z $TMUX ]] && comm=fzf-tmux || comm=fzf
# or something to that effect
# Then you could easily go $comm in the place of fzf in different commands

# rg --> fzf --> bat preview with snazyy colors and maximum readability: {{{1
# Mar 17, 2019: Here's a new pipline that I'm pretty proud of! Works actually quite well IMO

# I used \ before fzf to ignore anything i've set with FZF_DEFAULT's
# Realistically I need to start making the options set by the defaults as minimal as possible and then
# just make good pipelines like this and name them something else.

fzfr() {
    rg --no-heading --no-column --no-filename --hidden --files --no-messages | \fzf --ansi --filepath-word --preview='\bat --theme="Sublime Snazzy" --color always --wrap auto --style=plain --pager="less -RF" {}'
}

# fzf_down: split down: {{{1
fzf_down() {
  fzf --height 50% "$@" --border
}

# Move to fzf_git?
# fzf_commits: commits in a repo: {{{1
fzf_commits() {
  git log --pretty=oneline --abbrev-commit | fzf --preview-window=right:50% --preview 'echo {} | cut -f 1 -d " " | xargs git show --color=always' | cut -f 1 -d " "
}

# fzf_apropos: for existing man pages: {{{1
fzf_apropos() {
  apropos '' | fzf --preview-window=right:50% --preview 'echo {} | cut -f 1 -d " " | xargs man' | cut -f 1 -d " "
}

# fzf_env: View EVERYTHING set in your env: {{{1
fzf_env() {
    set | fzf | cut -f 1
}

# fzf_nvim: Needs more binds: {{{1
fzf_nvim() {
  local file
  file=$(fzf --query="$1" --select-1 --exit-0)
  [[ -n "$file" ]] && ${EDITOR:-nvim} "$file"
}
