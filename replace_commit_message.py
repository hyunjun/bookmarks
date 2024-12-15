from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

import re
import sys


#PATTERN_BASIC = re.compile(r'^[ \t]*\+\* \[(\*\*){0,1}(?P<title>.+)(\*\*){0,1}\]\((?P<addr>.+)\)')
#PATTERN_BASIC = re.compile(r'^[ \t]*\+[ \t]*\* (\(NOT YET\) )?\[(?P<title>.+)\]\((?P<addr>.+)\)')
PATTERN_BASIC = re.compile(r'^[ \t]*\+[ \t]*\* (.+)?\[(?P<title>.+)\]\((?P<addr>.+)\)')
PATTERN_URL_INSIDE_BRACKET = re.compile(r'http(.)+(?P<ending_bracket>(/){0,1}\])')


def removeUnnecessaryPart(line):
    line = line.replace('[**', '[').replace('**]', ']').replace('/]', ']').replace('/)', ')')#.replace('(NOT YET)', '')
    m = PATTERN_URL_INSIDE_BRACKET.search(line)
    if m:
        line = re.sub(r'/? \]\(', '](', line)
    return re.sub(PATTERN_BASIC, r'\g<title> \g<addr>', line).strip()


# 특정 파라미터를 제거하며 URL을 정리하는 함수
def clean_url(url, disallowed_params=None):
    """
    URL에서 특정 파라미터를 제거하고 정리.

    :param url: 원본 URL
    :param disallowed_params: 제거할 파라미터 이름 리스트. None이면 모든 파라미터 유지.
    :return: 정리된 URL
    """
    # URL 파싱
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)

    # 제거할 파라미터 필터링
    if disallowed_params is not None:
        filtered_params = {k: v for k, v in query_params.items() if k not in disallowed_params}
    else:
        filtered_params = query_params  # 모든 파라미터 유지

    # 새 쿼리 문자열 생성
    cleaned_query = urlencode(filtered_params, doseq=True)

    # 정리된 URL 재구성
    cleaned_url = urlunparse(parsed_url._replace(query=cleaned_query))
    return cleaned_url


disallowed_parameters = ["ab_channel", "ref", "utm_source"]  # 제거할 파라미터


# Markdown을 분석하고 정리하는 함수
def convert_markdown_to_clean_text(markdown, disallowed_params=None):
    m = PATTERN_URL_INSIDE_BRACKET.search(markdown)
    if m:
        markdown = re.sub(r'/? \]\(', '](', markdown)

    # Markdown URL 패턴 정규식
    pattern = re.compile(r"\[([^\]]+)\]\((http[s]?://[^\)]+)\)")

    # 텍스트와 URL 정리
    def replacer(match):
        text = match.group(1)
        url = match.group(2)
        cleaned_url = clean_url(url, disallowed_params)
        cleaned_url = cleaned_url[:-1] if cleaned_url.endswith('/') else cleaned_url
        return f"{text} {cleaned_url}"

    markdown = markdown.replace('(NOT YET)', '')

    # **bold text** 정리
    #print(f'markdown {markdown}')
    markdown = re.sub(r"\*\*([^*]+)\*\*", r"\1", markdown)
    #print(f'markdown {markdown}')

    # Markdown 문장에서 앞의 *, - 제거
    cleaned_markdown = re.sub(r"^\s*[\+\*\-\s]+", "", markdown)
    #print(f'cleaned markdown {cleaned_markdown}')

    # Markdown 문장을 원하는 형태로 변환
    return pattern.sub(replacer, cleaned_markdown).strip()


