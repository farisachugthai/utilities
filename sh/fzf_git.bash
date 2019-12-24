#!/bin/bash
# Maintainer: Faris Chugthai

# fzf_commits: commits in a repo: {{{1
# }}}
fcoc() { # {{{1 checkout git commit
  local commits commit
  commits="$(git log --pretty=oneline --abbrev-commit --reverse)" &&
  commit=$(echo "$commits" | fzf --tac +s +m -e) &&
  git checkout "$(echo $commit | sed s/ .*//)"
}
# }}}
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

  local cmd="${FZF_CTRL_T_COMMAND:-command git status -s}"

  eval "$cmd" | FZF_DEFAULT_OPTS="--height ${FZF_TMUX_HEIGHT:-40%} --reverse $FZF_DEFAULT_OPTS $FZF_CTRL_T_OPTS" fzf -m "$@" | while read -r item; do
    printf '%q ' "$item" | cut -d " " -f 2
  done
  echo
}
# }}}
ftags() { # {{{ search ctags
  local line

  # Let's first check that theres a tag file in the dir lol
  test -e ./tags || ctags -R .

  [[ -e tags ]] &&
  line=$(awk BEGIN "{ FS=\t }" !/^!/ "{print toupper($4)\t$1\t$2\t$3} tags" | \
    cut -c1-80 | fzf --nth=1,2) && ${EDITOR:-nvim} "$(cut -f3 <<< $line)" -c "set nocst" \
                                      -c "silent tag $(cut -f2 <<< $line)"
}
# }}}
# From Choi's Gist not the wiki.
fzf-down() { # {{{ fzf --height and border
  fzf --height 50% "$@" --border
}
# }}}
# fgb() { # {{{
#   is_in_git_repo || return
#   git branch -a --color=always | grep -v '/HEAD\s' | sort |
#   fzf-down --ansi --multi --tac --preview-window right:70% \
#   --preview "git log --oneline --graph --date=short --pretty=format:%C(auto)%cd %h%d %s" $(sed s/^..// <<< {} | cut -d" " -f1) | head -'$LINES |
#   sed 's/^..//' | cut -d' ' -f1 |
#   sed 's#^remotes/##'
# }
# }}}
fgt() { # {{{
  is_in_git_repo || return
  git tag --sort -version:refname |
  fzf-down '--multi --preview-window right:70% '\
    --preview "git show --color=always {} | head - $LINES"
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
    ctrl-o) "git stash pop $reflog" ;;
    ctrl-y) "git stash apply $reflog" ;;
    ctrl-x) "git stash drop $reflog" ;;
  esac
}

# Updated versions of the above. From Choi's bashrc.

fgs() {  # git status through fzf: {{{1
  is_in_git_repo || return
  git -c color.status=always status --short |
  fzf-down -m --ansi --nth 2..,.. \
    --preview '(git diff --color=always -- {-1} | sed 1,4d; cat {-1}) | head -500' |
  cut -c4- | sed 's/.* -> //'
}

fgb() {  # git branch: {{{1
  is_in_git_repo || return
  git branch -a --color=always | grep -v '/HEAD\s' | sort |
  fzf-down "--ansi --multi --tac --preview-window right:70%" \
    --preview "git log --oneline --graph --date=short --pretty='format:%C(auto)%cd %h%d %s'" $("sed s/^..// <<< {} | cut -d' ' -f1") | head -200 |
  sed 's/^..//' | cut -d' ' -f1 |
  sed 's#^remotes/##'
}

fgt() {  # tags: lp
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
fshow() { # {{{1 git commit browser
    git log --graph --color=always \
        "--format=%C(auto)%h%d %s %C(black)%C(bold)%cr" "$@" |
    fzf "--ansi --no-sort --reverse --tiebreak=index --bind=ctrl-s:toggle-sort \
        --no-multi --header='Ctrl-s to toggle sort. C-m to execute.' \
        --bind "ctrl-m:execute:
                (grep -o '[a-f0-9]\{7\}' | head -1 |
                xargs -I % bash -c "git show --color=always %" | bat -R) << 'FZF-EOF'
                {}
FZF-EOF
}
# }}}
