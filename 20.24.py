import numpy as np
import random

TEST_NUM = 10000
m = random.randint(2, 10)
colors = np.arange(m)
k = random.randint(2, 10)
d = random.randint(2, k)


def check(choice):
    res = np.zeros(TEST_NUM, dtype=bool)
    for i in range(TEST_NUM):
        if np.all(choice[i] == choice[i][0]):
            print(choice[i])
            res[i] = True
    return res


def beads_probability(beads, count):
    choice = np.zeros((TEST_NUM, count), dtype=int)
    for i in range(TEST_NUM):
        choice[i, :] = np.random.choice(beads, count, replace=False)
    choice.sort(axis=1) 
    print(choice)
    res = check(choice)
    return np.sum(res) / TEST_NUM


if __name__ == "__main__":
    hat = np.random.choice(colors, m * k)
    p = beads_probability(hat, d)
    print(f"{p * 100:.2f}%")
    print(f"Загальна кількість куль: {m * k}")
    print(f"Кількість кольорів: {m}")
    print(f"Кількість кульок одного кольру: {k}")
    print(f"Масив кольорів: {colors}")
    print(f"Кількість кульок, яку витягли за один раз: {d}")
