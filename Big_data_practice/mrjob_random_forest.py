from mrjob.job import MRJob
import sys
from Big_data_practice.rf_Building_decision_tree import DecisionTree
import random
from mrjob.step import MRStep


class MRJobRandomForest(MRJob):

    def configure_options(self):
        super(MRJobRandomForest, self).configure_options()
        self.add_file_option('--items', help='Path to the data location')  # waits for --items followed by data
        self.add_file_option('--item1')
        #self.add_passthrough_option('--item1')
        #print(self.options.item1



    def steps(self):
        return [MRStep(mapper=self.mapper_step_1,
                        reducer=self.reducer_step_1),
                MRStep(reducer=self.reducer_step_2)]

    # def mapper_init(self):
    def mapper_step_1(self, _, line):
        #print(self.options.item1
        file_obj = open(self.options.items)
        # file_obj1 = open(self.options.item1)
        # print(file_obj1)
        lines = file_obj.read().split('\n')[:-1] # +file_obj1.read().split('\n')[1:-1]
        train = []
        test = []

        def natural_type(x):
            x = x.replace(',', '')
            try:
                ret = int(x)
            except ValueError:
                ret = x

            return ret

        # Feature Naming
        hm = lines[0].split(';')



        # Preprocess Data into 80% Train Data
        # Train Data
        total_samples = int(0.8 * len(lines))
        for line in lines[1:total_samples+2]:
            line_split = line.split(';')

            train.append(list(map(natural_type, line_split[:-1])) + [line_split[-1]])

        random.shuffle(train)

        # Test Data
        for line in lines[total_samples+2:]:
            line_split = line.split(';')

            test.append(list(map(natural_type, line_split[:-1])) + [line_split[-1]])

        # Taking 2/3 samples randomly and take a subset of the features

        shuffler_limit = int(0.66 * len(train))  # 2/3rd train and 1/3rd validate
        num_feat = len(train[0])
        num_sel_feats = 6  # int(num_feat ** 0.5)
        rand_feat_idxs = random.sample(range(num_feat - 1), num_sel_feats) + [num_feat - 1]

        random.shuffle(train)
        new_subset = []
        elem = []
        for i in train:
            for idx, j in enumerate(i):
                if idx in rand_feat_idxs:
                    try:
                        elem.append(int(j))
                    except ValueError:
                        elem.append(j)
            new_subset.append(elem)
            elem = []

        train_subset = new_subset[:shuffler_limit]

        dt = DecisionTree()
        tree = dt.build_tree(train_subset)
        test_subset = []
        naming_subset = []
        for idx_i, i in enumerate(test[:-1]):
            elem = []
            for idx, j in enumerate(i):
                if idx in rand_feat_idxs:
                    try:
                        elem.append(int(j))
                    except ValueError:
                        elem.append(j)
            naming_subset.append(hm[idx])

            prediction = list(dt.predict([elem], tree)[0])[0]
            true_label = i[-1]
            yield (idx_i, true_label), prediction
            # print('These here: ' + str(test[:-1]))
            #test_subset.append(elem)
        #print(tree

        #print(dt.print_tree(tree, hm=hm)
        #test = line.split(';')
        #test = list(map(natural_type, test))
        #yield 1, list(dt.predict([test], tree)[0])

    # def mapper(self, _, line):
    #     print(line
    #     print(_
    #     yield "chars", len(line)
    #     yield "words", len(line.split())
    #     yield "lines", 1

    def reducer_step_1(self, test_sample, predictions):
        predictions = list(predictions)
        # print(predictions
        # print('These here: '+str(test_sample))
        yield 1, (test_sample[1], max(set(predictions), key=predictions.count))


    def reducer_step_2(self, key, true_and_rf_prediction):
        df = DecisionTree()
        print(true_and_rf_prediction)
        true_tuple, predict_tuple = zip(*true_and_rf_prediction)
        print('tre' + str(true_tuple) + 'pred' + str(predict_tuple))
        confusion_mat, accuracy = df.confusion_matrix(true_tuple, predict_tuple)
        #file_1 = open('accuracy.txt', mode='w+')
        accuracy_str = 'The Accuracy is at ' + str(
            accuracy * 100) + '% for the Test Data.\n'+'This is what the Confusion Matrix looks like \n' + '\n'.join(
            [str(i) for i in confusion_mat])
        file_acc = open('accuracy_file.txt', 'w+')
        file_acc.write(accuracy_str)
        yield 1, accuracy_str
        yield 1, 1



if __name__ == '__main__':
    #sys.argv.append('--items')
    #sys.argv.append('/home/abhishek/PycharmProjects/MSBIC/data/minitest.csv')
    file_ob = open('placeholder_file.txt', 'w+')
    file_ob.write('\n'.join(map(str, range(int(sys.argv[1])))))
    file_ob.close()
    print('N = '+sys.argv[1])
    sys.argv[1] = 'placeholder_file.txt'
    #print(sys.argv[1]
    MRJobRandomForest.run()