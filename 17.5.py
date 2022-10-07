"""
Т17.5 Побудувати декоратор, який перевіряє, чи належать усі параметри
декорованої функції заданому типу (ім’я цього типу є параметром
декоратора). Якщо ні, то ініціює виключення. Виконати перевірку роботи
декоратора для функції, яка обчислює середнє значення декількох числових
змінних.
"""
def decorator(n=float):
    def _decorator(f):
        def __decorator(*args, **kwargs):
            for x in args:
                if type(x) != n:
                    raise TypeError('Задані параметри іншого типу')
            for y in kwargs.values():
                if type(y) != n:
                    raise TypeError('Задані параметри іншого типу')
            res = f(*args, **kwargs)
            return res
        return __decorator
    return _decorator


@decorator(float)
def function(*args, **kwargs):
    n = len(args) + len(kwargs)
    s = 0
    for x in args:
        s += x
    for y in kwargs.values():
        s += y
    return f"Середнє значення: {s/n}"

if name == "__main__":
    print(function(4.0, 7.0, y1=8.0, x1=3.0))