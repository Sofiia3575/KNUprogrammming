"""
Т19.6 Описати декоратор класу, який здійснює модифікацію класу з метою
трасування виклику усіх власних (не спеціальних) методів класу. Під час
трасування показувати ім’я методу, значення параметрів до виклику, а також
результат після виклику. Застосувати цей декоратор до класів Person та
Student (див. тему «Класи та об’єкти») та виконати програму обчислення
стипендії студентам.
"""

def trace(f):
    depth = 0

    def _trace(*args, **kwargs):
        nonlocal depth
        depth += 1
        print("Входимо у функцію {}".format(f.__name__), end="; ")
        print("глибина: {}".format(depth), end="; ")
        print("позиційні параметри: {}".format(args), end="; ")
        print("ключові параметри: {}".format(kwargs))
        res = f(*args, **kwargs)
        print("Вихід з функції: {}".format(f.__name__), end="; ")
        print("глибина: {}".format(depth), end="; ")
        print("результат: {}".format(res))
        depth -= 1
        return res
    return _trace


def trace_class(cls):
    for name, attr in cls.__dict__.items():
        if not name.startswith("__") and callable(attr):
            setattr(cls, name, trace(attr))
    return cls


@trace_class
class SimpleClass:

    def __init__(self):
        pass

    def f(self, *args, **kwargs):
        if kwargs:
            self.f(*args)

    def g(self):
        return 1


if __name__ == '__main__':
    s = SimpleClass()
    s.f(1, 2, y=1)
    s.f(1)
    s.g()