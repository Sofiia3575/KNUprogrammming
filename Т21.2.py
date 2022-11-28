import re


SENTENCE = r"\b[A-ZА-ЯІЇЄ].*?[\.\!\?](?<![A-ZА-ЯІЇЄ\.][a-zа-яіїє]\.)(?=\s|$)"


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as inp:
        text = inp.read()
        rgx = re.compile(SENTENCE, flags=re.MULTILINE)
        sentences = rgx.findall(text)
        print(*sentences[:30], sep="\n~\n")
        with open("output.txt", "w", encoding="utf-8") as out:
            print(*sentences, sep="\n~\n", file=out)