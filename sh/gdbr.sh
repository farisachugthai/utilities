#!/usr/bin/env bash
# Maintainer: Faris Chugthai

# set -euo pipefail
gdbr() {
    if [[ "$#" -ne 2 ]]; then
        echo -e 'Usage: gitdiffb branch1 branch2'
        break
    fi

    git log --graph \
    --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr)%Creset' \
    --abbrev-commit --date=relative $1..$2;
}
