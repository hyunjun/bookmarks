#!/bin/sh
FILENAMES="$@"
PYTHON3=`which python3`

if [ 0 = '${#FILENAMES}' ]; then
  exit 1
fi

for FILENAME in $FILENAMES
do
  echo $f
  cat $FILENAME | sed -e 's/	/  /g' > $FILENAME.tmp
  mv $FILENAME.tmp $FILENAME
done
#git diff $FILENAMES | grep '^[+-][ ]\{0,\}[#\*]\{1,\}[ ]\{0,\}[^+]' | sed -e 's/\](/ /' | sed -e 's/)$//' | sed -e 's/\/$//' | pbcopy
git diff $FILENAMES | grep '^[+-][ ]\{0,\}[#\*]\{1,\}[ ]\{0,\}[^+]' | $PYTHON3 replace_commit_message.py | pbcopy
git add $FILENAMES
git commit
