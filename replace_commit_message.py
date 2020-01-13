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


data = [('+* [산드로 만쿠소, “소프트웨어 장인정신이란…”](http://www.bloter.net/archives/251535)', '산드로 만쿠소, “소프트웨어 장인정신이란…” http://www.bloter.net/archives/251535'),
        ('+* [**산드로 만쿠소, “소프트웨어 장인정신이란…”**](http://www.bloter.net/archives/251535)', '산드로 만쿠소, “소프트웨어 장인정신이란…” http://www.bloter.net/archives/251535'),
        ('+* [산드로 만쿠소, “소프트웨어 장인정신이란…”](http://www.bloter.net/archives/251535) more explanation', '산드로 만쿠소, “소프트웨어 장인정신이란…” http://www.bloter.net/archives/251535 more explanation'),
        ('+* [**산드로 만쿠소, “소프트웨어 장인정신이란…”**](http://www.bloter.net/archives/251535) more explanation', '산드로 만쿠소, “소프트웨어 장인정신이란…” http://www.bloter.net/archives/251535 more explanation'),
        ('+* 문자열 [산드로 만쿠소, “소프트웨어 장인정신이란…”](http://www.bloter.net/archives/251535) more explanation', '산드로 만쿠소, “소프트웨어 장인정신이란…” http://www.bloter.net/archives/251535 more explanation'),
        ('  +* [산드로 만쿠소, “소프트웨어 장인정신이란…”](http://www.bloter.net/archives/251535)', '산드로 만쿠소, “소프트웨어 장인정신이란…” http://www.bloter.net/archives/251535'),
        ('  +* [**산드로 만쿠소, “소프트웨어 장인정신이란…”**](http://www.bloter.net/archives/251535) more explanation', '산드로 만쿠소, “소프트웨어 장인정신이란…” http://www.bloter.net/archives/251535 more explanation'),
        ('  +* [산드로 만쿠소, “소프트웨어 장인정신이란…” http://someurl ](http://www.bloter.net/archives/251535)', '산드로 만쿠소, “소프트웨어 장인정신이란…” http://someurl http://www.bloter.net/archives/251535'),
        ('  +* [산드로 만쿠소, “소프트웨어 장인정신이란…” http://someurl/ ](http://www.bloter.net/archives/251535)', '산드로 만쿠소, “소프트웨어 장인정신이란…” http://someurl http://www.bloter.net/archives/251535'),
        ('  +* [산드로 만쿠소, “소프트웨어 장인정신이란…” http://someurl ](http://www.bloter.net/archives/251535/)', '산드로 만쿠소, “소프트웨어 장인정신이란…” http://someurl http://www.bloter.net/archives/251535'),
        ('  +* [산드로 만쿠소, “소프트웨어 장인정신이란…” http://someurl/ ](http://www.bloter.net/archives/251535/)', '산드로 만쿠소, “소프트웨어 장인정신이란…” http://someurl http://www.bloter.net/archives/251535'),
        ('  +    * [산드로 만쿠소, “소프트웨어 장인정신이란…” http://someurl ](http://www.bloter.net/archives/251535/)', '산드로 만쿠소, “소프트웨어 장인정신이란…” http://someurl http://www.bloter.net/archives/251535'),
        ('  +    * [산드로 만쿠소, “소프트웨어 장인정신이란…” http://someurl/ ](http://www.bloter.net/archives/251535/)', '산드로 만쿠소, “소프트웨어 장인정신이란…” http://someurl http://www.bloter.net/archives/251535'),
        ('  +* (NOT YET) [산드로 만쿠소, “소프트웨어 장인정신이란…” http://someurl/ ](http://www.bloter.net/archives/251535/)', '산드로 만쿠소, “소프트웨어 장인정신이란…” http://someurl http://www.bloter.net/archives/251535'),
        ]


if __name__ == '__main__':
    if 2 == len(sys.argv) and sys.argv[1] == 'test':
        for i, (raw, expected) in enumerate(data):
            real = removeUnnecessaryPart(raw)
            if real:
                print(f'case {i} successful')
            else:
                print(f'{raw}\n\texpected {expected}\n\treal {real}\n\tresult {expected == real}')
    else:
        for line in sys.stdin:
            print(removeUnnecessaryPart(line))
