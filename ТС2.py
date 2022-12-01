import threading
from queue import Queue
from time import time, sleep
import logging


logging.basicConfig(level=logging.DEBUG)

T1 = 1
T2 = 2

q = Queue()
start = time()


def log(message: str):
    t = time() - start
    name = threading.current_thread().getName()
    logging.debug("[%6.3f] %s: %s", t, name, message)


def put(count, process_time):
    for i in range(count):
        sleep(process_time)
        message = f"ПОВІДОМЛЕННЯ {i} (створено о {time() - start:6.3f})"
        log(f"В чергу додано   {message}")
        q.put(message)


def get(count, process_time):
    for i in range(count):
        message = q.get()
        log(f"З черги отримано {message}")
        sleep(process_time)
        print(f"\"{message}\" оброблене на {time() - start:6.3f} секунді")


if name == "main":
    n = 10
    th1 = threading.Thread(name="Put", target=put, args=(n, T1))
    th2 = threading.Thread(name="Get", target=get, args=(n, T2))
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    log("Кінець!")