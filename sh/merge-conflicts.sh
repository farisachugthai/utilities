#!/usr/bin/env bash
# Maintainer: Faris Chugthai
# Script to show how many merge conflicts occurred in which files.
# For the situations where it's really that bad.

# set -euo pipefail

# TODO: Just ran this and it stated 1 file matched. It was this file.
# If you add a bracket in the first letter of `ps aux | grep [s]shd `
# it removes grep from output. How do we doo the same here?


echo -e "Here are all the merge conflicts starting in this directory.\n"

ag --recurse --nofollow --hidden -l "<<<<<<< HEAD" .

# actually unnecessary with the stats
# total_files="$(ag --recurse --nofollow --hidden -l "<<<<<<< HEAD" . | wc -l)"
# echo -e "For a total of: $total_files total conflicted files"

stats="$(ag --recurse --nofollow --hidden -l --stats-only "<<<<<<< HEAD" .)"

echo -e "Here are the total stats:\n"

echo -e "$stats"

exit 0
