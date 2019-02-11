#!/bin/sh
filename=$1

if [ 0 = '${#filename}' ]; then
  exit 1
fi

git diff $filename | grep '^[+-][ ]\{0,\}\*[^+]' | sed -e 's/\](/ /' | sed -e 's/)$//' | sed -e 's/\/$//' | pbcopy
git add $filename
git commit
