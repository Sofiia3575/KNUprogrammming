import re


DATE1 = r"\b(?P<y1>\d{1,4})/(?P<m1>\d{1,2})/(?P<d1>\d{1,2})"
DATE2 = r"\b(?P<d2>\d{1,2})\.(?P<m2>\d{1,2})\.(?P<y2>\d{1,4})"
DATE3 = r"\b(?P<y3>\d{1,4})\-(?P<m3>\d{1,2})\-(?P<d3>\d{1,2})"
DATE = DATE1 + "|" + DATE2 + "|" + DATE3


def change_dates(string, n):

    def _change_date(match):
        date = match.group()
        if "/" in date:
            k = "1"
        elif "." in date:
            k = "2"
        else:
            k = "3"

        y = match.group("y" + k)
        m = match.group("m" + k)
        d = match.group("d" + k)

        while len(y) != 4:
            y = "0" + y
        if len(m) != 2:
            m = "0" + m
        if len(d) != 2:
            d = "0" + d

        if n == 1:
            date = "/".join((y, m, d))
        elif n == 2:
            date = ".".join((d, m, y))
        else:
            date = "-".join((y, m, d))
        return date

    return re.sub(DATE, _change_date, string)


if __name__ == "__main__":
    n = int(input())

    with open("input.txt", "r", encoding="utf-8") as inp:
        s = inp.read()
        s = change_dates(s, n)
    with open("output.txt", "w", encoding="utf-8") as out:
        out.write(s)