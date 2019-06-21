#!/usr/bin/env bash
# Maintainer: Faris Chugthai

# set -euo pipefail

# A bunch of these are from the fzf wiki. I've added them to have
# useful functions on $PATH but still want them visually separated

##############
#  Personal  #
##############

# fzf_commits: commits in a repo: {{{1
fzf_commits() {
  git log --pretty=oneline --abbrev-commit | fzf --preview-window=right:50% --preview 'echo {} | cut -f 1 -d " " | xargs git show --color=always' | cut -f 1 -d " "
}

fh() { # {{{1
    git log --color=always --all --branches --abbrev --oneline | fzf --ansi --multi --preview "git show {+1}" --preview-window=down
}

# }}}

# }}}
######################################################################
#                             fzf wiki                               #
######################################################################

git_log() { # {{{1 log piped into less and displays show
  local show="git show --color=always \"\$(grep -m1 -o \"[a-f0-9]\{7\}\" <<< {})\""
  fzf --prompt='log' -e --no-sort --tiebreak=index \
    --bind="enter:execute:$show | less -R" \
    --preview="$show" \
  < <(git log --graph --color=always \
    --format="%C(auto)%h%d %s %C(black)%C(bold)%cr" "$@")
}
# }}}
fbr() { # checkout git branch {{{1
  local branches branch
  branches=$(git branch -vv) &&
  branch=$(echo "$branches" | fzf +m) &&
  git checkout "$(echo "$branch" | awk '{print $1}' | sed "s/.* //")"
}
# }}}
fbr() { # {{{1 checkout git branch (including remote branches). Uses fzf-tmux
  local branches branch
  branches=$(git branch --all | grep -v HEAD) &&
  branch=$(echo "$branches" |
           fzf-tmux -d $(( 2 + $(wc -l <<< "$branches") )) +m) &&
  git checkout "$(echo "$branch" | sed "s/.* //" | sed "s#remotes/[^/]*/##")"
}
# }}}
fbr() { # {{{1 checkout git branch (including remote branches), sorted by most recent commit, limit 30 last branches
  local branches branch
  branches=$(git for-each-ref --count=30 --sort=-committerdate refs/heads/ --format="%(refname:short)") &&
  branch=$(echo "$branches" |
           fzf-tmux -d $(( 2 + $(wc -l <<< "$branches") )) +m) &&
  git checkout "$(echo "$branch" | sed "s/.* //" | sed "s#remotes/[^/]*/##")"
}
# }}}
fco() { # {{{1 checkout git branch/tag
  local tags branches target
  tags=$(
    git tag | awk '{print "\x1b[31;1mtag\x1b[m\t" $1}') || return
  branches=$(
    git branch --all | grep -v HEAD             |
    sed "s/.* //"    | sed "s#remotes/[^/]*/##" |
    sort -u          | awk '{print "\x1b[34;1mbranch\x1b[m\t" $1}') || return
  target=$(
    (echo "$tags"; echo "$branches") |
    fzf-tmux -l30 -- --no-hscroll --ansi +m -d "\t" -n 2) || return
  git checkout "$(echo "$target" | awk '{print $2}')"
}
# }}}
fco_preview() { # {{{1 checkout git branch/tag, with a preview showing the commits between the tag/branch and HEAD
  local tags branches target
  tags=$(
git tag | awk '{print "\x1b[31;1mtag\x1b[m\t" $1}') || return
  branches=$(
git branch --all | grep -v HEAD |
sed "s/.* //" | sed "s#remotes/[^/]*/##" |
sort -u | awk '{print "\x1b[34;1mbranch\x1b[m\t" $1}') || return
  target=$(
(echo "$tags"; echo "$branches") |
    fzf --no-hscroll --no-multi --delimiter="\t" -n 2 \
        --ansi --preview="git log -200 --pretty=format:%s $(echo {+2..} |  sed 's/$/../' )" ) || return
  git checkout "$(echo "$target" | awk '{print $2}')"
}
# }}}
fcoc() { # {{{1 checkout git commit
  local commits commit
  commits=$(git log --pretty=oneline --abbrev-commit --reverse) &&
  commit=$(echo "$commits" | fzf --tac +s +m -e) &&
  git checkout "$(echo "$commit" | sed "s/ .*//")"
}
# }}}
fshow() { # {{{1 git commit browser

    git log --graph --color=always \
        --format="%C(auto)%h%d %s %C(black)%C(bold)%cr" "$@" |
    fzf --ansi --no-sort --reverse --tiebreak=index --bind=ctrl-s:toggle-sort \
        --no-multi --header="Ctrl-s to toggle sort. C-m to execute." \
        --bind "ctrl-m:execute:
                (grep -o '[a-f0-9]\{7\}' | head -1 |
                xargs -I % sh -c 'git show --color=always % | bat -R') << 'FZF-EOF'
                {}
FZF-EOF"
}
# }}}
glNoGraph(){  # An alias I converted into a function. cross your fingers
    git log --color=always --format="%C(auto)%h%d %s %C(black)%C(bold)%cr% C(auto)%an" "$@"
}

