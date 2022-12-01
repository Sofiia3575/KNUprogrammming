from threading import Thread
from time import sleep
import logging


logging.basicConfig(level=logging.DEBUG)


class ThreadWithException(Thread):

    def init(self, target=None, args=(), kwargs=()):
        super().init()

        self._f = target
        self._f_args = args
        self._f_kwargs = kwargs if kwargs else {}
        self._exception = None
        self._result = None

    def run(self):
        try:
            self._result = self._f(*self._f_args, **self._f_kwargs)
        except Exception as e:
            self._exception = e

    def get_result(self):
        return self._result

    def get_exception(self):
        return self._exception


def fact(n):
    result = 1
    for i in range(1, n + 1):
        logging.debug(f"Обчислення нерекурсивного факторіалу для {i}")
        result *= i
        logging.debug(f"Нерекурсивний факторіал для {i} дорівнює {result}")
        sleep(0)
    return result


def fact_rec(n):
    logging.debug(f"Обчислення рекурсивного факторіалу для {n}")
    if n == 0:
        result = 1
    else:
        result = n * fact_rec(n - 1)
    logging.debug(f"Нерекурсивний факторіал для {n} дорівнює {result}")
    sleep(0)
    return result


if name == "main":
    n = 40

    th1 = ThreadWithException(target=fact, args=(n, ))
    th2 = ThreadWithException(target=fact_rec, args=(n, ))
    th1.start()
    th2.start()

    for k in range(10):
        logging.debug("Tick {}".format(k))
        sleep(0)

    th1.join()
    th2.join()

    if th1.get_exception() is None:
        print("Потік 1 завершився успішно:", th1.get_result())
    else:
        print("Отримано виключення в потоці 1:", th1.get_exception())

    if th2.get_exception() is None:
        print("Потік 2 завершився успішно:", th2.get_result())
    else:
        print("Отримано виключення в потоці 2:", th2.get_exception())