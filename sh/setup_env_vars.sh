#!/bin/bash
# Maintainer: Faris Chugthai

# set -euo pipefail

SOURCE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )"/.. >/dev/null && pwd )"
DOTFILE_DIR="$HOME/projects/dotfiles/unix"

DOT_REPO="$(git ls-files $DOTFILE_DIR)"

for DOT_FILE in $DOT_REPO[@]; do
        ln -svf "$SOURCE_DIR/$DOT_FILE" "$HOME/$DOT_FILE"
done

# Get the init.vim sourced do the rest later. Or change dot_repo

# If we've installed PowerShell, set up it's enviroment:
if [[ -n "$(which pwsh)" ]]; then
    # TODO: Should check that there isn't already a file there
    # Get the powershell profile path:
    PWSH_PROFILE="$(pwsh -c 'Write-Host $PROFILE')"
    echo "Profile set to: $PWSH_PROFILE"
    mkdir -p "$PWSH_PROFILE"
    ln -svf "$SOURCE_DIR/profile.ps1" "$PWSH_PROFILE/profile.ps1"
fi

exit 0
