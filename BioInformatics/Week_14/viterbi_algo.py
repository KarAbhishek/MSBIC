from operator import itemgetter
from math import log10
from BioInformatics.Week_14.hidden_path import get_matrix


def find_max_by_comparator(ls, element_idx=0):
    return max(ls, key=itemgetter(element_idx))


def viterbi_algorithm(the_string, states, transition_matrix, emission_matrix):
    place_holder_dict = {item: (emission_matrix[item, the_string[0]] - log10(len(states)), ) for item in states}
    dag = [place_holder_dict]
    for idx in range(len(the_string)-1):
        place_holder_dict = dict()

        for item in states:
            total_probability = []
            for state in states:
                total_probability.append((
                    emission_matrix[item, the_string[idx + 1]] + transition_matrix[state, item] + dag[idx][state][0],
                    state))
            place_holder_dict[item] = find_max_by_comparator(total_probability)
        dag.append(place_holder_dict)
    place_holder_dict = dict()
    total_probability = []
    for state in states:
        total_probability.append((dag[len(the_string) - 1][state][0], state))
    place_holder_dict['placeholder'] = find_max_by_comparator(total_probability)
    dag.append(place_holder_dict)
    return dag


def backtrack_viterbi(tre):
    ls = []
    curr_state = 'placeholder'
    for i in range(1, len(tre))[::-1]:
        state = tre[i][curr_state][1]
        ls.append(state)
        curr_state = state
    return ''.join(ls)[::-1]


if __name__ == '__main__':
    file = open('viterbi_data')
    lines = file.read().splitlines()
    le_string = lines[0]
    le_alphabets = lines[2]
    states_out = lines[4].split()
    logger_flag = True
    transition_matrix_out = get_matrix(lines[6:6 + (len(states_out) + 1)], logger_flag)
    emission_matrix_out = get_matrix(lines[(6 + len(states_out) + 2):], logger_flag)
    print(le_string, le_alphabets, states_out, transition_matrix_out, emission_matrix_out)
    tree_out = viterbi_algorithm(le_string, states_out, transition_matrix_out, emission_matrix_out)
    hidden_path_out = backtrack_viterbi(tree_out)
    print('Here ', hidden_path_out)
    file.close()
