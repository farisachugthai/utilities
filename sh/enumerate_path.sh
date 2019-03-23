#!/bin/bash

# Shell script that displays everything in path
echo -e "'Displaying everything on the $PATH.'\n"

echo -n "$PATH" | xargs -d: -I{} -r -- find -L {} -maxdepth 1 -mindepth 1 -type f -executable -printf '%P\n' 2>/dev/null | sort -u

# Need to run a `cmp` to:
echo -e "\n\n\n Now utilizing compgen.\n"

compgen -c | sort -u

# Great fodder for fzf

exit 0
