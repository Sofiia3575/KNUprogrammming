import numpy as np
def matrix(x):
    magic_matrix = True
    for i in range(x.shape[1]):
        if np.sum(x[:i]) != np.sum(x[:1]) or np.sum(x[:i]) != np.sum(x[:1]):
            magic_matrix = False
            break
        else:
            pass
    return magic_matrix
if __name__ == '__main__':
    print(matrix(np.array([[5,5,5],[5,5,5],[5,5,5]])))
    print(matrix(np.array([[5,5,5],[5,8,5],[6,5,5]])))
