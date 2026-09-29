from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

import re
import sys


PATTERN_URL_INSIDE_BRACKET = re.compile(r'http(.)+(?P<ending_bracket>(/){0,1}\])')

# 제거할 트래킹 파라미터
DISALLOWED_PARAMS = [
    "ab_channel", "ref", "refId", "trackingId",
    "utm_source", "utm_medium", "utm_campaign", "utm_content", "utm_term", "utm_id",
    "fbclid", "mibextid",
    "trk", "rcm",
    "rdid",
    "content_source", "fb_content_id", "channel_type",
    "triedRedirect",
]
# aem_*, __cft__, __tn__ 등 패턴 기반 파라미터는 별도 처리
DISALLOWED_PARAM_PREFIXES = ["aem_", "__cft__", "__tn__"]


def clean_url(url, disallowed_params=None):
    """URL에서 트래킹 파라미터를 제거하고 정리."""
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)

    if disallowed_params is not None:
        filtered_params = {
            k: v for k, v in query_params.items()
            if k not in disallowed_params
            and not any(k.startswith(prefix) for prefix in DISALLOWED_PARAM_PREFIXES)
        }
    else:
        filtered_params = query_params

    cleaned_query = urlencode(filtered_params, doseq=True)
    cleaned_url = urlunparse(parsed_url._replace(query=cleaned_query))
    return cleaned_url


def convert_markdown_to_clean_text(markdown, disallowed_params=None):
    """Markdown 링크를 '제목 URL' 형식의 커밋 메시지로 변환."""
    m = PATTERN_URL_INSIDE_BRACKET.search(markdown)
    if m:
        markdown = re.sub(r'/? \]\(', '](', markdown)

    # Markdown URL 패턴 정규식
    pattern = re.compile(r"\[([^\]]+)\]\((http[s]?://[^\)]+)\)")

    def replacer(match):
        text = match.group(1)
        url = match.group(2)
        cleaned_url = clean_url(url, disallowed_params)
        cleaned_url = cleaned_url[:-1] if cleaned_url.endswith('/') else cleaned_url
        return f"{text} {cleaned_url}"

    markdown = markdown.replace('(NOT YET)', '')
    # **bold text** 정리
    markdown = re.sub(r"\*\*([^*]+)\*\*", r"\1", markdown)
    # Markdown 문장에서 앞의 *, - 제거
    cleaned_markdown = re.sub(r"^\s*[\+\*\-\s]+", "", markdown)

    return pattern.sub(replacer, cleaned_markdown).strip()


# ---------------------------------------------------------------------------
# subject(커밋 제목) 생성
# ---------------------------------------------------------------------------

# '제목 | 작성자 | 플랫폼' 형태에서 마지막 구간이 이 목록과 정확히 일치하면
# 뒤쪽 구간 전체(작성자 + 플랫폼)를 작성자 표기로 보고 첫 ' | '에서 자른다.
PLATFORM_NAMES = [
    "linkedin", "facebook", "facebook reel", "instagram", "threads",
    "x", "twitter", "geeknews", "pgr21", "youtube", "medium", "substack",
    "github", "reddit", "brunch",
]
# 매체 표기가 구간 안에 섞여 있는지 판별할 때 쓰는 키워드 (예: 'InfoQ - YouTube')
PLATFORM_KEYWORDS = [
    "youtube", "linkedin", "facebook", "geeknews", "github",
    "google slides", "blog", "블로그", "브런치",
]
# 제목 뒤에 붙는 매체 꼬리표 (근거가 확인된 것만)
SITE_SUFFIXES = [" - YouTube", " - Google Slides", " · GitHub"]

# 제목 끝에 붙는 장식용 이모지 (앞쪽 이모지는 제목의 일부이므로 건드리지 않음)
PATTERN_TRAILING_EMOJI = re.compile(
    "(\\s+[\\U0001F000-\\U0001FAFF\\u2600-\\u27BF\\uFE0F\\u200D]+)+$"
)
# 제목 끝에 붙는 해시태그 묶음. 2개 이상만 제거한다
# (시리즈 표기 '#1', 'P.2' 처럼 하나만 붙은 것은 제목의 일부)
PATTERN_TRAILING_HASHTAG = re.compile(r"(\s+#[^\s#]+){2,}$")
# ' 제목 https://...' 에서 URL 시작 지점
PATTERN_URL_START = re.compile(r"\s+https?://")
# markdown 헤더 라인 (# Section)
PATTERN_HEADER_LINE = re.compile(r"^#{1,6}\s")


def strip_url_part(entry):
    """'제목 URL' 형태에서 URL과 그 뒤 잡문을 제거."""
    m = PATTERN_URL_START.search(entry)
    if m:
        return entry[:m.start()].strip()
    return entry.strip()


def has_url(entry):
    """항목에 URL이 포함되어 있는지."""
    return "http://" in entry or "https://" in entry


def is_header_line(entry):
    """'# 섹션명' 형태의 헤더 라인인지."""
    return bool(PATTERN_HEADER_LINE.match(entry.strip()))


def _is_platform_segment(segment):
    """구간 전체가 플랫폼 이름 하나인지 (예: 'LinkedIn', 'Facebook Reel')."""
    return segment.strip().lower() in PLATFORM_NAMES


