import os
import sys


def compare(dir1, dir2):
    set1 = set(os.listdir(dir1))
    set2 = set(os.listdir(dir2))

    print(
        f"Файли, що присутні в одному каталозі та "
        f"відсутні в іншому ({dir1}, {dir2}):"
    )
    for name in set1 ^ set2:
        print(name)

    for name in set1 & set2:
        fullname1 = os.path.join(dir1, name)
        fullname2 = os.path.join(dir2, name)
        if os.path.isfile(fullname1):
            f1 = open(fullname1, "rb")
            f2 = open(fullname2, "rb")
            if f1.read() != f2.read():
                print(name)
            f1.close()
            f2.close()


if __name__ == "__main__":
    newout = open("output.txt", "w", encoding="utf-8")
    oldout = sys.stdout
    sys.stdout = newout

    dir1 = os.path.join(sys.path[0], "dir1")
    dir2 = os.path.join(sys.path[0], "dir2")
    compare(dir1, dir2)

    sys.stdout = oldout
    newout.close()