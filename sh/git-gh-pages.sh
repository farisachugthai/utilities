#!/bin/bash

# From: https://raw.githubusercontent.com/tj/git-extras/master/bin/git-gh-pages
echo 'setting up gh-pages'
echo '-------------------'
 
echo 'Tell me your github account username: '
read username
 
echo 'Now, tell me your repository name: '
read repository
 
git stash \
&& git checkout -b 'gh-pages' \
&& echo 'My Page' > index.html \
&& git add . \
&& git commit -a -m 'Initial commit' \
&& git remote add origin https://github.com/"$username"/"$repository".git \
&& git push -u origin gh-pages \
&& echo 'Complete' \
&& echo '-------------------' \
&& echo 'You can find your last changes in the stash!'
