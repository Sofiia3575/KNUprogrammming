import numpy as np
import matplotlib.pyplot as plt


def seqa(n):
    s = 0
    z = 1
    for i in range(n):
        s += n / (3 ** i)
    return (s * (n - 3) * (n ** 1 / n) / (2 * n * n + 5))


def verify(e, a, b):
    c = abs(a - b) < e
    k = - 1
    for i in range(c.size):
        if c[i] == True:
            k = i
            break
    if k != -1:
        cc = c[k:c.size]
        if np.all(cc):
            print('sequence convergence, number of convergenced sequence is', k)
            return k
    else:
        print('sequence do not convergent')
        return -1


def movespinesticks():
    ax = plt.gca()
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))


if __name__ == '__main__':
    e = 0.01
    b = 0.75
    n = int(input('Кількість елементів: '))

    x = [seqa(i) for i in range(1, n)]
    nn = np.array([i for i in range(1, n)])
    a = np.array(x)

    k = verify(e, a, b)

    bb = np.ones(nn.size) * b
    movespinesticks()
    plt.plot(nn, a, '*b')
    plt.xlabel('n')
    plt.ylabel('a_n')
    plt.title('послідовність а_n')
    plt.plot(nn, bb, 'r')
    plt.plot(nn, bb - e, '--g')
    plt.plot(nn, bb + e, '--g')
    plt.show()