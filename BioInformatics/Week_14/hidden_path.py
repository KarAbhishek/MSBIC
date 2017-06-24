from math import log10


def get_matrix(lines, logger_flag=False):
    from collections import defaultdict
    transition_matrix = defaultdict(dict)
    column_keys = lines[0].strip().split('\t')
    for line in lines[1:]:
        row = line.strip().split('\t')
        row_key, matrix_row = row[0], row[1:]
        for content_idx, content in enumerate(matrix_row):
            transition_matrix[row_key, column_keys[content_idx]] = log10(float(content)) if logger_flag else float(content)
    return dict(transition_matrix)


def probability_of_hidden_path(hidden_path, transition_matrix):
    initial_probability = 0.5
    total_prob = initial_probability
    for idx in range(len(hidden_path)-1):
        total_prob *= transition_matrix[hidden_path[idx], hidden_path[idx+1]]
    return total_prob

if __name__ == '__main__':

    file = open('hidden_path_data.txt')
    lines = file.read().splitlines()
    hidden_path_out = lines[0]
    states_out = lines[2]
    transition_matrix_out = get_matrix(lines[4:])
    print(transition_matrix_out)
    prob_out = probability_of_hidden_path(hidden_path_out, transition_matrix_out)
    print(prob_out)
    file.close()