# Wait are these backslashes necessary inside of a single quote?
_gitLogLineToHash="echo {} | grep -o '[a-f0-9]\{7\}' | head -1"

_viewGitLogLine="$_gitLogLineToHash | xargs -I % sh -c 'git show --color=always % | diff-so-fancy'"

fcoc_preview() { # {{{ checkout git commit with previews. Probably won't work because we don't have diff-so-fancy
  local commit
  commit=$( glNoGraph |
    fzf --no-sort --reverse --tiebreak=index --no-multi \
        --ansi --preview="$_viewGitLogLine" ) &&
  git checkout "$(echo "$commit" | sed "s/ .*//")"
}
# }}}
fshow_preview() { # {{{ fshow_preview - git commit browser with previews
    glNoGraph "$@" |
        fzf --no-sort --reverse --tiebreak=index --no-multi \
            --ansi --preview="$_viewGitLogLine" \
                --header "enter to view, alt-y to copy hash" \
                --bind "enter:execute:$_viewGitLogLine   | bat - " \
                --bind "alt-y:execute:$_gitLogLineToHash | xclip"
}
# }}}
is_in_git_repo() { # {{{
  git rev-parse HEAD > /dev/null 2>&1
}
# }}}
fgst() { # {{{ pick files from git status -s
  # "Nothing to see here, move along"
  is_in_git_repo || return

  local cmd="${FZF_CTRL_T_COMMAND:-"command git status -s"}"

  eval "$cmd" | FZF_DEFAULT_OPTS="--height ${FZF_TMUX_HEIGHT:-40%} --reverse $FZF_DEFAULT_OPTS $FZF_CTRL_T_OPTS" fzf -m "$@" | while read -r item; do
    printf '%q ' "$item" | cut -d " " -f 2
  done
  echo
}
# }}}
ftags() { # {{{ search ctags
  local line
  [ -e tags ] &&
  line=$(
    awk 'BEGIN { FS="\t" } !/^!/ {print toupper($4)"\t"$1"\t"$2"\t"$3}' tags |
    cut -c1-80 | fzf --nth=1,2
  ) && ${EDITOR:-vim} $(cut -f3 <<< "$line") -c "set nocst" \
                                      -c "silent tag $(cut -f2 <<< "$line")"
}
# }}}
# From Choi's Gist not the wiki.
fzf-down() { # {{{ fzf --height and border
  fzf --height 50% "$@" --border
}
# }}}
fgf() { # {{{ git status - preview diff
  is_in_git_repo || return
  git -c color.status=always status --short |
  fzf-down -m --ansi --nth 2..,.. \
    --preview '(git diff --color=always -- {-1} | sed 1,4d; cat {-1}) | head -500' |
  cut -c4- | sed 's/.* -> //'
}
# }}}
fgb() { # {{{
  is_in_git_repo || return
  git branch -a --color=always | grep -v '/HEAD\s' | sort |
  fzf-down --ansi --multi --tac --preview-window right:70% \
    --preview 'git log --oneline --graph --date=short --pretty="format:%C(auto)%cd %h%d %s" $(sed s/^..// <<< {} | cut -d" " -f1) | head -'$LINES |
  sed 's/^..//' | cut -d' ' -f1 |
  sed 's#^remotes/##'
}
# }}}
fgt() { # {{{
  is_in_git_repo || return
  git tag --sort -version:refname |
  fzf-down --multi --preview-window right:70% \
    --preview 'git show --color=always {} | head -'$LINES
}
# }}}
fgh() { # {{{
  is_in_git_repo || return
  git log --date=short --format="%C(green)%C(bold)%cd %C(auto)%h%d %s (%an)" --graph --color=always |
  fzf-down --ansi --no-sort --reverse --multi --bind 'ctrl-s:toggle-sort' \
    --header 'Press CTRL-S to toggle sort' \
    --preview 'grep -o "[a-f0-9]\{7,\}" <<< {} | xargs git show --color=always | head -'$LINES |
  grep -o "[a-f0-9]\{7,\}"
}
# }}}
fgr() { # {{{1 git remote
  is_in_git_repo || return
  git remote -v | awk '{print $1 "\t" $2}' | uniq |
  fzf-down --tac \
    --preview 'git log --oneline --graph --date=short --pretty="format:%C(auto)%cd %h%d %s" {1} | head -200' |
  cut -d$'\t' -f1
}
# }}}
# Key bindings for each. {{{1
# Definitely go through everything and optimize
bind '"\er": redraw-current-line'
bind '"\C-g\C-f": "$(fgf)\e\C-e\er"'
bind '"\C-g\C-b": "$(fgb)\e\C-e\er"'
bind '"\C-g\C-t": "$(fgt)\e\C-e\er"'
bind '"\C-g\C-h": "$(fgh)\e\C-e\er"'
bind '"\C-g\C-r": "$(fgr)\e\C-e\er"'

