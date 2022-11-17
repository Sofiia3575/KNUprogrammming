import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def f01(x, n):
    s = 1
    p = 1
    for k in range(2, n + 1):
        p *= -x
        s += p
    return s

a = -10
b = 10

x = np.linspace(a, b, int((b - a) * 100))
fig = plt.figure()
plt.axis([a, b, -3/8 * (b-a), 3/8 * (b-a)])
plt.plot(x, 1/(1+x), "--r", lw =4)
line, = plt.plot([], [], "yellow", lw=2)


def animate(i):
    y = f01(x, i + 1)
    line.set_data(x, y)
    return line,

anim = FuncAnimation(
    fig, animate,
    frames=20,
    interval=500,
    repeat=False
)
plt.show()
