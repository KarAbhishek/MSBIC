def distortion(data_points, centers):
    ls = []
    for data_point in data_points:
        ls.append(distance(data_point, centers))
    return sum(ls)/len(ls)



def distance(data_point, centers):
    suma_list = []
    for center in centers:
        suma = 0
        for idx in range(len(center)):
            suma += (center[idx] - data_point[idx])**2
        suma_list.append(suma)
    return min(suma_list)


if __name__ == '__main__':
    file = open('distor.txt')
    lines = file.read().splitlines()
    k_out, m = tuple(map(int, lines[0].split(' ')))
    print(k_out, m)
    centers_out = []
    indices = 1
    while lines[indices][0] != '-':
        line = lines[indices]
        centers_out.append(tuple(map(float, line.split(' '))))
        indices += 1
    print(centers_out)
    data_points_out = []
    for line in lines[indices+1:]:
        data_points_out.append(tuple(map(float, line.split())))
    print(data_points_out)
    print(distortion(data_points_out, centers_out))