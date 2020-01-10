import re
import sys


p = re.compile(r'^[ \t]*\+\* \[(\*\*){0,1}(?P<title>.+)(\*\*){0,1}\]\((?P<addr>.+)\)')


def removeUnnecessaryPart(line):
    line = line.replace('[**', '[').replace('**]', ']')
    return re.sub(p, r'\g<title> \g<addr>', line)


data = [('+* [산드로 만쿠소, “소프트웨어 장인정신이란…”](http://www.bloter.net/archives/251535)', '산드로 만쿠소, “소프트웨어 장인정신이란…” http://www.bloter.net/archives/251535'),
        ('+* [**산드로 만쿠소, “소프트웨어 장인정신이란…”**](http://www.bloter.net/archives/251535)', '산드로 만쿠소, “소프트웨어 장인정신이란…” http://www.bloter.net/archives/251535'),
        ('+* [산드로 만쿠소, “소프트웨어 장인정신이란…”](http://www.bloter.net/archives/251535) more explanation', '산드로 만쿠소, “소프트웨어 장인정신이란…” http://www.bloter.net/archives/251535 more explanation'),
        ('+* [**산드로 만쿠소, “소프트웨어 장인정신이란…”**](http://www.bloter.net/archives/251535) more explanation', '산드로 만쿠소, “소프트웨어 장인정신이란…” http://www.bloter.net/archives/251535 more explanation'),
        ('  +* [산드로 만쿠소, “소프트웨어 장인정신이란…”](http://www.bloter.net/archives/251535)', '산드로 만쿠소, “소프트웨어 장인정신이란…” http://www.bloter.net/archives/251535'),
        ('  +* [**산드로 만쿠소, “소프트웨어 장인정신이란…”**](http://www.bloter.net/archives/251535) more explanation', '산드로 만쿠소, “소프트웨어 장인정신이란…” http://www.bloter.net/archives/251535 more explanation'),
        ]


if __name__ == '__main__':
    if 2 == len(sys.argv) and sys.argv[1] == 'test':
        for raw, expected in data:
            real = removeUnnecessaryPart(raw)
            print(f'{raw}\n\texpected {expected}\n\treal {real}\n\tresult {expected == real}')
    else:
        for line in sys.stdin:
            print(removeUnnecessaryPart(line))
