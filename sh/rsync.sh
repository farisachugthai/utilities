#!/bin/bash
# Vim: set ff=unix:
# Because shellcheck freaks out otherwise

# TODO: First check that we have a Unix OS. Win 10 now has native bash for windows.
# If unix, then put it in var/logs or something don't drop it in the home dir.
# if ! [[ -d "$HOME/logs" ]]; then
#     mkdir "$HOME/logs";
#     echo "Creating directory for rsync logs.";
# fi

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