data = [('+* [산드로 만쿠소, “소프트웨어 장인정신이란…”](http://www.bloter.net/archives/251535)', '산드로 만쿠소, “소프트웨어 장인정신이란…” http://www.bloter.net/archives/251535'),
        ('+* [**산드로 만쿠소, “소프트웨어 장인정신이란…”**](http://www.bloter.net/archives/251535)', '산드로 만쿠소, “소프트웨어 장인정신이란…” http://www.bloter.net/archives/251535'),
        ('+* [산드로 만쿠소, “소프트웨어 장인정신이란…”](http://www.bloter.net/archives/251535) more explanation', '산드로 만쿠소, “소프트웨어 장인정신이란…” http://www.bloter.net/archives/251535 more explanation'),
        ('+* [**산드로 만쿠소, “소프트웨어 장인정신이란…”**](http://www.bloter.net/archives/251535) more explanation', '산드로 만쿠소, “소프트웨어 장인정신이란…” http://www.bloter.net/archives/251535 more explanation'),
        ('+* 문자열 [산드로 만쿠소, “소프트웨어 장인정신이란…”](http://www.bloter.net/archives/251535) more explanation', '문자열 산드로 만쿠소, “소프트웨어 장인정신이란…” http://www.bloter.net/archives/251535 more explanation'),
        ('  +* [산드로 만쿠소, “소프트웨어 장인정신이란…”](http://www.bloter.net/archives/251535)', '산드로 만쿠소, “소프트웨어 장인정신이란…” http://www.bloter.net/archives/251535'),
        ('  +* [**산드로 만쿠소, “소프트웨어 장인정신이란…”**](http://www.bloter.net/archives/251535) more explanation', '산드로 만쿠소, “소프트웨어 장인정신이란…” http://www.bloter.net/archives/251535 more explanation'),
        ('  +* [산드로 만쿠소, “소프트웨어 장인정신이란…” http://someurl ](http://www.bloter.net/archives/251535)', '산드로 만쿠소, “소프트웨어 장인정신이란…” http://someurl http://www.bloter.net/archives/251535'),
        ('  +* [산드로 만쿠소, “소프트웨어 장인정신이란…” http://someurl/ ](http://www.bloter.net/archives/251535)', '산드로 만쿠소, “소프트웨어 장인정신이란…” http://someurl http://www.bloter.net/archives/251535'),
        ('  +* [산드로 만쿠소, “소프트웨어 장인정신이란…” http://someurl ](http://www.bloter.net/archives/251535/)', '산드로 만쿠소, “소프트웨어 장인정신이란…” http://someurl http://www.bloter.net/archives/251535'),
        ('  +* [산드로 만쿠소, “소프트웨어 장인정신이란…” http://someurl/ ](http://www.bloter.net/archives/251535/)', '산드로 만쿠소, “소프트웨어 장인정신이란…” http://someurl http://www.bloter.net/archives/251535'),
        ('  +    * [산드로 만쿠소, “소프트웨어 장인정신이란…” http://someurl ](http://www.bloter.net/archives/251535/)', '산드로 만쿠소, “소프트웨어 장인정신이란…” http://someurl http://www.bloter.net/archives/251535'),
        ('  +    * [산드로 만쿠소, “소프트웨어 장인정신이란…” http://someurl/ ](http://www.bloter.net/archives/251535/)', '산드로 만쿠소, “소프트웨어 장인정신이란…” http://someurl http://www.bloter.net/archives/251535'),
        ('  +    * [산드로 만쿠소, “소프트웨어 장인정신이란…” http://someurl/ ](http://www.bloter.net/archives/251535?utm_source=google&ab_channel=xyz&ref=12345)', '산드로 만쿠소, “소프트웨어 장인정신이란…” http://someurl http://www.bloter.net/archives/251535'),
        ('  +* (NOT YET) [산드로 만쿠소, “소프트웨어 장인정신이란…” http://someurl/ ](http://www.bloter.net/archives/251535/)', '산드로 만쿠소, “소프트웨어 장인정신이란…” http://someurl http://www.bloter.net/archives/251535'),
        ]


if __name__ == '__main__':
    if 2 == len(sys.argv) and sys.argv[1] == 'test':
        #for i, (raw, expected) in enumerate(data):
        #    real = removeUnnecessaryPart(raw)
        #    if real == expected:
        #        print(f'case {i} successful')
        #    else:
        #        print(f'{raw}\n\texpected {expected}\n\treal {real}\n\tresult {expected == real}')
        for i, (raw, expected) in enumerate(data):
            if raw.startswith('+') or raw.startswith('-'):
                raw = raw[1:]
            real = convert_markdown_to_clean_text(raw, disallowed_parameters)
            if real == expected:
                print(f'case {i} successful')
            else:
                print(f'case {i} failed')
                print(f'{key}\n\texpected {expected}\n\treal {real}\n\tresult {expected == real}')
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
            print(convert_markdown_to_clean_text(key, disallowed_parameters))
