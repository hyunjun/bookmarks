#!/bin/sh
filename=$1

if [ 0 = '${#filename}' ]; then
  exit 1
fi

cat $filename | sed -e 's/	/  /g' > $filename.tmp
mv $filename.tmp $filename
git diff $filename | grep '^[+-][ ]\{0,\}\*[^+]' | sed -e 's/\](/ /' | sed -e 's/)$//' | sed -e 's/\/$//' | pbcopy
git add $filename
git commit
