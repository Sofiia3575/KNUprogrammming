"""
Т17.2 Побудувати декоратор, який коригує результат функції, що повертає
число, так, щоб цей результат x був у межах заданих границь a, b (a <= x <= b).
Виконати перевірку роботи декоратора для деякої функції f.
"""

def ininterval(a,b):
	def _mydecorator(function):
		def __mydecorator(*args, **kw):
			# виконати дії перед викликом реальної ункції
			res = function(*args, **kw)
			# виконати дії після виклику функції
			if res<a or res>b:
				res = (a+b)/2

			return res
		# повренути підфункцію
		return __mydecorator
	return _mydecorator


@makegreaterzero
def f(x):
	return 2*x - 1

@makegreaterzero
def f1(x,y):
	return -1



@ininterval(0,1)
def f3(x):
	return 2*x - 1

@ininterval(0,2)
def f4(x,y):
	return -1


class ExceptNonEqual(Exception):

	def __init__(self):
		super()

	def __str__(self):
		return "Non Equal sizes!!!"