"""
Т17.1 Побудувати декоратор, який коригує результат функції, що повертає
число, так, щоб цей результат завжди був більше 0. Виконати перевірку
роботи декоратора для деякої функції f.
"""

def makegreaterzero(function):
	def _mydecorator(*args, **kw):
		# виконати дії перед викликом реальної ункції
		res = function(*args, **kw)
		# виконати дії після виклику функції
		if res<0:
			res = -res
		elif res==0:
			res = 1

		return res
	# повренути підфункцію
	return _mydecorator


@makegreaterzero
def f(x):
	return 2*x - 1

@makegreaterzero
def f1(x,y):
	return -1
