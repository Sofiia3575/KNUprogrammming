import re

NAME1 = r"^(?P<name1>(?:[a-zA-Z]{2,})\s(?:[a-zA-Z]{1,}'?-?[a-zA-Z]{2,})\s(?:([a-zA-Z]{1,})?))"
NAME2 = r"^(?P<name2>(?:[a-zA-Z]{2,})\s(?:[a-zA-Z]{1}[\.]?)\s(?:([a-zA-Z]{1}[\.]?)))"
PHONE = r"(?P<phone>[\+\'0']\d[0-9]{11})"
DEBT = r"(?P<debt>.*)"
PATTERN1 = NAME1 + " " + PHONE + " " + DEBT
PATTERN2 = NAME2 + " " + PHONE + " " + DEBT

if __name__ == "__main__":
    with open("idebt.txt", "r", encoding="utf-8") as inp:
        text = inp.read()

    names = []
    phones = []
    debts = []

    for match in re.finditer(PATTERN1, text, re.MULTILINE | re.IGNORECASE):
        names.append(f"<{match.group('name1')}>")
        phones.append(f"<{match.group('phone')}>")
        debts.append(f"<{match.group('debt')}>")
    for match in re.finditer(PATTERN2, text, re.MULTILINE | re.IGNORECASE):
        names.append(f"<{match.group('name2')}>")
        phones.append(f"<{match.group('phone')}>")
        debts.append(f"<{match.group('debt')}>")

    print(*zip(names, *zip(phones, debts)), sep="\n")

    with open("odebt.txt", "w", encoding="utf-8") as out:
        print(*set(names), sep="\n", file=out)