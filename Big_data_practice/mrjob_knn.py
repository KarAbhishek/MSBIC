from mrjob.step import MRStep
from mrjob.job import MRJob
import operator


class MRJobKNN(MRJob):
    def configure_options(self):
        super(MRJobKNN, self).configure_options()
        self.add_passthrough_option('--k', help='Enter the number of neighbors to consider')
        self.add_file_option('--test', help='Path to the test data location')

    def steps(self):
        return [MRStep(mapper=self.mapper_step_1,
                       reducer=self.reducer_step_1),
                MRStep(reducer=self.reducer_step_2)]

    def natural_type(self, x):
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

    def get_data_points(self, file):
        # file = open(file_name)
        features = []
        labels = []
        lines = file.read().splitlines()
        for line in lines[1:]:
            splitter = line.split(',')
            features.append(list(map(self.natural_type, splitter[:-1])))
            labels.append(self.natural_type(splitter[-1]))
        return features, labels

    def calculate_eucleidian_distance(self, i, j):
        summation = 0
        for idx in range(len(j)):
            try:
                summation += (j[idx] - i[idx]) ** 2
            except:
                if type(j[idx]) != str and type(i[idx]) != str:
                    print('problem')
                    # print()
        return [summation ** 0.5]

    def mapper_step_1(self, _, line):
        # get test file
        file_obj = open(self.options.test)
        test_data, test_labels = self.get_data_points(file_obj)
        for j_idx in range(len(test_data)):
            true_label = test_labels[j_idx]

            j = test_data[j_idx]
            train_sample = list(map(self.natural_type, line.split(',')))
            yield (j_idx, true_label), self.calculate_eucleidian_distance(train_sample, j) + [line]

    def reducer_step_1(self, key, value):
        value = list(value)
        value.sort(key=operator.itemgetter(0))
        all_labels = ([w[1] for w in value[:int(self.options.k)]])
        predicted_label = int(sorted(all_labels, key=all_labels.count)[-1][-1])
        true_label = key[1]
        yield 1, (predicted_label, true_label)
        print(key, predicted_label, true_label)

    def reducer_step_2(self, _, predicted_list):
        error = 0
        predicted_list = list(predicted_list)
        for key in predicted_list:
            # print(abs(key[0] == key[1]))
            error += abs(key[0] == key[1])
            print(key[0], key[1])

        # print(error, float(len(predicted_list)))
        classification_error = error / float(len(predicted_list))
        print(classification_error)


if __name__ == '__main__':
    # sys.argv.append('data/train_new.csv')
    # sys.argv.append('--test')
    # sys.argv.append('data/test_new.csv')
    # file=open('data/train.csv')
    # print(file.read())
    # file.close()
    # print('N = ' + sys.argv[1])
    # print(sys.argv[1]
    MRJobKNN.run()
