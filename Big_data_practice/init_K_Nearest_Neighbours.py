import operator

def calculate_eucleidian_distance(i, j):
    summation = 0
    for idx in range(len(j)):
        summation += (j[idx] - i[idx])**2
    return [summation ** 0.5]


def get_data_points():
    file = open('kNN_data')
    features = []
    labels = []
    lines = file.read().splitlines()
    for line in lines:
        splitter = line.split(' ')
        features.append((int(splitter[0]), int(splitter[1])))
        labels.append(int(splitter[2]))
    return features, labels

def extrapolate_label_for_current(all_dist, labels):
    all_dist.sort(key=operator.itemgetter(1))

def knn(k):
    ls, labels = get_data_points()
    error = 0
    for idx in range(len(ls)):
        i = ls[idx]
        true_label = labels[idx]
        all_dist = []
        for j_idx in range(len(ls)):
            j = ls[j_idx]
            j_label = labels[j_idx]
            all_dist.append(calculate_eucleidian_distance(i,j)+[j_label])
        all_dist.sort(key=operator.itemgetter(0))
        all_labels = ([w[2] for w in all_dist[:k]])
        predicted_label = sorted(all_labels, key=all_labels.count)[-1]

        print(predicted_label,true_label)
        error += abs(predicted_label-true_label)
    classification_error = error/len(ls)
    print(classification_error)

knn(5)
