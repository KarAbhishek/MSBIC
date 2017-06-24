import numpy as np
from copy import deepcopy


# Referred a 10-601 homework i did for lloyd iteration
def distance_numpy(elem1, elem2):
    return np.sum(np.square(elem1 - elem2))
    # idx = np.argmin(distance_list)
    # return elem1[idx], elem2[idx]


def update_assignments(X, C):
    a = np.zeros(X.shape[0])
    # for i in X.shape[0]:
    #     z = np.sum(np.square(X[i, :] - C[i, ?]))
    #     a[i] = C[np.argmin(z)]

    # for c_idx in range(C.shape[0]):
    #     dist_list = distance_numpy(X[c_idx, :], C[c_idx])
    #     _, a[c_idx] = argmin_distance(C, dist_list)
    # return a

    # ret = []
    # dist_list = []
    for single_point_idx in range(X.shape[0]):
        min_dist = float('inf')
        min_arg = None
        single_point = X[single_point_idx]
        for center_idx in range(C.shape[0]):
            center = C[center_idx]
            dist = distance_numpy(single_point, center)
            if dist < min_dist:
                min_dist = dist
                min_arg = center_idx
        a[single_point_idx] = min_arg
        #_, a[center_idx] = argmin_distance(_, dist_list)
    return a

    # for i in range(N):
        # Find the j which minimizes distnace between x[i] and Cj

    # for i in range(X.shape[0]):
    #     a[i] = distance(X[i, :], C)
    # return a


def update_centers(X, C, a):
    # for i in X.shape[0]:
    #     c = np.sum(np.square(X[i, :] - C[?, i]))
    #     C[i] = C[np.argmin(c)]

    # for c_idx in range(C.shape[0]):
    #     dist_list = distance_numpy(X[c_idx, :], C[c_idx])
    #     _, C[c_idx] = argmin_distance(a, dist_list)
    for i in range(C.shape[0]):
        indices = np.where(a == i)
        C[i] = np.mean(X[indices], axis=0)
    return C


def lloyd_iteration(X, C):
    a = np.zeros(X.shape[0])
    while True:
        bkp_a = deepcopy(a)
        a = update_assignments(X, C)
        C = update_centers(X, C, a)
        if all(a == bkp_a):
            break
        # updatea
        # updatec
    return C, a

if __name__ == '__main__':
    from trial_lloyd import read_input
    print(lloyd_iteration(zip(*read_input())))
