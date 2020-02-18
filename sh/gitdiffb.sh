#!/bin/bash
# Maintainer: Faris Chugthai

# set -euo pipefail

gitdiffb() {
    if [[ "$@" -ne 2 ]]; then
        echo -e 'Usage: gitdiffb branch1 branch2'
        exit 127
        # if you care you can do man bash and search for exit codes to get the
        # correct code to use here
    fi

    git log --graph \
    --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr)%Creset' \
    --abbrev-commit --date=relative $1..$2;

}

if [[ -n "$(command -v fzf)" ]]; then
    gitdiffb "$@"
else
    gitdiffb "$@" | fzf -
fi

exit 0
