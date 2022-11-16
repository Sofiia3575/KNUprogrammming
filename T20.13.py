import numpy as np

def inputPoints():
    n = int(input("n="))
    ar = []
    for _ in range(n):
        x = float(input("x="))
        y = float(input("x="))
        ar.append((x,y))
    return ar

def dist(i,j):
    global x, y

    return (x[i]-x[j])**2 + (y[i] - y[j])**2


if __name__ == '__main__':
    pts = inputPoints()

    x = np.array([it[0] for it in ar])
    y = np.array([it[1] for it in ar])

    for x1, y1 in zip(x, y):
        for x2, y2 in zip(x, y):
            z = np.sqrt((x1-x2)**2 + (y1-y2)**2)

    zs = np.array()
    xs = np.array()
    ys = np.array()
    mas = np.array(n*n*3)
    mas.reshape(3, n*n)

    for i in range(x.size()):
        z = np.sqrt((x-x[i])**2 + (y-y[i])**2)
        zs = np.vstack(zs, z)
        x_ = np.arrange(x.size())
        y_ = np.ones(x.size()) * i
        xs = np.vstack(xs, x_)
        ys = np.vstack(ys, y_)
    mas[0, :] = xs
    mas[1, :] = ys
    mas[2, :] = zs

    m = np.max(mas, axis=2)
    ind = np.argmax(mas, axis=2)

    print("Max = ({}{}) = {}".format(ind[0], ind[1], m))


