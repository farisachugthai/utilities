#!/usr/bin/env bash
# Maintainer: Faris Chugthai

# set -euo pipefail

# if basename "$(pwd)" != docs; exit; fi
# idk if that works yet.

make html

git checkout gh-pages;

mv -f _build/html/* ..

git add -A ..

if $1; then
    git commit -a -m '$1'
else
    git commit -a -m 'Update docs'
fi

git push
git checkout master

exit 0
