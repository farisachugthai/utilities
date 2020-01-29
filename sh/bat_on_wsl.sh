#!/bin/bash
# Maintainer: Faris Chugthai

# set -euo pipefail


function bat() {
    # Gonna pat myself on the back because this works exactly how I want it to!
    local file
    if [[ -n "$1" ]]; then
        file="$1"
    else
        echo -e "I'm assuming you didn't wanna do that. Give me a filename."
    fi

    if [[ -n "$(command -v bat)" ]]; then
        bat.exe --italic-text always --wrap character --paging always --pager "$PAGER" -- "$file"
    else
        echo "Yo I can't find the bat executable"
    fi
}


