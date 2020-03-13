#!/bin/bash
# Maintainer: Faris Chugthai

fzf-down() { # {{{ fzf
    # Integration with ripgrep
    RG_PREFIX="rg --column --line-number --no-heading --color=always
    --smart-case "
    INITIAL_QUERY="."
    FZF_DEFAULT_COMMAND="$RG_PREFIX $INITIAL_QUERY" |
    fzf-tmux --prompt'FZF' --ansi --cycle --sort \
        --bind 'ctrl-r:reload(ps -ef)' --header 'Press CTRL-R to reload' \
        --header-lines=1 --layout=reverse --bind "change:reload:$RG_PREFIX {q} || true" \
        --ansi --phony --query "$INITIAL_QUERY"

}
# }}}

complete -F _fzf_opts_completion -o bashdefault -o default fzf-down

is_in_git_repo() { # {{{
  git rev-parse HEAD > /dev/null 2>&1  || echo -e "Not in a git repo!\n"
}
# }}}

# __git_complete_refs [<option>]...  {{{
# Completes refs, short and long, local and remote, symbolic and pseudo.
# --remote=<remote>: The remote to list refs from, can be the name of a
#                    configured remote, a path, or a URL.
# --track: List unique remote branches for 'git checkout's tracking DWIMery.
# --pfx=<prefix>: A prefix to be added to each ref.
# --cur=<word>: The current ref to be completed.  Defaults to the current
#               word to be completed.
# --sfx=<suffix>: A suffix to be appended to each ref instead of the default
#                 space.
__git_complete_refs ()
{
	local remote track pfx cur_="$cur" sfx=" "

	while test $# != 0; do
		case "$1" in
		--remote=*)	remote="${1##--remote=}" ;;
		--track)	track="yes" ;;
		--pfx=*)	pfx="${1##--pfx=}" ;;
		--cur=*)	cur_="${1##--cur=}" ;;
		--sfx=*)	sfx="${1##--sfx=}" ;;
		*)		return 1 ;;
		esac
		shift
	done

	__gitcomp_direct "$(__git_refs "$remote" "$track" "$pfx" "$cur_" "$sfx")"
}  # }}}

fz() {  # Not git relates but depends on fasd: {{{
  f | awk -F' ' '{print $2}' | fzf-down
}  # }}}

complete -o bashdefault -F _fzf_opts_completion -o default  -o filenames fz

dz() {  # Not git relates but depends on fasd: {{{
  d | awk -F' ' '{print $2}' | fzf-down
}  # }}}

complete -o bashdefault -F _fzf_opts_completion -o default  -o filenames dz

fgco() { # {{{1 checkout git commit
  is_in_git_repo || return
  local commits commit
  commits="$(git log --pretty=oneline --abbrev-commit --reverse)" &&
  commit=$(echo "$commits" | fzf --tac +s +m -e) &&
  git checkout "$(echo $commit | sed s/ .*//)"

} # }}}

fshow_preview() { # {{{1 fshow_preview - git commit browser with previews

  is_in_git_repo || return
    git log --graph --decorate --oneline "$@" |
        fzf --reverse --tiebreak=index --no-multi \
            --preview="git show --color=always {}" --preview-window right:80% \
            --header "enter to view with nvim, alt-y to copy hash" \
            --bind "enter:execute:nvim {}" 
} # }}}

complete -F _git_log -F _fzf_opts_completion -o bashdefault -o default fshow_preview

fgzt() {  # {{{ preview tags
  is_in_git_repo || return
  git tag --sort -version:refname "$@" |
  fzf-down '--multi --preview-window right:70% '\
            --bind 'ctrl-s:toggle-sort' \
            --header 'Press CTRL-S to toggle sort' \
            --preview "git show --color=always {} | head - $LINES"

} # }}}

complete -F _git_tag -o bashdefault -o default fgt

fgl() { # {{{  Souped up git log with sort and preview

  is_in_git_repo || return
  git log --date=short --format="%C(green)%C(bold)%cd %C(auto)%h%d %s (%an)" --graph --color=always |
  fzf-down --ansi --no-sort --reverse --multi --bind 'ctrl-s:toggle-sort' \
    --header 'Press CTRL-S to toggle sort' \
    --preview 'grep -o "[a-f0-9]\{7,\}" <<< {} | xargs git show --color=always | head -'$LINES |
  grep -o "[a-f0-9]\{7,\}"
} # }}}

