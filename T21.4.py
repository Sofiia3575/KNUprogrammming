import re
import datetime

DATE1 = r"\b(?P<d1>\d{1,2})\.(?P<m1>\d{1,2})\.(?P<y1>\d{1,4})"
DATE2 = r"\b(\w{1,2})\.(\w{1,2})\.(\w{1,4})"
DATE = DATE1 + "|" + DATE2


def change_dates(string):

    def _change_date(match):
        now = datetime.datetime.now()

        date = match.group()
        if "_" in date:
            y = now.strftime("%Y")
            m = now.strftime("%m")
            d = now.strftime("%d")
        else:
            k = "1"
            y = match.group("y" + k)
            m = match.group("m" + k)
            d = match.group("d" + k)

        while len(y) != 4:
            y = "0" + y
        if len(m) != 2:
            m = "0" + m
        if len(d) != 2:
            d = "0" + d

        date = ".".join((d, m, y))

        return date

    return re.sub(DATE, _change_date, string)


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as inp:
        s = inp.read()
        s = change_dates(s)
    with open("output.txt", "w", encoding="utf-8") as out:
        out.write(s)