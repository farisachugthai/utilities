#!/usr/bin/env bash
# Maintainer: Faris Chugthai

# set -euo pipefail
glNoGraph(){  # An alias I converted into a function. cross your fingers
    git log --color=always --format="%C(auto)%h%d %s %C(black)%C(bold)%cr% C(auto)%an" "$@"
}

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



fh() { # {{{1
    git log --color=always --all --branches --abbrev --oneline | fzf --ansi --multi --preview "git show {+1}" --preview-window=down
}

# }}}
git_log() { # {{{1 log piped into less and displays show
  local show="git show --color=always \"\$(grep -m1 -o \"[a-f0-9]\{7\}\" <<< {})\""
  fzf --prompt='log' -e --no-sort --tiebreak=index \
    --bind="enter:execute:$show | less -R" \
    --preview="$show" \
  < <(git log --graph --color=always \
    --format="%C(auto)%h%d %s %C(black)%C(bold)%cr" "$@")
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

fgbr() { # {{{1 checkout git branch (including remote branches), sorted by most recent commit, limit 30 last branches
  local branches branch
  branches="$(git for-each-ref --count=30 --sort=-committerdate refs/heads/ --format='%(refname:short)')" &&
  branch="$(echo $branches |
           fzf-tmux -d $(( 2 + $(wc -l <<< $branches) )) +m)" # &&
	   # Honestly the line below is fucked up somehow and is *I think* fucking the syntax of the whole file
  # git checkout $(echo $branch | sed s/.* // | sed s/remotes/[^/]*/##)
}
# }}}
fco_preview() { # {{{1 checkout git branch/tag, with a preview showing the commits between the tag/branch and HEAD
  local tags branches target
  tags=$(
git tag | awk {print "\x1b[31;1mtag\x1b[m\t" $1}) || return
  branches=$(
git branch --all | grep -v HEAD |
sed "s/.* //" | sed "s#remotes/[^/]*/##" |
sort -u | awk {print "\x1b[34;1mbranch\x1b[m\t" $1}) || return
  target=$(
(echo "$tags"; echo "$branches") |
    fzf --no-hscroll --no-multi --delimiter="\t" -n 2 \
        --ansi --preview="git log -200 --pretty=format:%s $(echo {+2..} |  sed 's/$/../' )" ) || return
  git checkout "$(echo $target | awk '{print $2}')"
}
