import numpy as np

def orthonormal_v1(x):
    for i in range(x.shape[0]):
        for j in range(i, x.shape[0]):
            prod = np.dot(x[i], x[j])
            if i == j:
                if not np.isclose(prod, 1):
                    return False
            else:
                if not np.isclose(prod, 0):
                    return False
    return True


def orthonormal_v2(x):
    y = np.dot(x, x.T)
    eye = np.eye(x.shape[0])
    return np.all(np.isclose(y, eye))


if __name__ == "__main__":
    x = np.eye(3)
    print(x)
    print(orthonormal_v1(x))
    print(orthonormal_v2(x))

    x = np.array(
        [
            [np.sqrt(2) / 2, np.sqrt(2) / 2, 0],
            [0, 0, 1],
            [np.sqrt(2) / 2, -np.sqrt(2) / 2, 0]
        ]
    )
    print(x)
    print(orthonormal_v1(x))
    print(orthonormal_v2(x))

    x = np.random.randn(3, 3)
    print(x)
    print(orthonormal_v1(x))
    print(orthonormal_v2(x))