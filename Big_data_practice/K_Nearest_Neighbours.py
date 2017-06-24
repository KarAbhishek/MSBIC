import operator


def calculate_eucleidian_distance(i, j):
    summation = 0
    for idx in range(len(j)):
        try:
            summation += (j[idx] - i[idx])**2
        except:
            if type(j[idx]) != str and type(i[idx]) != str:
                print('problem')
            #print()
    return [summation ** 0.5]


def natural_type(x):
    try:
        x = int(x)
    except ValueError:
        try:
            x = float(x)
        except ValueError:
            if x != '':
                if x[0] == '"':
                    x = x.replace('"', '')
                elif x[-1] == '"':
                    x = 'placeholder'
    return x


def get_data_points(file_name='data/train.csv'):
    file = open(file_name)
    features = []
    labels = []
    lines = file.read().splitlines()
    for line in lines[1:]:
        splitter = line.split(',')
        features.append(list(map(natural_type, splitter[:-1])))
        labels.append(natural_type(splitter[-1]))
    return features, labels


def get_test_data_points(file_name):
    file = open(file_name)
    features = []
    labels = []
    lines = file.read().splitlines()
    for line in lines[1:]:
        splitter = line.split(',')
        features.append(list(map(natural_type, splitter)))
    return features


def knn(k):
    train_data, train_labels = get_data_points()
    test_data, test_labels = get_data_points('data/test_new.csv')

    # test_labels = get_test_data_points('data/iris_test_label.csv')
    error = 0

    all_dist = {}

    for idx in range(len(train_data)):
        i = train_data[idx]
        train_label = train_labels[idx]

        for j_idx in range(len(test_data)):
            true_label = test_labels[j_idx]

            j = test_data[j_idx]
            if (j_idx, true_label) not in all_dist:
                all_dist[(j_idx, true_label)] = []
            all_dist[(j_idx, true_label)].append(calculate_eucleidian_distance(i, j)+[train_label])

    predicted_list = []

    for key in all_dist:
        all_dist[key].sort(key=operator.itemgetter(0))
        all_labels = ([w[1] for w in all_dist[key][:k]])
        predicted_label = sorted(all_labels, key=all_labels.count)[-1]
        true_label = key[1]
        predicted_list.append((predicted_label, true_label))

    for key in predicted_list:
        error += abs(key[0] == key[1])
        print(key[0], key[1])

    classification_error = error/float(len(test_data))
    print(classification_error)

knn(5)
