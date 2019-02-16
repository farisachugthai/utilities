#!/usr/bin/env bash
# Maintainer: Faris Chugthai

# set -euo pipefail

# fzf_down: split down: {{{1
fzf_down() {
  fzf --height 50% "$@" --border
}

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
    set | tr = "\t" | fzf | cut -f 1
}

# fzf_nvim: Needs more binds: {{{1
fzf_nvim() {
  local file
  file=$(fzf --query="$1" --select-1 --exit-0)
  [[ -n "$file" ]] && ${EDITOR:-nvim} "$file"
}