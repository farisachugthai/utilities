#!/usr/bin/env bash
# Maintainer: Faris Chugthai

# set -euo pipefail
# TODO: Honestly drop this script i keep forgetting rclone with cloud storage id so much easier
# https://rclone.org/crypt/

# This is me basically taking notes as I haven't run this yet

# Hoping this is the correct syntax for logical not
if ! [[ -d "$HOME/logs" ]]; then
    mkdir "$HOME/logs";
    echo "Creating directory for rsync logs.";
fi

rsync -avz --recursive --update --preallocate --one-file-system --files-from="rsync.txt" \
    --human-readable --itemize-changes --log-file="$HOME/logs/rsync$(date)" --links

# Then feel free to toggle --dry-run here or there

# As far as links go you have 2 options
# -l --links means symlinks are symlinks
# -L or --copy-links means transform symlinks into the file they refer to

# Preallocate to ensure that theres space on the EHD

# -s, --protect-args -> no space-splitting; only wildcard special chars. that's interesting

# Pretty straight forward. Now just to make that list of files.

exit 0
