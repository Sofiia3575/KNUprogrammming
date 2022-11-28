import os
import sys
from datetime import datetime, timedelta
import tarfile
def archive(folder, date_now):
    files = os.listdir()

    for it in files:

        if os.path.isfile(it) and it.endwith(".log"):
            path = os.path.join(os.getcwd(), it)
            time1 = os.path.getmtime(path)

            if time1 < date_now:
                lst.append(path)
    if lst:
        arch_file = os.path.join(os.getcwd(), date_now.strftime("%Y%m%d_%H%M%S") + ".tar.gz")
        with tarfile.open(arch_file, "w:gz") as tf:
            for it in lst:
                tf.add(it)
                os.remove(path)
if __name__ == "__main__":
    now = datetime.datetime.now()
    folder = input("Folder")
    archive(date_now)