import os
import sys
import time
from datetime import timedelta


def compare(dir1, dir2):
    set1 = set(os.listdir(dir1))
    set2 = set(os.listdir(dir2))

    for name in set1 & set2:
        fullname1 = os.path.join(dir1, name)
        fullname2 = os.path.join(dir2, name)

        if os.path.isfile(fullname1) and os.path.isfile(fullname2):
            ctime1 = os.path.getctime(fullname1)
            ctime2 = os.path.getctime(fullname2)

            if ctime1 < ctime2:
                date1 = time.ctime(ctime1)
                date2 = time.ctime(ctime2)
                print(
                    f"Файл {name} ({date1}) з каталогу {dir1} було створено раніше "
                    f"за файл {name} ({date2}) з каталогу {dir2}."
                )
            elif ctime1 > ctime2:
                date1 = time.ctime(ctime1)
                date2 = time.ctime(ctime2)
                print(
                    f"Файл {name} ({date1}) з каталогу {dir1} було створено пізніше "
                    f"за файл {name} ({date2}) з каталогу {dir2}."
                )
            else:
                print(f"Файли {name} було створено одночасно.")

            print("Різниця в часі: ", timedelta(seconds=abs(ctime2 - ctime1)))


if __name__ == "__main__":
    dir1 = "dir1"
    dir2 = "dir2"
    # print(os.getcwd())
    root = sys.path[0]
    os.chdir(root)
    compare(dir1, dir2)