def _has_platform_keyword(segment):
    """구간에 매체/플랫폼 키워드가 섞여 있는지 (예: 'InfoQ - YouTube')."""
    lowered = segment.lower()
    return any(keyword in lowered for keyword in PLATFORM_KEYWORDS)


def _looks_like_tagline(head, tail):
    """' | ' 뒤가 작성자·매체가 아니라 제품 설명(태그라인)처럼 보이는지.

    예) 'MyScale | Run Vector Search with SQL', 'text-to-cad | A library of ...'
    앞이 한 단어(제품명)이고 뒤가 두 단어 이상이며 매체 키워드가 없을 때만 유지한다.
    """
    if _has_platform_keyword(tail):
        return False
    return len(head.split()) == 1 and len(tail.split()) >= 2


def _cut_attribution_pipe(text):
    """' | 작성자', ' | 작성자 | 플랫폼' 형태의 꼬리를 제거."""
    segments = text.split(" | ")
    if len(segments) == 1:
        return text
    if _is_platform_segment(segments[-1]):
        # '제목 | 작성자 | LinkedIn' → 첫 ' | '에서 자른다
        return segments[0]
    if len(segments) > 2:
        # 가운데 구간은 부제일 수 있으므로 마지막 구간만 매체로 보고 제거
        return " | ".join(segments[:-1])
    if _looks_like_tagline(segments[0], segments[1]):
        return text
    return segments[0]


PUBLISHER_ENDINGS = ("블로그", "블로그입니다", "blog", "story", "이야기", "노트", "notes")


def _looks_like_publisher(text):
    """'조대협의 블로그' 처럼 글 제목이 아니라 매체·블로그 이름처럼 보이는지."""
    lowered = text.strip().lower()
    return any(lowered.endswith(ending) for ending in PUBLISHER_ENDINGS)


def _strip_site_suffix(text):
    """' - YouTube', ' :: 블로그명' 같은 매체 꼬리표 제거."""
    changed = True
    while changed:
        changed = False
        for suffix in SITE_SUFFIXES:
            if text.endswith(suffix):
                text = text[:-len(suffix)].rstrip()
                changed = True
    if " :: " in text:
        head, tail = text.rsplit(" :: ", 1)
        # Tistory 기본 템플릿은 '제목 :: 블로그명'과 '블로그명 :: 제목' 두 가지가 있다.
        # 앞쪽이 블로그명처럼 보이면 뒤쪽이 제목이므로 자르지 않는다.
        if not _looks_like_publisher(head):
            text = head.rstrip()
    return text


def _strip_trailing_decoration(text):
    """꼬리 해시태그·이모지 제거.

    마침표는 제거하지 않는다. 실제 커밋 subject에 마침표로 끝나는 제목이 그대로
    쓰여 있고('Forgejo – Beyond coding. We forge.'), 제거해도 일치율 이득이 없다.
    """
    text = PATTERN_TRAILING_HASHTAG.sub("", text)
    text = PATTERN_TRAILING_EMOJI.sub("", text).rstrip()
    return text


def extract_title(entry):
    """커밋 본문 한 줄('제목 URL')에서 subject에 쓸 제목만 추출.

    ' • '(컨퍼런스 발표자 표기)와 ' | '(작성자·매체 표기) 중 먼저 나오는 쪽에서 자르고,
    남은 매체 꼬리표와 장식을 제거한다. 근거가 없는 ' - ', ' — ', ' · ', ':' 에서는 자르지 않는다.
    """
    fallback = strip_url_part(entry)
    text = fallback

    bullet_at = text.find(" • ")
    pipe_at = text.find(" | ")
    if bullet_at != -1 and (pipe_at == -1 or bullet_at < pipe_at):
        text = text[:bullet_at]
    else:
        text = _cut_attribution_pipe(text)

    text = _strip_site_suffix(text)
    text = _strip_trailing_decoration(text)
    text = text.strip()
    if not text:
        text = fallback
    # 제목 자리에 URL이나 깨진 markdown이 남았으면 subject에 쓸 제목이 없는 항목이다
    if has_url(text) or text.startswith("["):
        return ""
    return text


def _running_min_heads(group):
    """'앞에 나온 어떤 항목보다 들여쓰기가 깊지 않은' URL 항목들을 머리글로 뽑는다."""
    heads, min_indent = [], None
    for indent, text in group:
        if is_header_line(text):
            # 헤더는 목록 구조에 포함하지 않는다
            continue
        if min_indent is None or indent <= min_indent:
            min_indent = indent
            if has_url(text):
                heads.append(text)
    return heads


def _shallowest_linked(group):
    """URL 있는 항목 중 가장 얕은 들여쓰기만 골라내는 보수적 대안."""
    linked = [(indent, text) for indent, text in group
              if has_url(text) and not is_header_line(text)]
    if not linked:
        return []
    base = min(indent for indent, _ in linked)
    return [text for indent, text in linked if indent == base]


def _promoted_from_indented(group):
    """전부 들여쓰인 hunk(기존 부모 아래 보강)에서 독립 북마크로 승격할 항목을 고른다.

    가장 얕은 URL 항목 중 '첫 번째 하나'만 승격한다(나머지 형제는 그 북마크의
    부속 링크·요약으로 본다). '자기 하위 줄을 가진 형제를 전부 승격'하는 규칙도
    실측했지만 399커밋 기준 일치율이 312→308로 오히려 떨어져 채택하지 않았다
    — 실제 커밋은 형제 여럿에 각자 요약이 있어도 첫 항목만 제목에 쓴 경우가 다수.
    """
    shallowest = _shallowest_linked(group)
    return shallowest[:1]


def select_subject_entries(entries):
    """subject에 기여하는 항목만 골라낸다.

    entries: (들여쓰기 깊이, 본문 텍스트, 부호, hunk 번호) 목록. 본문 순서를 유지한다.
    삭제('-')된 항목, 요약 같은 plain text 라인, '# 헤더' 라인은 기여하지 않는다.

    hunk 정보가 있으면(diff의 '@@' 헤더가 입력에 포함) hunk 단위로 판단한다:
    - 최상위(들여쓰기 0) 추가가 있는 hunk → 첫 최상위 항목 앞의 들여쓰인 구간은
      보강 규칙으로, 나머지는 running-min 규칙으로 머리글을 뽑는다
    - 전체가 들여쓰인 hunk → 기존 항목 아래에 새 북마크를 보강한 경우로 보고,
      _promoted_from_indented 규칙(하위 줄을 가진 형제만 승격) 적용
    hunk 정보가 없으면(예전 grep) 전체를 하나의 그룹으로 보고 running-min 규칙 적용.
    """
    added = [(indent, text, hunk) for indent, text, sign, hunk in entries if sign == '+']
    if not added:
        return []

    hunk_ids = []
    for _, _, hunk in added:
        if hunk not in hunk_ids:
            hunk_ids.append(hunk)

    if hunk_ids == [0]:
        # hunk 정보 없음 — 기존 전역 규칙
        group = [(indent, text) for indent, text, _ in added]
        heads = _running_min_heads(group)
        return heads if heads else _shallowest_linked(group)

    heads = []
    for hid in hunk_ids:
        group = [(indent, text) for indent, text, hunk in added if hunk == hid]
        structural = [(indent, text) for indent, text in group if not is_header_line(text)]
        if not structural:
            continue
        if min(indent for indent, _ in structural) == 0:
            # 최상위 항목이 있는 hunk. 첫 최상위 항목보다 앞의 들여쓰인 구간은
            # 직전 기존 항목에 붙은 보강이므로 보강 규칙으로 따로 처리한다
            first_top = next(i for i, (indent, text) in enumerate(group)
                             if indent == 0 and not is_header_line(text))
            if first_top > 0:
                heads.extend(_promoted_from_indented(group[:first_top]))
            heads.extend(_running_min_heads(group[first_top:]))
        else:
            # 전부 들여쓰인 hunk: 기존 부모 아래 보강 — 하위 줄을 가진 형제만 승격
            heads.extend(_promoted_from_indented(group))
    if heads:
        return heads
    return _shallowest_linked([(indent, text) for indent, text, _ in added])


def build_subject(entries):
    """subject 한 줄을 만든다. 제목들을 본문 순서대로 ', '로 연결.

    같은 항목의 제목/URL만 수정한 커밋은 옛 줄과 새 줄이 모두 남아 제목이 겹치므로
    같은 제목은 첫 번째 것만 사용한다.
    """
    titles = []
    for text in select_subject_entries(entries):
        title = extract_title(text)
        if title and title not in titles:
            titles.append(title)
    return ", ".join(titles)


def count_indent(diff_line):
    """diff 한 줄('+', '-' 로 시작)의 들여쓰기 깊이를 센다.

    본문 변환은 들여쓰기를 지우기 때문에, 지우기 전에 따로 측정해야 한다.
    """
    content = diff_line
    if content.startswith("+") or content.startswith("-"):
        content = content[1:]
    content = content.replace("\t", "  ")
    return len(content) - len(content.lstrip(" "))


TEST_DATA = [
    ('+* [산드로 만쿠소, "소프트웨어 장인정신이란…"](http://www.bloter.net/archives/251535)', '산드로 만쿠소, "소프트웨어 장인정신이란…" http://www.bloter.net/archives/251535'),
    ('+* [**산드로 만쿠소, "소프트웨어 장인정신이란…"**](http://www.bloter.net/archives/251535)', '산드로 만쿠소, "소프트웨어 장인정신이란…" http://www.bloter.net/archives/251535'),
    ('+* [산드로 만쿠소, "소프트웨어 장인정신이란…"](http://www.bloter.net/archives/251535) more explanation', '산드로 만쿠소, "소프트웨어 장인정신이란…" http://www.bloter.net/archives/251535 more explanation'),
    ('+* [**산드로 만쿠소, "소프트웨어 장인정신이란…"**](http://www.bloter.net/archives/251535) more explanation', '산드로 만쿠소, "소프트웨어 장인정신이란…" http://www.bloter.net/archives/251535 more explanation'),
    ('+* 문자열 [산드로 만쿠소, "소프트웨어 장인정신이란…"](http://www.bloter.net/archives/251535) more explanation', '문자열 산드로 만쿠소, "소프트웨어 장인정신이란…" http://www.bloter.net/archives/251535 more explanation'),
    ('  +* [산드로 만쿠소, "소프트웨어 장인정신이란…"](http://www.bloter.net/archives/251535)', '산드로 만쿠소, "소프트웨어 장인정신이란…" http://www.bloter.net/archives/251535'),
    ('  +* [**산드로 만쿠소, "소프트웨어 장인정신이란…"**](http://www.bloter.net/archives/251535) more explanation', '산드로 만쿠소, "소프트웨어 장인정신이란…" http://www.bloter.net/archives/251535 more explanation'),
    ('  +* [산드로 만쿠소, "소프트웨어 장인정신이란…" http://someurl ](http://www.bloter.net/archives/251535)', '산드로 만쿠소, "소프트웨어 장인정신이란…" http://someurl http://www.bloter.net/archives/251535'),
    ('  +* [산드로 만쿠소, "소프트웨어 장인정신이란…" http://someurl/ ](http://www.bloter.net/archives/251535)', '산드로 만쿠소, "소프트웨어 장인정신이란…" http://someurl http://www.bloter.net/archives/251535'),
    ('  +* [산드로 만쿠소, "소프트웨어 장인정신이란…" http://someurl ](http://www.bloter.net/archives/251535/)', '산드로 만쿠소, "소프트웨어 장인정신이란…" http://someurl http://www.bloter.net/archives/251535'),
    ('  +* [산드로 만쿠소, "소프트웨어 장인정신이란…" http://someurl/ ](http://www.bloter.net/archives/251535/)', '산드로 만쿠소, "소프트웨어 장인정신이란…" http://someurl http://www.bloter.net/archives/251535'),
    ('  +    * [산드로 만쿠소, "소프트웨어 장인정신이란…" http://someurl ](http://www.bloter.net/archives/251535/)', '산드로 만쿠소, "소프트웨어 장인정신이란…" http://someurl http://www.bloter.net/archives/251535'),
    ('  +    * [산드로 만쿠소, "소프트웨어 장인정신이란…" http://someurl/ ](http://www.bloter.net/archives/251535/)', '산드로 만쿠소, "소프트웨어 장인정신이란…" http://someurl http://www.bloter.net/archives/251535'),
    ('  +    * [산드로 만쿠소, "소프트웨어 장인정신이란…" http://someurl/ ](http://www.bloter.net/archives/251535?utm_source=google&ab_channel=xyz&ref=12345)', '산드로 만쿠소, "소프트웨어 장인정신이란…" http://someurl http://www.bloter.net/archives/251535'),
    ('  +* (NOT YET) [산드로 만쿠소, "소프트웨어 장인정신이란…" http://someurl/ ](http://www.bloter.net/archives/251535/)', '산드로 만쿠소, "소프트웨어 장인정신이란…" http://someurl http://www.bloter.net/archives/251535'),
]


# (본문 한 줄, 기대하는 subject 제목) — 실제 커밋 히스토리에서 가져온 문자열
TITLE_TEST_DATA = [
    # e334e87fa: ' | 작성자' 제거
    ('The future of software engineering is SRE | swizec https://swizec.com/blog/the-future-of-software-engineering-is-sre',
     'The future of software engineering is SRE'),
    # e334e87fa: ' | 매체 - YouTube' 제거, 제목 안의 ' - ' 는 유지
    ('Why 90% of Platform Engineering Fails - And How to Fix It | InfoQ - YouTube https://www.youtube.com/watch?v=X7o52n34L0M',
     'Why 90% of Platform Engineering Fails - And How to Fix It'),
    # e334e87fa: 첫 ' • '에서 자름
    ('Tech Truth: Agile Evolution & the Future of SW Engineering • Martin Fowler & Kent Beck • GOTO 2025 - YouTube https://www.youtube.com/watch?v=ii_rLjQfjp0',
     'Tech Truth: Agile Evolution & the Future of SW Engineering'),
    # c724b6401
    ('Signals & Levers • Elisabeth Hendrickson, Joel Tosi & Charles Humble • GOTO Book Club - YouTube https://www.youtube.com/watch?v=8tNtZMm3Hyc',
     'Signals & Levers'),
    # 9cf3e2ded: '제목 | 작성자 | LinkedIn' → 첫 ' | '에서 자름, 앞의 'GitHub - ' 유지
    ('GitHub - gnu-gnu/network-fundamentals-lab 공유 | 심근우 | LinkedIn https://www.linkedin.com/posts/gnu-shim_github-gnu-gnunetwork-fundamentals-lab-share-7483304706904154112-OEmZ',
     'GitHub - gnu-gnu/network-fundamentals-lab 공유'),
    # ea0ec3490
    ('AWS Agentic Stack for Scalable AI Systems | Hemant Virmani | LinkedIn https://www.linkedin.com/posts/hemantvirmani_aws-agenticai-amazonbedrock-share-7468710637490200576-DKh7',
     'AWS Agentic Stack for Scalable AI Systems'),
    # b9157bd6e: 끝의 '?' 유지
    ('정규화를 하면 정말 성능이 느려질까요? | 이병후 | LinkedIn https://www.linkedin.com/posts/example-KpPI',
     '정규화를 하면 정말 성능이 느려질까요?'),
    # 5bad207cf: 'repo: 설명 | owner' → 설명은 유지
    ('Prompt_Engineering: 22 prompt engineering techniques with hands-on Jupyter Notebook tutorials | NirDiamant https://github.com/NirDiamant/Prompt_Engineering',
     'Prompt_Engineering: 22 prompt engineering techniques with hands-on Jupyter Notebook tutorials'),
    # c5ca8215f
    ('ml-engineering: Machine Learning Engineering Open Book | stas00 https://github.com/stas00/ml-engineering',
     'ml-engineering: Machine Learning Engineering Open Book'),
    # dfdfe0e5a: 설명 안의 마침표·쉼표 유지
    ('deja: Predictive inline shell autosuggestions for zsh. Go daemon, no TUI, no sync | Giammarco-Ferranti https://github.com/Giammarco-Ferranti/deja',
     'deja: Predictive inline shell autosuggestions for zsh. Go daemon, no TUI, no sync'),
    # 960bb7872: 구분자 없음 → URL만 제거
    ('oxigraph: SPARQL graph database https://github.com/oxigraph/oxigraph',
     'oxigraph: SPARQL graph database'),
    # 73cf97c67: ' — ' 는 자르지 않음
    ('ArcticDB — the fastest Python-native DataFrame database https://arcticdb.io',
     'ArcticDB — the fastest Python-native DataFrame database'),
    # 672990ac5: arXiv id 유지
    ('2607.14159 MemoHarness: Agent Harnesses That Learn from Experience https://arxiv.org/html/2607.14159v1',
     '2607.14159 MemoHarness: Agent Harnesses That Learn from Experience'),
    # a4870b249: ' | 매체 - YouTube' 만 제거, 앞의 발표자 표기는 유지
    ('Homa: The End of TCP for AI Clusters — John Ousterhout, Stanford | AI Engineer - YouTube https://www.youtube.com/watch?v=eZ8WWZzoaR0',
     'Homa: The End of TCP for AI Clusters — John Ousterhout, Stanford'),
    # 1069862e1: 제목 자체에 ', ' 포함
    ('순서대로, 한 번만, 빠르게 | AB180 엔지니어링 https://engineering.ab180.co/stories/kafka-event-ordering-at-scale',
     '순서대로, 한 번만, 빠르게'),
    # 6f319dbbd: 끝의 '!' 유지
    ('AI가 하루 넘게 혼자 알아서 일했다! | 티타임즈TV - YouTube https://www.youtube.com/watch?v=JI9YoLVuiE4',
     'AI가 하루 넘게 혼자 알아서 일했다!'),
    # 672990ac5: 문장 중간 마침표와 끝의 '?' 유지
    ('무조건 쓰세요. 다른 터미널 툴을 압도하는 현존 최고의 IDE Orca의 특징은? | 찐AI - YouTube https://www.youtube.com/watch?v=T9mypKihAeY',
     '무조건 쓰세요. 다른 터미널 툴을 압도하는 현존 최고의 IDE Orca의 특징은?'),
    # 44f135a33: ' | ' 없이 끝에 붙은 ' - YouTube' 제거
    ('내가 대규모 트래픽을 만나면 제일 먼저 하는 일 - YouTube https://www.youtube.com/watch?v=1CRNXpfYvZE',
     '내가 대규모 트래픽을 만나면 제일 먼저 하는 일'),
    # 60f790b96: ' - Google Slides' 제거
    ('알아도 도움안되는 얕은 개발 지식들 - Google Slides https://docs.google.com/presentation/d/1T8MbP89hY3EEfxft7H2qtmOfosTerhaGtoZpk8OYSso/mobilepresent',
     '알아도 도움안되는 얕은 개발 지식들'),
    # 74d98a698: ' · GitHub' 제거
    ('딴짓하는 류주임(chrisryugj) — Public AX FDE · GitHub https://github.com/chrisryugj',
     '딴짓하는 류주임(chrisryugj) — Public AX FDE'),
    # 0d9a04079: 끝의 마침표 1개 제거
    # 꼬리 마침표는 남긴다. 실제 커밋을 보면 0d9a04079는 지웠지만 890862eb('...Here's
    # What Happened.')·Forgejo 등 6건은 그대로 두었고, 지워서 얻는 일치율 이득이 0이다.
    ('Everyone Is Hiring for Judgment. Nobody Is Making It Anymore. | The AI Corner https://www.the-ai-corner.com/p/hiring-for-judgment-ai-seniorization',
     'Everyone Is Hiring for Judgment. Nobody Is Making It Anymore.'),
    # 73a678406: 꼬리 해시태그·이모지 제거
    ('Stop crawling under your desk for an outlet! 🛑 #desksetup #anker | Kimi ASMR | Facebook Reel https://www.facebook.com/reel/1380026430883869',
     'Stop crawling under your desk for an outlet!'),
    # 4db312ffd: 뒤가 제품 태그라인이면 ' | ' 유지
    ('MyScale | Run Vector Search with SQL https://www.myscale.com',
     'MyScale | Run Vector Search with SQL'),
    # f881f884b: 태그라인 유지
    ('text-to-cad | A library of agent skills for CAD, CAE and CAM https://text-to-cad.example.com',
     'text-to-cad | A library of agent skills for CAD, CAE and CAM'),
    # 74d98a698: 앞이 한 단어면 뒤를 유지
    ('microgpt | Andrej Karpathy https://github.com/karpathy/microgpt',
     'microgpt | Andrej Karpathy'),
    # f1ab956d6: ' :: 사이트명' 제거, 제목 안의 ' - ' 유지
    ('누가 종속 소리를 내었는가! - 바이브 코딩 시대의 인프라에 대한 고찰 :: ROBOCO https://roboco.io/posts/vibe-coding-infrastructure-lock-in',
     '누가 종속 소리를 내었는가! - 바이브 코딩 시대의 인프라에 대한 고찰'),
    # f1ab956d6: 파이프 3개 중 마지막(매체)만 제거하고 부제는 유지
    ('AI에게 검증가능한 품질목표 제시하기 | 국제표준기반 품질목표 세우기 | 코딩하는기술사 - YouTube https://www.youtube.com/watch?v=example',
     'AI에게 검증가능한 품질목표 제시하기 | 국제표준기반 품질목표 세우기'),
    # ccf5e3739
    ('Introducing SWE-2: Pushing the Pareto Frontier | Cognition https://cognition.com/blog/swe-2',
     'Introducing SWE-2: Pushing the Pareto Frontier'),
    # 5de4dd0fe: ' | GeekNews' 제거, 제목 안의 ' - ' 유지
    ('Diagram Design - AI가 만드는 다이어그램에 디자인 규칙을 더하는 스킬 | GeekNews https://news.hada.io/topic?id=33664',
     'Diagram Design - AI가 만드는 다이어그램에 디자인 규칙을 더하는 스킬'),
    # 86dbbcf3e: ' - 블로그명' 은 제거하지 않음
    ('IEEE 754 부동소수점 오차와 Java의 대안 - 개발수양록 | benelog https://blog.benelog.net/floating-point-java.html',
     'IEEE 754 부동소수점 오차와 Java의 대안 - 개발수양록'),
    # 7bb2961a8: ' - <사이트>' 를 일괄로 자르면 안 되는 반례
    ('Marigold V2: Revisiting Diffusion Transformers for Monocular Depth Estimation - a Hugging Face Space by huawei-bayerlab https://huggingface.co/spaces/huawei-bayerlab/marigold-v2',
     'Marigold V2: Revisiting Diffusion Transformers for Monocular Depth Estimation - a Hugging Face Space by huawei-bayerlab'),
    # 9cf3e2ded: 설명 안의 ' — ' 유지
    ('NetScan-Pro: An interactive Bash-based network scanning tool — live host discovery, port scanning | niladri-1 https://github.com/niladri-1/NetScan-Pro',
     'NetScan-Pro: An interactive Bash-based network scanning tool — live host discovery, port scanning'),
]


# (diff 라인 목록, 기대하는 subject) — 들여쓰기에 따른 항목 선택 규칙 검증
SUBJECT_TEST_DATA = [
    # e334e87fa 축약: 최상위 항목만 subject에 들어가고 하위 링크·요약은 제외
    (['+* [The future of software engineering is SRE | swizec](https://swizec.com/blog/x)',
      '+* [Tech Truth: Agile Evolution & the Future of SW Engineering • Martin Fowler & Kent Beck • GOTO 2025 - YouTube](https://www.youtube.com/watch?v=ii_rLjQfjp0)',
      '+  * [The Tech Truth Circle | GOTO Copenhagen 2025](https://gotocph.com/2025/sessions/3780/the-tech-truth-circle)',
      '+  * Martin Fowler와 Kent Beck의 54분 대담'],
     'The future of software engineering is SRE, Tech Truth: Agile Evolution & the Future of SW Engineering'),
    # 6f319dbbd 축약: 모든 라인이 들여쓰여 있어도 가장 얕은 깊이를 기준으로 재기준화
    (['+  * [AI가 하루 넘게 혼자 알아서 일했다! | 티타임즈TV - YouTube](https://www.youtube.com/watch?v=JI9YoLVuiE4)',
      '+    * AGI 논쟁을 촉발한 GPT-6 Astra 11분 해설',
      '+  * [JEV RAG: A More Efficient Solution for RAG Systems? | Gao Dalie - YouTube](https://www.youtube.com/watch?v=sa1qESk1x-o)',
      '+    * RAG 파이프라인에서 Jev의 자리를 검증하는 9분 데모'],
     'AI가 하루 넘게 혼자 알아서 일했다!, JEV RAG: A More Efficient Solution for RAG Systems?'),
    # 헤더 라인과 URL 없는 요약 라인은 기여하지 않음
    (['+# Code Complexity',
      '+* [oxigraph: SPARQL graph database](https://github.com/oxigraph/oxigraph)',
      '+  * 요약 텍스트'],
     'oxigraph: SPARQL graph database'),
    # 같은 내용의 +/- 는 서로 상쇄되어 subject에도 본문에도 남지 않음
    (['-* [moved entry | someone](https://example.com/moved)',
      '+* [moved entry | someone](https://example.com/moved)',
      '+* [ml-engineering: Machine Learning Engineering Open Book | stas00](https://github.com/stas00/ml-engineering)'],
     'ml-engineering: Machine Learning Engineering Open Book'),
    # b79f59edb: 기존 항목의 제목만 고친 커밋 — 옛 줄과 새 줄의 제목이 같으면 한 번만
    (['-* [cs-video-courses: List of Computer Science courses with video lectures](https://github.com/Developer-Y/cs-video-courses)',
      '+* [cs-video-courses: List of Computer Science courses with video lectures | Developer-Y](https://github.com/Developer-Y/cs-video-courses)'],
     'cs-video-courses: List of Computer Science courses with video lectures'),
    # URL 없는 라인만 있으면 subject는 비어 있다
    (['+  * 요약만 추가한 경우'], ''),
    # 46ac4a60f: hunk 2개, 각각 최상위 항목 — 둘 다 subject에
    (['@@ -583,6 +583,8 @@',
      '+* [금융권 Databricks 기반 AI Agent PoC 참여 회고 | Hwan Tae Kim](https://www.linkedin.com/posts/x)',
      '+  * 보수적 금융권에서 하루 만에 Draft Agent 구축',
      '@@ -4699,6 +4701,8 @@',
      '+* [개발자들이 먼저 느끼고 있고, 다른 직군도 곧 느끼게될 내용 | Kurt Lee](https://www.linkedin.com/posts/y)',
      '+  * 특정 LLM에 충성심이 없어진 개발 현장'],
     '금융권 Databricks 기반 AI Agent PoC 참여 회고, 개발자들이 먼저 느끼고 있고, 다른 직군도 곧 느끼게될 내용'),
    # 672990ac5 축약: 전부 들여쓰인 보강 hunk → 첫 항목만 승격, 부속 링크·요약은 제외
    (['@@ -7456,6 +7456,9 @@',
      '+  * [무조건 쓰세요. 다른 터미널 툴을 압도하는 현존 최고의 IDE Orca의 특징은? | 찐AI - YouTube](https://www.youtube.com/watch?v=a)',
      '+    * 25분 소개',
      '+  * [Orca 오케스트레이션, 이렇게 쓰면 됩니다 | 아빠너구리 TV - YouTube](https://www.youtube.com/watch?v=b)',
      '@@ -5072,6 +5072,7 @@',
      '+  * [llmfit 공식 사이트](https://www.llmfit.org/)'],
     '무조건 쓰세요. 다른 터미널 툴을 압도하는 현존 최고의 IDE Orca의 특징은?, llmfit 공식 사이트'),
    # 최상위와 보강 hunk 혼합: 최상위 hunk의 하위 링크는 제외, 보강 hunk는 첫 항목 승격
    (['@@ -100,3 +100,6 @@',
      '+* [SLayer - The open-source semantic layer for AI agents | Motley](https://motley.ai/slayer/)',
      '+  * [slayer: An embeddable, expressive semantic layer | MotleyAI](https://github.com/MotleyAI/slayer)',
      '+  * 요약',
      '@@ -3984,2 +3987,3 @@',
      '+  * [Sakana Fugu — Multi-agent System as A Model](https://sakana.ai/fugu/)',
      '+  * [2606.21228 Sakana Fugu Technical Report](https://arxiv.org/html/2606.21228)'],
     'SLayer - The open-source semantic layer for AI agents, Sakana Fugu — Multi-agent System as A Model'),
]


def collect_entries(lines):
    """diff 라인들을 (들여쓰기, 본문 텍스트, 부호, hunk 번호) 목록으로 변환.

    같은 내용의 추가/삭제 라인은 서로 상쇄시킨다(기존 동작 유지).
    부호('+'/'-')와 hunk 번호는 subject 선별에만 쓴다. 본문에는 삭제 라인도 그대로 남긴다.
    '@@' hunk 헤더 라인은 그룹 경계로만 쓰고 본문에는 내보내지 않는다.
    hunk 헤더가 입력에 없으면(예전 grep 패턴) 모든 라인이 hunk 0으로 묶인다.
    """
    lines_to_log_dict, counter, hunk = {}, 1, 0
    for line in lines:
        if line.startswith('@@'):
            hunk += 1
            continue
        if line.startswith('+') or line.startswith('-'):
            item = line[1:].strip()
            if item in lines_to_log_dict:
                del lines_to_log_dict[item]
            else:
                lines_to_log_dict[item] = (counter, count_indent(line), line[0], hunk)
                counter += 1
    return [
        (indent, convert_markdown_to_clean_text(item, DISALLOWED_PARAMS), sign, hunk)
        for item, (_, indent, sign, hunk) in lines_to_log_dict.items()
    ]


def rebase_indents(entries):
    """본문 출력용 들여쓰기를 hunk별로 재기준화한다.

    각 hunk의 최소 들여쓰기를 0으로 맞추고 상대 들여쓰기만 유지한다.
    e.g. 기존 항목 아래 2/4/4로 보강된 그룹은 본문에서 0/2/2가 된다
    (실제 커밋 본문의 관례 — app.md KiwiDesk 커밋, 6f319dbbd 등).
    """
    min_by_hunk = {}
    for indent, _, _, hunk in entries:
        if hunk not in min_by_hunk or indent < min_by_hunk[hunk]:
            min_by_hunk[hunk] = indent
    return [
        (indent - min_by_hunk[hunk], text, sign, hunk)
        for indent, text, sign, hunk in entries
    ]


def format_output(entries):
    """클립보드에 담을 최종 커밋 메시지 텍스트를 만든다.

    - 변경이 한 줄뿐이면 그 줄 하나만(제목 축약 없이) 출력한다 — subject/본문
      구분이 필요 없다 (관례: 단일 항목 커밋은 본문 라인이 곧 subject).
    - 여러 줄이면 subject + 빈 줄 + 본문. 본문은 재기준화한 들여쓰기를 유지한다.
    """
    rebased = rebase_indents(entries)
    if len(rebased) == 1:
        return rebased[0][1]

    body_lines = [" " * indent + text for indent, text, _, _ in rebased]
    subject = build_subject(entries)
    if subject:
        return subject + "\n\n" + "\n".join(body_lines)
    return "\n".join(body_lines)


# (diff 라인 목록, 기대하는 전체 출력) — 단일 항목·들여쓰기 재기준화 검증
FORMAT_TEST_DATA = [
    # writing.md 최신 커밋: 1줄 변경 → 그 줄 하나만 (들여쓰기·제목 축약 없이)
    (['@@ -142,2 +142,3 @@',
      '+  * [LLM에게 글을 쓰게 하지 말고 교정하게 하라: AI 시대의 글쓰기 원칙 | digitalbourgeois](https://digitalbourgeois.tistory.com/3700)'],
     'LLM에게 글을 쓰게 하지 말고 교정하게 하라: AI 시대의 글쓰기 원칙 | digitalbourgeois https://digitalbourgeois.tistory.com/3700'),
    # app.md KiwiDesk 커밋: 2/4/4 보강 hunk → 본문 0/2/2 재기준화
    (['@@ -2069,0 +2070,3 @@',
      '+  * [KiwiDesk — Tiling that feels like it shipped with macOS](https://kiwidesk.kiwicanopy.com/)',
      '+    * [kiwidesk: Settings instead of config files | kiwicanopy](https://github.com/kiwicanopy/kiwidesk)',
      '+    * 설정 파일 대신 GUI 설정. Swift'],
     'KiwiDesk — Tiling that feels like it shipped with macOS\n\n'
     'KiwiDesk — Tiling that feels like it shipped with macOS https://kiwidesk.kiwicanopy.com\n'
     '  kiwidesk: Settings instead of config files | kiwicanopy https://github.com/kiwicanopy/kiwidesk\n'
     '  설정 파일 대신 GUI 설정. Swift'),
    # 최상위 hunk: 들여쓰기 0/2 그대로 유지
    (['@@ -10,0 +10,3 @@',
      '+* [oxigraph: SPARQL graph database](https://github.com/oxigraph/oxigraph)',
      '+  * [소개 글 | 저자](https://example.com/intro)',
      '+  * 요약 텍스트'],
     'oxigraph: SPARQL graph database\n\n'
     'oxigraph: SPARQL graph database https://github.com/oxigraph/oxigraph\n'
     '  소개 글 | 저자 https://example.com/intro\n'
     '  요약 텍스트'),
    # hunk 2개: 각 hunk가 따로 재기준화
    (['@@ -1,0 +1,1 @@',
      '+  * [llmfit 공식 사이트](https://www.llmfit.org/)',
      '@@ -50,0 +52,2 @@',
      '+* [strata: one-click install | niko1221](https://github.com/niko1221/strata)',
      '+  * 게이밍 PC에서 125B MoE 구동'],
     'llmfit 공식 사이트, strata: one-click install\n\n'
     'llmfit 공식 사이트 https://www.llmfit.org\n'
     'strata: one-click install | niko1221 https://github.com/niko1221/strata\n'
     '  게이밍 PC에서 125B MoE 구동'),
]


def run_tests():
    """단위 테스트 실행. 실패 개수를 반환."""
    failed = 0

    for i, (raw, expected) in enumerate(TEST_DATA):
        if raw.startswith('+') or raw.startswith('-'):
            raw = raw[1:]
        real = convert_markdown_to_clean_text(raw, DISALLOWED_PARAMS)
        if real == expected:
            print(f'body case {i} successful')
        else:
            failed += 1
            print(f'body case {i} failed')
            print(f'{raw}\n\texpected {expected}\n\treal     {real}')

    for i, (entry, expected) in enumerate(TITLE_TEST_DATA):
        real = extract_title(entry)
        if real == expected:
            print(f'title case {i} successful')
        else:
            failed += 1
            print(f'title case {i} failed')
            print(f'{entry}\n\texpected {expected}\n\treal     {real}')

    for i, (lines, expected) in enumerate(SUBJECT_TEST_DATA):
        real = build_subject(collect_entries(lines))
        if real == expected:
            print(f'subject case {i} successful')
        else:
            failed += 1
            print(f'subject case {i} failed')
            print(f'\texpected {expected}\n\treal     {real}')

    for i, (lines, expected) in enumerate(FORMAT_TEST_DATA):
        real = format_output(collect_entries(lines))
        if real == expected:
            print(f'format case {i} successful')
        else:
            failed += 1
            print(f'format case {i} failed')
            print(f'\texpected {expected!r}\n\treal     {real!r}')

    total = (len(TEST_DATA) + len(TITLE_TEST_DATA)
             + len(SUBJECT_TEST_DATA) + len(FORMAT_TEST_DATA))
    print(f'{total - failed}/{total} cases passed, {failed} failed')
    return failed


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'test':
        sys.exit(1 if run_tests() else 0)
    else:
        entries = collect_entries(sys.stdin)
        output = format_output(entries)
        if output:
            print(output)
