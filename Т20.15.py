import numpy as np


def is_equilateral_triangle(tri):
    tri_shifted = np.roll(tri, 1, axis=2)
    dis = np.sqrt(np.sum((tri - tri_shifted)**2, axis=1))
    rot90 = np.rot90(dis)
    dis0 = np.full_like(rot90, rot90[0])
    b = np.isclose(rot90, dis0)
    res = np.all(b, axis=0)
    return res


def count_equilateral_triangles(pts):
    n = pts.shape[1]
    arrays = []
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                arrays.append(
                    pts[:, np.array((i, j, k))]
                )
    triplets = np.stack(arrays)
    result = is_equilateral_triangle(triplets)
    return np.sum(result)


if __name__ == "__main__":
    x = np.array([-1, 1, 0, 0])
    y = np.array([0, 0, np.sqrt(3), -np.sqrt(3)])
    points = np.vstack((x, y))
    print(count_equilateral_triangles(points))