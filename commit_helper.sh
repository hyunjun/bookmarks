#!/bin/sh
AMEND=""
FILENAMES=()
for arg in "$@"; do
  if [ "$arg" = "--amend" ]; then
    AMEND="--amend"
  else
    FILENAMES+=("$arg")
  fi
done
PYTHON3=$(which python3)

if [ ${#FILENAMES[@]} -eq 0 ]; then
  exit 1
fi

for FILENAME in "${FILENAMES[@]}"
do
  echo "$FILENAME"
  sed -i '' 's/	/  /g' "$FILENAME"
done

if [ -n "$AMEND" ]; then
  # amend: diff between HEAD~1 and current working tree
  git diff HEAD~1 -- "${FILENAMES[@]}" | grep '^[+-][ ]\{0,\}[#\*]\{1,\}[ ]\{0,\}[^+]' | $PYTHON3 replace_commit_message.py | pbcopy
else
  git diff -- "${FILENAMES[@]}" | grep '^[+-][ ]\{0,\}[#\*]\{1,\}[ ]\{0,\}[^+]' | $PYTHON3 replace_commit_message.py | pbcopy
fi

git add "${FILENAMES[@]}"
git commit $AMEND
