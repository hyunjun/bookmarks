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

# '@@' hunk 헤더도 함께 넘긴다 — subject 생성 시 hunk 단위로 북마크 그룹을 구분하기 위함.
# (replace_commit_message.py가 본문에서는 '@@' 라인을 무시하므로 본문 출력은 동일)
# 컨텍스트는 기본값(-U3)을 유지한다 — -U0은 한 북마크 그룹의 두 삽입 지점을
# 별개 hunk로 쪼개서 실측 일치율이 오히려 떨어졌다(399커밋 기준 312→309).
GREP_PATTERN='^@@\|^[+-][ ]\{0,\}[#\*]\{1,\}[ ]\{0,\}[^+]'
if [ -n "$AMEND" ]; then
  # amend: diff between HEAD~1 and current working tree
  git diff HEAD~1 -- "${FILENAMES[@]}" | grep "$GREP_PATTERN" | $PYTHON3 replace_commit_message.py | pbcopy
else
  git diff -- "${FILENAMES[@]}" | grep "$GREP_PATTERN" | $PYTHON3 replace_commit_message.py | pbcopy
fi

git add "${FILENAMES[@]}"
git commit $AMEND
