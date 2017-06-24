from operator import itemgetter


def distance(point1, point2):
    return (point1**2 - point2**2)**0.5


def k_closest_points(k, center, data_points):
    ls = []
    for data_point in data_points:
        ls.append([data_point, center, distance(data_point, center)])
    ls.sort(key=itemgetter(2))
    return ls[:k]

k_closest_points(k, center, data_points)