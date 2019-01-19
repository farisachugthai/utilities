#!/usr/bin/env bash
# set -euo pipefail
# TODO: Honestly drop this script i keep forgetting rclone with cloud storage id so much easier
# https://rclone.org/crypt/

rsync -avz --recursive --update --preallocate --one-file-system --files-from="rsync.txt" \
    --human-readable --itemize-changes --log-file="$HOME/logs/rsync$(date)" --links

# Then feel free to toggle --dry-run here or there

# TODO:
## Options I still need to explore:

# As far as links go you have 2 options
# -l --links means symlinks are symlinks
# -L or --copy-links means transform symlinks into the file they refer to

# Preallocate to ensure that theres space on the EHD

# -s, --protect-args -> no space-splitting; only wildcard special chars. that's interesting

# Pretty straight forward. Now just to make that list of files.
# TODO: Make that list of files. Run the script and inspect files for content, whether mtime and ctime
# stayed constant, and then come up with a procedure for restoration.

exit 0
