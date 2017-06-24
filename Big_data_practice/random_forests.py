import random
from Big_data_practice.rf_Building_decision_tree import DecisionTree
import pickle


class RandomForests():
    def __init__(self, n=3):
        self.num_decision_tree = n
        self.train_set = None
        self.validate_set = None
        self.rand_feat_list = []

    # def create_decision_tree_train_and_validate_sets(self, full_set):
    #     train_set = []
    #     validate_set = []
    #     shuffler_limit = int(0.66 * len(full_set))  # 2/3rd train and 1/3rd validate
    #     feat_select = int(len(full_set[0])**0.5)
    #     print feat_select
    #     rand_samples = random.sample(range(len(full_set[0]) - 1), feat_select)
    #     for i in range(self.num_decision_tree):
    #         feat_sel = []
    #         for sample_lim_set in full_set[:shuffler_limit]:
    #             for feat_idx, feats_in_sample in enumerate(sample_lim_set):
    #                 if feat_idx in rand_samples:
    #                     feat_sel.append(feats_in_sample)
    #
    #             feat_sel.append(sample_lim_set[-1])
    #         train_set.append(feat_sel)
    #         # validate_set.append(full_set[shuffler_limit:])
    #         random.shuffle(full_set)
    #     return train_set, validate_set

    def create_decision_tree_train_and_validate_sets(self, full_set):
        train_set = []
        validate_set = []
        shuffler_limit = int(0.66 * len(full_set))  # 2/3rd train and 1/3rd validate
        num_feat = len(full_set[0])

        for i in range(self.num_decision_tree):
            num_sel_feats = 6  # int(num_feat ** 0.5)
            rand_feat_idxs = random.sample(range(num_feat - 1), num_sel_feats) + [len(full_set[0])-1]
            # import numpy as np
            # full_set_array = np.array(full_set)
            # sub_set = full_set_array[:, rand_feat_idxs].tolist()

            new_subset = []
            elem = []
            for i in full_set:
                for idx, j in enumerate(i):
                    if idx in rand_feat_idxs:
                        # try:
                        #     elem.append(int(j))
                        # except ValueError:
                        elem.append(j)
                new_subset.append(elem)
                elem = []


            train_set.append(new_subset[:shuffler_limit])
            validate_set.append(new_subset[shuffler_limit:])
            random.shuffle(full_set)
            self.rand_feat_list.append(rand_feat_idxs)
        return train_set, validate_set#, rand_feat_idxs

    def get_train_data(self, location='data/train.csv'):
        fil = open(location)
        lines = fil.read().splitlines()
        return_var = []

        for line in lines[1:]:
            line_split = line.split(',')

            def data_spec(x, dtype=[float, float, str, str, str, float, float, float, str, float, str, str]):
                bag = []
                for s_idx, s_dtype in enumerate(dtype):
                    try:
                        if s_dtype == float and x[s_idx] == '':
                            m =28 if s_idx==5 else 0
                            bag.append(s_dtype(m))
                        elif s_dtype == str:
                            bag.append(s_dtype(x[s_idx]).replace('"',''))
                        else:
                            bag.append(s_dtype(x[s_idx]))
                    except:
                        print()
                return bag


                # return ret

            return_var.append(list(data_spec(line_split[:-1])) + [line_split[-1]])
        # self.create_decision_tree_train_and_validate_sets(return_var)
        # print return_var
        return return_var

    # def dummy_code(self, lis):
    #     new_lis = []
    #     ref_hm = {idx: i for idx, i in enumerate(list(set(lis)))}
    #     for i in lis:
    #         new_lis.append(ref_hm[i])
    #     return new_lis

    def fit(self):
        ensemble = []
        td = self.get_train_data()
        train_set, validate_set = self.create_decision_tree_train_and_validate_sets(td)
        for i in range(self.num_decision_tree):
            dt = DecisionTree()
            tree = dt.build_tree(train_set[i])

            # print('Cross Validating just Tree ', i)
            # ignor1, ignor2, res = dt.cross_validation(train_set[i])
            # print(res)
            tree_model_file = open('rf_model_tree_'+str(i+1), 'wb+')
            pickle.dump(tree, tree_model_file)
            tree_model_file.close()
            ensemble.append(tree)

        ensemble_model_file = open('rf_model', 'wb+')
        pickle.dump(ensemble, ensemble_model_file)
        ensemble_model_file.close()

        return ensemble

    def predict(self, ensemble, test_data):
        rf_prediction = []
        dt_predictions = []

        for tree_idx, single_tree in enumerate(ensemble):
            new_subset = []

            for i in test_data:
                elem = []
                for idx, j in enumerate(i):
                    if idx in self.rand_feat_list[tree_idx]:
                        # try:
                        #     elem.append(int(j))
                        # except ValueError:
                        elem.append(j)
                new_subset.append(elem)
            dt_predictions.append([i[0] for i in map(list, DecisionTree().predict(new_subset, single_tree))])
        turn_predictions = zip(*dt_predictions)

        for single_prediction_row in turn_predictions:
            # Calculate Mode #
            # data = Counter(single_prediction_row)
            # rf_prediction.append(data.most_common(1)[0][0])  # Majority Vote
            rf_prediction.append(max(set(single_prediction_row), key=single_prediction_row.count))
        return rf_prediction

    def accuracy(self, prdict_label, true_label):
        correct = 0
        for i in range(len(true_label)):
            if prdict_label[i] == true_label[i]:
                correct += 1
        return correct/float(len(true_label))


rf = RandomForests(10)
e = rf.fit()
test_data = rf.get_train_data('data/test_new.csv')
prediction = rf.predict(e, test_data)
print(rf.accuracy(prediction, [i[-1] for i in test_data]))
# print prediction