# Different gist
fgstash() { # {{{1 preview window for git stashes
  local out k reflog
  out=(
    $(git stash list --pretty='%C(yellow)%gd %>(14)%Cgreen%cr %C(blue)%gs' |
      fzf --ansi --no-sort --header='enter:show, ctrl-d:diff, ctrl-o:pop, ctrl-y:apply, ctrl-x:drop' \
          --preview='git stash show --color=always -p $(cut -d" " -f1 <<< {}) | head -'$LINES \
          --preview-window=down:50% --reverse \
          --bind='enter:execute(git stash show --color=always -p $(cut -d" " -f1 <<< {}) | less -r > /dev/tty)' \
          --bind='ctrl-d:execute(git diff --color=always $(cut -d" " -f1 <<< {}) | less -r > /dev/tty)' \
          --expect=ctrl-o,ctrl-y,ctrl-x))
  k=${out[0]}
  reflog=${out[1]}
  [ -n "$reflog" ] && case "$k" in
    ctrl-o) git stash pop $reflog ;;
    ctrl-y) git stash apply $reflog ;;
    ctrl-x) git stash drop $reflog ;;
  esac
}

# Updated versions of the above. From Choi's bashrc.

fgs() {  # git status through fzf
  is_in_git_repo || return
  git -c color.status=always status --short |
  fzf-down -m --ansi --nth 2..,.. \
    --preview '(git diff --color=always -- {-1} | sed 1,4d; cat {-1}) | head -500' |
  cut -c4- | sed 's/.* -> //'
}

fgb() {  # git branch
  is_in_git_repo || return
  git branch -a --color=always | grep -v '/HEAD\s' | sort |
  fzf-down --ansi --multi --tac --preview-window right:70% \
    --preview 'git log --oneline --graph --date=short --pretty="format:%C(auto)%cd %h%d %s" $(sed s/^..// <<< {} | cut -d" " -f1) | head -200' |
  sed 's/^..//' | cut -d' ' -f1 |
  sed 's#^remotes/##'
}

fgt() {  # tags
  is_in_git_repo || return
  git tag --sort -version:refname |
  fzf-down --multi --preview-window right:70% \
    --preview 'git show --color=always {} | head -200'
}

fgh() {  # hist
  is_in_git_repo || return
  git log --date=short --format="%C(green)%C(bold)%cd %C(auto)%h%d %s (%an)" --graph --color=always |
  fzf-down --ansi --no-sort --reverse --multi --bind 'ctrl-s:toggle-sort' \
    --header 'Press CTRL-S to toggle sort' \
    --preview 'grep -o "[a-f0-9]\{7,\}" <<< {} | xargs git show --color=always | head -200' |
  grep -o "[a-f0-9]\{7,\}"
}

fgrr() {
  is_in_git_repo || return
  git remote -v | awk '{print $1 "\t" $2}' | uniq |
  fzf-down --tac \
    --preview 'git log --oneline --graph --date=short --pretty="format:%C(auto)%cd %h%d %s" {1} | head -200' |
  cut -d$'\t' -f1
}

fgshs() {
  is_in_git_repo || return
  git stash list | fzf-down --reverse -d: --preview 'git show --color=always {1}' |
  cut -d: -f1
}

fgrp() {
    git grep -C 0 --heading --break --word-regex --no-line-number |
    fzf-down --tac --reverse --ansi
}
