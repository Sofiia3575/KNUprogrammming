import threading
from time import sleep, time
import random
import logging


logging.basicConfig(level=logging.DEBUG)

T1 = 1
T2 = 5
T3 = 0
T4 = 30

lock = threading.Lock()
start = time()


def log(message: str):
    t = time() - start
    name = threading.current_thread().getName()
    logging.debug("[%6.3f] %s: %s", t, name, message)


def train(trans_time, arr_time):
    sleep(arr_time)
    log("прибув до ділянки")
    with lock:
        log(f"почав проходити ділянку")
        sleep(trans_time)
    log("пройшов ділянку")
    print(f"{threading.current_thread().getName()} пройшов ділянку.")


if __name__ == "__main__":
    n = 10
    ths = []
    for i in range(n):
        transit_time = random.random() * (T2 - T1) + T1
        arrive_time = random.random() * (T4 - T3) + T3
        ths.append(
            threading.Thread(
                target=train,
                args=(transit_time, arrive_time),
                name=f"Потяг {i}"
            )
        )
        print(
            f"Потяг {i} прибуває о {arrive_time:6.3f} "
            f"і проходить ділянку за {transit_time:6.3f}"
        )

    for th in ths:
        th.start()
    for th in ths:
        th.join()
    log("всі потяги пройшли ділянку")