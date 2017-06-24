import numpy as np


class TreeStructure:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

    def set_left(self, left_val):
        self.left = left_val

    def set_right(self, right_val):
        self.right = right_val

class DataUtil:
    def get_train_data(self):
        XTrain = np.genfromtxt('data/train.csv', delimiter=',', dtype=np.str)
        yTrain = XTrain[:, -1].reshape(XTrain.shape[0], 1)
        XTrain = np.array(XTrain[:, :-1], dtype=np.float)
        return XTrain, yTrain


    def get_test_data(self):
        XTest = np.genfromtxt('data/test.csv', delimiter=',', dtype=np.str)
        yTest = XTest[:, -1].reshape(XTest.shape[0], 1)
        XTest = np.array(XTest[:, :-1], dtype=np.float)
        return XTest, yTest

class CalcUtil:
    def calc_entropy(self, prob_list):
        list_of_single_entropies = [-prob*np.log2(prob) for prob in prob_list]
        return np.sum(list_of_single_entropies)


    def get_entropy_of_set(self, curr_array, labels):
        label_set = set(labels)
        for i in label_set:
            if i in curr_array:
                print i


def decision_tree():
    Xtrain, yTrain = DataUtil.get_train_data()

    root_node = TreeStructure(Xtrain)
    calc_entropy(root_node.subset())
