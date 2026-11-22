#!/usr/bin/env python3
"""북마크 중복 URL 검사.

  python3 check_duplicate_urls.py URL [URL ...]   저장 전: 이미 있는 주소인지 조회
  python3 check_duplicate_urls.py --diff [--base REV] [FILE ...]
                                                  저장 후: 커밋 전 변경분이 중복을 만들었는지 검사
                                                  (REV 기본값 HEAD, FILE 생략 시 모든 .md)

"동일"은 문자열이 완전히 같은 주소, "유사"는 http/https·www·끝의 '/'·추적 파라미터만 다른 주소.
동일 중복이 있으면 종료 코드 1.
"""
import glob
import re
import subprocess
import sys
from urllib.parse import parse_qsl, urlencode, urlsplit

SKIP = {"CLAUDE.md", "README.md", "SUMMARY.md"}
TRACKING = re.compile(
    r"^(utm_.*|fbclid|mibextid|trk|aem_.*|rdid|rcm|__cft__.*|__tn__|ref|refId|trackingId"
    r"|highlightedUpdateUrn|highlightedUpdateType|origin)$"
)


def urls_in(line):
    out, i = [], 0
    while True:
        j = line.find("](", i)
        if j < 0:
            return out
        k, depth = j + 2, 1
        while k < len(line) and depth > 0:
            c = line[k]
            if c == "(":
                depth += 1
            elif c == ")":
                depth -= 1
            elif c in " \t\n":
                break
            k += 1
        url = line[j + 2 : k - 1] if depth == 0 else line[j + 2 : k]
        i = k
        if url.startswith(("http://", "https://")):
            out.append(url)


def normalize(url):
    p = urlsplit(url)
    host = p.netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    query = urlencode([(k, v) for k, v in parse_qsl(p.query, keep_blank_values=True) if not TRACKING.match(k)])
    path = p.path.rstrip("/")
    if host == "github.com":  # GitHub은 소유자·저장소 이름의 대소문자를 구분하지 않는다
        path = path.lower()
    return host + path + ("?" + query if query else "")


def index():
    exact, similar = {}, {}
    for name in sorted(glob.glob("*.md")):
        if name in SKIP:
            continue
        with open(name, encoding="utf-8", errors="replace") as f:
            for n, line in enumerate(f, 1):
                for url in urls_in(line):
                    exact.setdefault(url, []).append((name, n))
                    similar.setdefault(normalize(url), []).append((name, n, url))
    return exact, similar


def added_urls(base, paths):
    diff = subprocess.run(
        ["git", "diff", "-U0", base, "--", *(paths or ["*.md"])], capture_output=True, text=True, check=True
    ).stdout
    found = []
    for line in diff.split("\n"):
        if line.startswith("+") and not line.startswith("+++"):
            for url in urls_in(line[1:]):
                if url not in found:
                    found.append(url)
    return found


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    exact, similar = index()
    after_save = argv[0] == "--diff"
    if after_save:
        rest, base = argv[1:], "HEAD"
        if rest[:1] == ["--base"]:
            base, rest = rest[1], rest[2:]
        targets = added_urls(base, rest)
    else:
        targets = argv
    limit = 1 if after_save else 0  # 저장 후에는 방금 넣은 한 건은 정상
    dup = False
    for url in targets:
        same = exact.get(url, [])
        near = [(f, n, u) for f, n, u in similar.get(normalize(url), []) if u != url]
        if len(same) > limit:
            dup = True
            print(f"동일  {url}")
            for f, n in same:
                print(f"        {f}:{n}")
        if near:
            print(f"유사  {url}")
            for f, n, u in near:
                print(f"        {f}:{n}  {u}")
    if after_save:
        print(f"추가된 주소 {len(targets)}개 검사, 동일 중복 {'있음' if dup else '없음'}")
    elif not dup:
        print("동일 주소 없음")
    return 1 if dup else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
