#!/bin/bash
# Local:  rsync [OPTION...] SRC... [DEST]

set -euo pipefail

configured_rsync() {

    local log
    if [[ -d /var/log ]]; then
        log="/var/log/$(date)"
    # TODO:
    # elseif
    else
        log=""
    fi

    "rsync \
        --8-bit-output \
        -avz \
        --itemize-changes \
        --recursive \
        --$log \
        --preallocate \
        --protect-args
        # -l --links means symlinks are symlinks
        --links"

        # If you need to transfer a filename that contains whitespace, you can
        # either specify the --protect-args (-s) option, or you'll need to escape
        # the whitespace in a way that the remote shell will understand.  For
        # instance:
        # TODO:1
        # -L or --copy-links means transform symlinks into the file they refer to

}
# Then feel free to toggle --dry-run here or there

# Pretty straight forward. Now just to make that list of files.
# TODO: Make that list of files. Run the script and inspect files for content, whether mtime and ctime
# stayed constant, and then come up with a procedure for restoration.

configured_rsync argv[:]

exit 0