complete -F __git_complete_refs -o bashdefault -o default fgl

fgr() {  # {{{1 git remote
  is_in_git_repo || return
  git remote -v | awk '{print $1 "\t" $2}' | uniq |
  fzf-down --tac \
    --preview 'git log --oneline --graph --date=short --pretty="format:%C(auto)%cd %h%d %s" {1} | head -200' |
  cut -d$'\t' -f1
} # }}}

#   Updated versions of the above. From Choi's bashrc.:
fghist() {  # Hist: {{{1
  is_in_git_repo || return
  git log --date=short --format="%C(green)%C(bold)%cd %C(auto)%h%d %s (%an)" --graph --color=always |
  fzf-down --ansi --no-sort --reverse --multi --bind 'ctrl-s:toggle-sort' \
    --header 'Press CTRL-S to toggle sort' \
    --preview 'grep -o "[a-f0-9]\{7,\}" <<< {} | xargs git show --color=always | head $LINES' |
  grep -o "[a-f0-9]\{7,\}"
}  # }}}

fgs() {  # {{{1
  is_in_git_repo || return
  git stash list | fzf-down --reverse -d: --preview 'git show --color=always {1}'
}  # }}}

fggrep() {  # {{{1
  is_in_git_repo || return
    git grep -C 0 --heading --break --word-regex --no-line-number |
    fzf-down --tac --reverse --ansi
}  # }}}

fgf() {  # {{{
    is_in_git_repo || return
    git -c color.status=always status --short |
    fzf-down -m --ansi --nth 2..,.. \
    --preview '(git diff --color=always -- {-1} | sed 1,4d; cat {-1}) | head -500' |
    cut -c4- | sed 's/.* -> //'
}  # }}}

complete -o bashdefault -F _fzf_opts_completion -o default  -o filenames fgf

fgt() {  # tags: {{{
  is_in_git_repo || return
  git tag --sort -version:refname |
  fzf-down --multi --preview-window right:70% \
    --preview 'git show --color=always {} | head -200'
}  # }}}

complete -o bashdefault -F _fzf_opts_completion -o default  -o filenames fgt

fgb() {  # branches: {{{
  is_in_git_repo || return
  git branch -a --color=always | grep -v '/HEAD\s' | sort |
  fzf-down --ansi --multi --tac --preview-window right:70% \
    --preview 'git log --oneline --graph --date=short --color=always --pretty="format:%C(auto)%cd %h%d %s" $(sed s/^..// <<< {} | cut -d" " -f1) | head -'$LINES |
  sed 's/^..//' | cut -d' ' -f1 |
  sed 's#^remotes/##'
}  # }}}

fgh() {  # {{{ git hist
  is_in_git_repo || return
  git log --date=short --format="%C(green)%C(bold)%cd %C(auto)%h%d %s (%an)" --graph --color=always |
  fzf-down --ansi --no-sort --reverse --multi --bind 'ctrl-s:toggle-sort' \
    --header 'Press CTRL-S to toggle sort' \
    --preview 'grep -o "[a-f0-9]\{7,\}" <<< {} | xargs git show --color=always | head -'$LINES |
  grep -o "[a-f0-9]\{7,\}"
}  # }}}

fgr() {  # {{{
  is_in_git_repo || return
  git remote -v | awk '{print $1 "\t" $2}' | uniq |
  fzf-down --tac \
    --preview 'git log --oneline --graph --date=short --pretty="format:%C(auto)%cd %h%d %s" {1} | head -200' |
  cut -d$'\t' -f1
}  # }}}

# The bindings: {{{
bind -m emacs-standard '"\er": redraw-current-line'
bind -m emacs-standard '"\C-g\C-f": "$(fgf)\e\C-e\er"'
bind -m emacs-standard '"\C-g\C-b": "$(fgb)\e\C-e\er"'
bind -m emacs-standard '"\C-g\C-t": "$(fgt)\e\C-e\er"'
bind -m emacs-standard '"\C-g\C-h": "$(fgh)\e\C-e\er"'
bind -m emacs-standard '"\C-g\C-r": "$(fgr)\e\C-e\er"'

# }}}

# Vim: set et ts=4 sw=4 et sts=4:
