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


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'test':
        for i, (raw, expected) in enumerate(TEST_DATA):
            if raw.startswith('+') or raw.startswith('-'):
                raw = raw[1:]
            real = convert_markdown_to_clean_text(raw, DISALLOWED_PARAMS)
            if real == expected:
                print(f'case {i} successful')
            else:
                print(f'case {i} failed')
                print(f'{raw}\n\texpected {expected}\n\treal     {real}')
    else:
        lines_to_log_dict, counter = {}, 1
        for line in sys.stdin:
            if line.startswith('+') or line.startswith('-'):
                item = line[1:].strip()
                if item in lines_to_log_dict:
                    del lines_to_log_dict[item]
                else:
                    lines_to_log_dict[item] = counter
                    counter += 1
        for key, value in lines_to_log_dict.items():
            print(convert_markdown_to_clean_text(key, DISALLOWED_PARAMS))
