"""
Т17.14 Нехай результатом функції f є список деяких елементів. Побудувати
декоратор, який модифікує цей список так, щоб він не містив повторів.
Перевірити роботу декоратора для функції, яка повертає список слів, що
містяться у текстовому файлі.
"""

def Mydecorator(f):
    def _decorator(*args1, **args2):
        res = f(*args1, **args2)
        l = []
        l.append(res[0])
        for i in res[1::]:
            if i != l[-1]:
                l.append(i)
        return l
    return _decorator

@Mydecorator
def f(l):
    return(l)

l = 'abcddeeffggg'

print(f(l))