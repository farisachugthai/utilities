#!/bin/bash
# Maintainer: Faris Chugthai

is_in_git_repo() { # {{{1
  git rev-parse HEAD > /dev/null 2>&1
} # }}}

fzf-down() {  # {{{
  fzf --height 50% "$@" --border
}  # }}}

fgco() { # {{{1 checkout git commit
  is_in_git_repo || return
  local commits commit
  commits="$(git log --pretty=oneline --abbrev-commit --reverse)" &&
  commit=$(echo "$commits" | fzf --tac +s +m -e) &&
  git checkout "$(echo $commit | sed s/ .*//)"
} # }}}

fshow_preview() { # {{{1 fshow_preview - git commit browser with previews

  is_in_git_repo || return
    git log --graph --format:lo --decorate --oneline "$@" |
        fzf --no-sort --reverse --tiebreak=index --no-multi \
            --ansi --preview="$_viewGitLogLine" \
                --header "enter to view, alt-y to copy hash" \
                --bind "enter:execute:nvim {}" \
                # --bind "alt-y:execute:$_gitLogLineToHash | xclip"
} # }}}

fgs() { # {{{ pick files from git status -s
    # doesn't work
  # "Nothing to see here, move along"
  is_in_git_repo || return

  local cmd="${FZF_CTRL_T_COMMAND:-command git status -s}"

  eval "$cmd" | FZF_DEFAULT_OPTS="--height ${FZF_TMUX_HEIGHT:-40%} --reverse " fzf -m "$@" | while read -r item; do
    printf '%q ' "$item" | cut -d " " -f 2
  done
  echo
} # }}}

ftags() { # {{{ search ctags
  is_in_git_repo || return
  local line

  # Let's first check that theres a tag file in the dir lol
  test -e ./tags || ctags -R .

  [[ -e tags ]] &&
  line=$(awk BEGIN "{ FS=\t }" !/^!/ "{print toupper($4)\t$1\t$2\t$3} tags" | \
    cut -c1-80 | fzf --nth=1,2) && ${EDITOR:-nvim} "$(cut -f3 <<< $line)" -c "set nocst" \
                                      -c "silent tag $(cut -f2 <<< $line)"
} # }}}

fzf-down() { # {{{ fzf --height and border
# From Choi's Gist not the wiki.
  fzf --height 50% "$@" --border
} # }}}

fgt() {  # {{{ preview tags
  is_in_git_repo || return
  git tag --sort -version:refname |
  fzf-down '--multi --preview-window right:70% '\
    --preview "git show --color=always {} | head - $LINES"
} # }}}

fgl() { # {{{  Souped up git log with sort and preview
  is_in_git_repo || return
  git log --date=short --format="%C(green)%C(bold)%cd %C(auto)%h%d %s (%an)" --graph --color=always |
  fzf-down --ansi --no-sort --reverse --multi --bind 'ctrl-s:toggle-sort' \
    --header 'Press CTRL-S to toggle sort' \
    --preview 'grep -o "[a-f0-9]\{7,\}" <<< {} | xargs git show --color=always | head -'$LINES |
  grep -o "[a-f0-9]\{7,\}"
} # }}}

fgr() {  # {{{1 git remote
  is_in_git_repo || return
  git remote -v | awk '{print $1 "\t" $2}' | uniq |
  fzf-down --tac \
    --preview 'git log --oneline --graph --date=short --pretty="format:%C(auto)%cd %h%d %s" {1} | head -200' |
  cut -d$'\t' -f1
} # }}}

fgstash() { # {{{1 preview window for git stashes Different gist
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
    ctrl-o) "git stash pop $reflog" ;;
    ctrl-y) "git stash apply $reflog" ;;
    ctrl-x) "git stash drop $reflog" ;;
  esac
} # }}}

#   Updated versions of the above. From Choi's bashrc.:

