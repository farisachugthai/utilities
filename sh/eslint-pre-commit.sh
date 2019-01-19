#!/usr/bin/env bash
# Maintainer: Faris Chugthai

# set -euo pipefail

for file in $(git diff --cached --name-only | grep -E '\.(js|jsx)$'); do
    git show ":$file" | node_modules/.bin/eslint --stdin --stdin-filename "$file"
    # we only want to lint the staged changes, not any un-staged changes

    if [ $? -ne 0 ]; then

        echo -e "ESLint failed on staged file '$file'.\nPlease check your code and try again.\nYou can run ESLint manually via npm run eslint.\n"
        exit 1 # exit with failure status
    fi
done
