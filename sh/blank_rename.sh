#! /bin/bash
# Advanced Bash Scripting Guide
# page 578-579
# blank-rename.sh
#
# Substitutes underscores for blanks in all the filenames in a directory.
# TODO: Faris Chugthai: I mean I'm sure it does what it says it does but I 
# wanna reverse it [replace blanks for underscores] and also understand
# it better and what's going on. So study this.

ONE=1 # For getting singular/plural right (see below).
number=0 # Keeps track of how many files actually renamed.
FOUND=0 # Successful return value.

for filename in * #Traverse all files in directory.
do
    echo "$filename" | grep -q " " # Check whether filename
    if [ $? -eq $FOUND ]           #+ contains space(s).
then
fname=$filename # Yes, this filename needs work.
n=`echo $fname | sed -e "s/ /_/g"` # Substitute underscore for blank.
mv "$fname" "$n" # Do the actual renaming.
let "number += 1"
fi
done
if [ "$number" -eq "$ONE" ]
then
echo "$number file renamed."
else
echo "$number files renamed."
fi
exit 0