fgs() {  # git status through fzf: {{{1
  is_in_git_repo || return
  git -c color.status=always status --short |
  fzf-down -m --ansi --nth 2..,.. \
    --preview '(git diff --color=always -- {-1} | sed 1,4d; cat {-1}) | head -500' |
  cut -c4- | sed 's/.* -> //'
}  # }}}

fghist() {  # Hist: {{{1
  is_in_git_repo || return
  git log --date=short --format="%C(green)%C(bold)%cd %C(auto)%h%d %s (%an)" --graph --color=always |
  fzf-down --ansi --no-sort --reverse --multi --bind 'ctrl-s:toggle-sort' \
    --header 'Press CTRL-S to toggle sort' \
    --preview 'grep -o "[a-f0-9]\{7,\}" <<< {} | xargs git show --color=always | head $LINES' |
  grep -o "[a-f0-9]\{7,\}"
}  # }}}

fgr() {  # {{{1
  is_in_git_repo || return
  git remote -v | awk '{print $1 "\t" $2}' | uniq |
  fzf-down --tac \
    --preview 'git log --oneline --graph --date=short --pretty="format:%C(auto)%cd %h%d %s" {1} | head -200' |
  cut -d$'\t' -f1
}  # }}}

fgs() {  # {{{1
  is_in_git_repo || return
  git stash list | fzf-down --reverse -d: --preview 'git show --color=always {1}' |
  cut -d: -f1
}  # }}}

fggrep() {  # {{{1
  is_in_git_repo || return
    git grep -C 0 --heading --break --word-regex --no-line-number |
    fzf-down --tac --reverse --ansi
}  # }}}

fgstash() {  # {{{ git stash list
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
} # }}}

# Functions For the Bindings: {{{

fgf() {  # {{{
    is_in_git_repo || return
    git -c color.status=always status --short |
    fzf-down -m --ansi --nth 2..,.. \
    --preview '(git diff --color=always -- {-1} | sed 1,4d; cat {-1}) | head -500' |
    cut -c4- | sed 's/.* -> //'
}  # }}}

fgt() {  # tags: {{{
  is_in_git_repo || return
  git tag --sort -version:refname |
  fzf-down --multi --preview-window right:70% \
    --preview 'git show --color=always {} | head -200'
}  # }}}

fgb() {
  is_in_git_repo || return
  git branch -a --color=always | grep -v '/HEAD\s' | sort |
  fzf-down --ansi --multi --tac --preview-window right:70% \
    --preview 'git log --oneline --graph --date=short --color=always --pretty="format:%C(auto)%cd %h%d %s" $(sed s/^..// <<< {} | cut -d" " -f1) | head -'$LINES |
  sed 's/^..//' | cut -d' ' -f1 |
  sed 's#^remotes/##'
}

fgh() {
  is_in_git_repo || return
  git log --date=short --format="%C(green)%C(bold)%cd %C(auto)%h%d %s (%an)" --graph --color=always |
  fzf-down --ansi --no-sort --reverse --multi --bind 'ctrl-s:toggle-sort' \
    --header 'Press CTRL-S to toggle sort' \
    --preview 'grep -o "[a-f0-9]\{7,\}" <<< {} | xargs git show --color=always | head -'$LINES |
  grep -o "[a-f0-9]\{7,\}"
}

fgr() {
  is_in_git_repo || return
  git remote -v | awk '{print $1 "\t" $2}' | uniq |
  fzf-down --tac \
    --preview 'git log --oneline --graph --date=short --pretty="format:%C(auto)%cd %h%d %s" {1} | head -200' |
  cut -d$'\t' -f1
}

# The bindings: {{{
bind '"\er": redraw-current-line'
bind '"\C-g\C-f": "$(fgf)\e\C-e\er"'
bind '"\C-g\C-b": "$(fgb)\e\C-e\er"'
bind '"\C-g\C-t": "$(fgt)\e\C-e\er"'
bind '"\C-g\C-h": "$(fgh)\e\C-e\er"'
bind '"\C-g\C-r": "$(fgr)\e\C-e\er"'

# }}}
