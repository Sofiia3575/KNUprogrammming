import re


DATE1 = r"\b\d{1,2}\.\d{1,2}\.\d{1,4}\b"
DATE2 = r"\b\d{1,4}/\d{1,2}/\d{1,2}\b"
DATE = DATE1 + "|" + DATE2


def _change_date(match):
    date = match.group()
    if "." in date:
        d, m, y = date.split(".")
    else:
        y, m, d = date.split("/")
    while len(y) != 4:
        y = "0" + y
    if len(m) != 2:
        m = "0" + m
    if len(d) != 2:
        d = "0" + d
    date = ".".join((d, m, y))
    return date


def change_dates(string):
    return re.sub(DATE, _change_date, string)


if __name__ == "__main__":
    s = """Some text.
Date 1: 2020/10/21
Date 2: 2020-10-22
Date 3: 23.10.2020
Another dates: 1.1.989. :8/8/8: a7/7/7! 06-05-04! ^3-2-1!
More dates: 2.10.1999, 1988-09-3, 09.2.2003, 2008/11/11."""
    s = change_dates(s)
    print(s)

    with open("input.txt", "r", encoding="utf-8") as inp:
        s = inp.read()
        s = change_dates(s)
    with open("output.txt", "w", encoding="utf-8") as out:
        out.write(s)