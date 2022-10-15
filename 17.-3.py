"""
Т17.3 Побудувати декоратор, який перевіряє, чи дорівнює кількість
позиційних параметрів кількості ключових параметрів функції, що
декорується. Якщо не дорівнює, то ініціює виключення. За допомогою
декоратора розв’язати задачу: скласти підпрограму зі змінною кількістю
параметрів для обчислення функції...
"""

def key_value_equal_sizes(fun):

	def _key_value_equal_sizes(*args,**kwargs):

		if len(args) != len(kwargs):
			raise ExceptNonEqual
		res = fun(*args, **kwargs)
		return res
	return _key_value_equal_sizes


@key_value_equal_sizes
def func1(*args, **kwargs):
	p = 1
	for x,y in zip(args,kwargs.values()):
		if y==0:
			continue
		p *= (x + 1/ y)

	return p


if __name__ == '__main__':
	print("{}".format(f(2)))
	print("{}".format(f(-3)))
	print("{}".format(f1(1,4)))

	print("{}".format(f3(1)))
	print("{}".format(f3(-3)))
	print("{}".format(f4(1,4)))


	a1 = func1(1,2,3,y1=1,y2=2,y3=3)
	print("a=",a1)

	try:
		a1 = func1(1,2,3,y1=1,y2=2)
		print("a=",a1)
	except ExceptNonEqual as e:
		print("Caught exception: ", e)