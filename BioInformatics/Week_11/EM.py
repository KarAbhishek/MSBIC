import math


def distance(vec_1, vec_2):
    ls = 0
    for idx in range(len(vec_1)):
        ls += (vec_1[idx] - vec_2[idx]) ** 2
    return ls ** 0.5


def dot(vec_1, vec_2):
    suma = 0
    for i in range(len(vec_1)):
        suma += vec_1[i] * vec_2[i]
    return suma


def EM(data, num_of_centers, beta, centers=None):
    if centers is None:
        centers = data[:num_of_centers]
    hidden_matrix = []
    for center in centers:
        hidden_matrix.append([math.exp(-beta * distance(point, center)) for point in data])
    hidden_matrix_T = list(zip(*hidden_matrix))
    for col in range(len(hidden_matrix_T)):
        hidden_matrix_T[col] = [element / sum(hidden_matrix_T[col]) for element in hidden_matrix_T[col]]
    hidden_matrix = list(zip(*hidden_matrix_T))

    data_points = list(zip(*data))
    new_centers = []
    for center_idx in range(num_of_centers):
        new_centers.append(
            [dot(hidden_matrix[center_idx], col) / sum(hidden_matrix[center_idx]) for col in data_points])

    exit_now = has_convergence(centers, new_centers)
    if exit_now:
        return centers
    else:
        return EM(data, num_of_centers, beta, centers=new_centers)


def has_convergence(center_1, center_2):
    for idx in range(len(center_1)):
        if round(distance(center_1[idx], center_2[idx]), 3) == 0:
            return False
    return True


if __name__ == '__main__':
    file_ob = open('EM_data.txt')
    lines = file_ob.read().splitlines()

    k_out, _ = map(int, lines[0].split())
    beta_out = float(lines[1])
    print(k_out, beta_out)
    data_points_out = []
    for line in lines[2:]:
        data_points_out.append(tuple(map(float, line.split(' '))))
    print(data_points_out)

    centers_out = EM(data_points_out, k_out, beta_out)
    for center_out in centers_out:
        print(' '.join(map(str, center_out)))
