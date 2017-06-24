def farthest_first(data_points, k):
    x = data_points[0]
    del data_points[0]
    centers = [x]
    while len(centers) < k:
        ret, id = maximizer(data_points, centers)
        centers.append(ret)
        del data_points[id]
    return centers


def maximizer(data_points, centers):
    best_d = float('-inf')
    for idx, data_point in enumerate(data_points):
        d = distance(data_point, centers)
        if d > best_d:
            best_d = d
            best_point = data_point
            best_point_idx = idx
    return best_point, best_point_idx


def distance(data_point, centers):
    suma_list = []
    for center in centers:
        suma = 0
        for idx in range(len(center)):
            suma += (center[idx] - data_point[idx])**2
        suma_list.append(suma)
    return min(suma_list)


if __name__ == '__main__':
    file = open('farthest.txt')
    lines = file.read().splitlines()
    k_out, m = tuple(map(int, lines[0].split(' ')))
    data_points_out = []
    for line in lines[1:]:
        data_points_out.append(tuple(map(float, line.split(' '))))
    print('\n'.join(' '.join(farthest_first(data_points_out, k_out))))