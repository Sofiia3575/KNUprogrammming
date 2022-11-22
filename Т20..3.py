import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

a = -4 * np.pi
b = 4 * np.pi
m = 15

x = np.linspace(a, b, int((b - a) * 50))

fig = plt.figure()
plt.axis([a, b, -3 / 8 * (b - a), 3 / 8 * (b - a)])
line, = plt.plot([], [], "-b", lw=3)


def taylor_sin(x, n):
    s = x.copy()
    p = x.copy()
    for k in range(2, n + 1):
        p *= -x*x / ((2*k - 2)*(2*k - 1))
        s += p
    return s


def init():
    plt.plot(x, np.sin(x), "--r")
    return line,


def animate(i):
    y = taylor_sin(x, i + 1)
    line.set_data(x, y)
    return line,


if __name__ == "__main__":
    anim = FuncAnimation(
        fig,
        animate,
        init_func=init,
        frames=m,
        interval=2000,
        repeat=True
    )
    plt.show()
