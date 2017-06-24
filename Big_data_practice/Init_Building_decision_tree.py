import numpy as np


class TreeStructure():
    def __init__(self, col=-1, value=None, results=None, left=None, right=None, nos=None):
        self.col = col
        self.value = value
        self.results = results
        self.left = left
        self.right = right
        self.nos = nos


class DataUtils():
    def __init__(self):
        return

    def get_test_data(self):
        file = open('data/test.csv')
        lines = file.read().splitlines()
        return_var = []
        for line in lines:
            line_split = line.split(',')
            return_var.append(list(map(float, line_split[:-1])) + [line_split[-1]])
        return return_var

    def get_train_data(self):
        file = open('data/train.csv')
        lines = file.read().splitlines()
        return_var = []
        for line in lines:
            line_split = line.split(',')
            return_var.append(list(map(float, line_split[:-1])) + [line_split[-1]])
        return return_var


class DecisionTree():
    def split_func(self, row, column, value):
        if type(value) is int or type(value) is float:
            return row[column] >= value
        else:
            return row[column] == value

    def split_sets(self, rows, column, threshold):
        part_uno = []
        part_dos = []
        for row in rows:
            if self.split_func(row, column, threshold):
                part_uno.append(row)
            else:
                part_dos.append(row)
        return part_uno, part_dos

    def calc_entropy(self, rows):
        from math import log
        results = self.freq_dict(rows)
        list_of_single_entropies = [-results[count] / float(len(rows)) * log(results[count] / float(len(rows)), 2) for
                                    count
                                    in results]
        return sum(list_of_single_entropies)

    def freq_dict(self, rows):
        hm = {}
        for row in rows:
            label = row[-1]
            if label in hm:
                hm[label] += 1
            else:
                hm[label] = 1
        return hm

    def information_gain(self, current_score, part_uno, part_dos, probability):
        return current_score - probability * self.calc_entropy(part_uno) - (1 - probability) * self.calc_entropy(
            part_dos)

    def build_tree(self, rows):

        if len(rows) == 0:
            return TreeStructure()
        current_score = self.calc_entropy(rows)

        best_gain = 0.0
        best_criteria = None
        best_sets = None

        column_count = len(rows[0]) - 1
        for col_idx in range(column_count):
            column_values = set()
            for row in rows:
                column_values.add(row[col_idx])
            for value in column_values:
                (part_uno, part_dos) = self.split_sets(rows, col_idx, value)
                p = float(len(part_uno)) / len(rows)
                gain = self.information_gain(current_score, part_uno, part_dos, p)
                if gain > best_gain and len(part_uno) > 0 and len(part_dos) > 0:
                    best_gain = gain
                    best_criteria = (col_idx, value)
                    best_sets = (part_uno, part_dos)

        # Create the sub branches
        if best_gain > 0:
            true_branch = self.build_tree(best_sets[0])
            false_branch = self.build_tree(best_sets[1])
            return TreeStructure(col=best_criteria[0], value=best_criteria[1],
                                 left=true_branch, right=false_branch, nos=(len(best_sets[0]), len(best_sets[1])))
        else:
            return TreeStructure(results=self.freq_dict(rows))

    def print_tree(self, tree, indent=''):
        string = ''
        hm = {0: 'Sepal Length', 1: 'Sepal Width', 2: 'Petal Length', 3: 'Petal Width'}
        if tree.results != None:
            string += (tree.results.keys()[0] + '\n')
        else:
            string += (
                hm[tree.col] + ':' + str(tree.value) + '? ' + str(tree.nos).replace('(', '[').replace(',',
                                                                                                      '+,').replace(
                    ')', '-]') + ' .' + str(tree.nos[0] / float(sum(tree.nos))) + '+  .' + str(
                    tree.nos[1] / float(sum(tree.nos))) + '-  \n')
            # string += the branches
            string += (indent + 'True :->')
            string += self.print_tree(tree.left, indent + '|  ')
            string += (indent + 'False :->')
            string += self.print_tree(tree.right, indent + '|  ')
        return string

    def classify(self, observation, tree):
        if tree.results != None:
            return tree.results
        else:
            v = observation[tree.col]
            branch = None
            if type(v) is int or type(v) is float:
                if tree.value <= v:
                    branch = tree.left
                else:
                    branch = tree.right
            else:
                if v == tree.value:
                    branch = tree.left
                else:
                    branch = tree.right
        return self.classify(observation, branch)

    def confusion_matrix(self, predicted_label, true_label):
        pred_list = [i[0] for i in map(list, predicted_label)]
        true_list = [single for single in true_label]
        complete_node_list = list(set(pred_list + true_list))
        hm = {i: idx for idx, i in enumerate(complete_node_list)}
        conf_mat = [[0 for x in range(len(complete_node_list))] for y in range(len(complete_node_list))]
        for idx, true_label_at_idx in enumerate(true_list):
            conf_mat[hm[true_label_at_idx]][hm[pred_list[idx]]] += 1
        import numpy as np

        correct = 0
        for i in range(len(conf_mat)):
            correct += conf_mat[i][i]
        accuracy = correct / float(len(true_list))
        return conf_mat, accuracy

    def predict(self, test_data, tree):
        predicted_labels = []
        for test_data_single in test_data:
            predicted_labels.append(self.classify(test_data_single, tree))
        return predicted_labels

    def split_into_train_and_validate(self, train_data, k=10):
        total_length = len(train_data)
        length_of_each_fold = total_length / k
        ls = []
        for start in range(len(train_data) - length_of_each_fold + 1)[::length_of_each_fold]:
            test_fold = train_data[start: start + length_of_each_fold]
            train_fold = train_data[:start] + train_data[start + length_of_each_fold:]
            ls.append([train_fold, test_fold])
        return ls

    def cross_validation(self, train_data):
        cross_validation_results = (
            '**************************************Cross Validation Begins**************************************' + '\n')
        splitted = self.split_into_train_and_validate(train_data)
        sum_accuracy = 0
        std_list = []
        for train_fold, validate_fold in splitted:
            split_tree = self.build_tree(train_fold)
            predicted_validate_split = self.predict(validate_fold, split_tree)
            ignor, v_accuracy = self.confusion_matrix(predicted_validate_split,
                                                      [i[-1] for i in validate_fold])
            sum_accuracy += v_accuracy
            std_list.append(v_accuracy)

        mean_accuracy = sum_accuracy / len(splitted)
        mean_error = 1 - mean_accuracy
        std_accuracy = np.std(std_list)
        cross_validation_results += 'The mean accuracy with cross validation is ' + str(mean_accuracy * 100) + '%\n'
        cross_validation_results += 'The standard deviation of the accuracy with cross validation is ' + str(
            std_accuracy) + '\n'
        cross_validation_results += 'The mean error with cross validation is ' + str(mean_error) + '\n'
        cross_validation_results += 'The standard deviation of the error with cross validation is ' + str(
            np.std(1 - np.array(std_list))) + '\n'
        cross_validation_results += '****************************************Cross Validation Ends**************************************\n'
        return mean_accuracy, np.std(std_list), cross_validation_results


if __name__ == '__main__':
    decision_tree = DecisionTree()
    train_data = DataUtils().get_train_data()
    test_data = DataUtils().get_test_data()
    tree = decision_tree.build_tree(train_data)
    file_1 = open('tree_diagram.txt', mode='w+')
    tree_print = decision_tree.print_tree(tree)
    print(tree_print)
    file_1.write(tree_print)
    file_1.close()
    ignor1, ignor2, res = decision_tree.cross_validation(train_data)
    file_1 = open('cross_validation.txt', mode='w+')
    print(res)
    file_1.write(res)
    file_1.close()
    predicted_labels = decision_tree.predict(test_data, tree)
    confusion_mat, accuracy = decision_tree.confusion_matrix(predicted_labels, [i[-1] for i in test_data])
    file_1 = open('accuracy.txt', mode='w+')
    accuracy_str = 'The Accuracy is at ' + str(
        accuracy * 100) + '% for the Test Data.\n' + 'This is what the Confusion Matrix looks like \n' + '\n'.join(
        [str(i) for i in confusion_mat])

    print(accuracy_str)
    file_1.write(accuracy_str)
    file_1.close()
