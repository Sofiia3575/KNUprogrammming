import numpy as np
from math import sin
from math import pi
import matplotlib.pyplot as plt


def function(f, x):
    try:
        y = f(x)
    except Exception as e:
        print('Exception handling', e)
        n = x.size
        y = np.zeros(n)
        for i in range(n):
            y[i] = f(x[i])
    return y


def lagrange(f, a, b, n):
    xk = np.linspace(a, b, n)
    yk = function(f, xk)

    def _lagrange(x):
        P = np.zeros(n)
        lk = np.ones(n)
        for k in range(n):
            lk.fill(1)
            for i in range(n):
                if i != k:
                    lk *= (x - xk[i]) / (xk[k] - xk[i])
            P += yk[k] * lk
        return P

    return _lagrange


if name == "__main__":
    n = np.linspace(0, 2 * pi, 1000)
    q = []
    m = 2
    while len(n) - m > 0:
        m *= 2
        q.append(m + 1)
    n1 = n[q[:len(q) - 1]]
    plt.plot(n, function(sin, n), "b")
    plt.axis([0, 2 * pi, -1.1, 1.1])
    plt.plot(n1, lagrange(sin, 0, 2 * pi, len(n1))(n1), "r")
    plt.show()
