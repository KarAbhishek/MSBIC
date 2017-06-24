from BioInformatics.Week_15.forward_backward import forward_backward, get_matrix
from BioInformatics.Week_15.viterbi_learning import convert_tuple_dict_to_dict_of_dicts, convert_dict_of_dicts_to_tuple_dict


def distance(vec_1, vec_2):
    ls = 0
    for idx in range(len(vec_1)):
        ls += (vec_1[idx] - vec_2[idx]) ** 2
    return ls ** 0.5


def baum_welch(states, alphabet, le_string, transition_matrix, emission_matrix):
    from collections import defaultdict
    # transition_matrix = {state: {state_: 1.0/len(states) for state_ in states} for state in states}
    # emission_matrix = {state: {a: 1.0/len(states) for a in alphabet} for state in states}
    defa = lambda:defaultdict(defaultdict)
    prob_dict= defaultdict(defa)
    while True:

        transition_matrix = convert_dict_of_dicts_to_tuple_dict(transition_matrix)
        emission_matrix = convert_dict_of_dicts_to_tuple_dict(emission_matrix)
        ret = forward_backward(le_string, states, transition_matrix, emission_matrix)
        transition_matrix = convert_tuple_dict_to_dict_of_dicts(transition_matrix)
        emission_matrix = convert_tuple_dict_to_dict_of_dicts(emission_matrix)
        trans_bkp, ems_bkp = transition_matrix, emission_matrix
        for state in states:
            for state_ in states:
                for char in le_string:
                    prob_dict[state][state_][char] = ret[char][state]
        for state in states:
            for state_ in states:
                transition_matrix[state][state_] = sum(prob_dict[state][state_].values())

        for elem in transition_matrix:
            total = sum(transition_matrix[elem].values())
            for elem2 in transition_matrix[elem]:
                transition_matrix[elem][elem2] /= total

        for state in states:
            for char in le_string:
                emission_matrix[state][char] = sum(prob_dict[state][state_])

        for elem in emission_matrix:
            total = sum(emission_matrix[elem])
            for elem2 in emission_matrix[elem]:
                emission_matrix[elem][elem2] /= total

        if round(distance(transition_matrix, trans_bkp), 3) == round(distance(emission_matrix, ems_bkp), 3) == 0:
            break

        return transition_matrix, emission_matrix


if __name__ == '__main__':
    file = open('test')
    lines = file.read().splitlines()
    num = int(lines[0])
    le_string = lines[2]
    le_alphabets = lines[4].split()
    states_out = lines[6].split()
    logger_flag = True
    transition_matrix_out = get_matrix(lines[8:8 + (len(states_out) + 1)], logger_flag)
    emission_matrix_out = get_matrix(lines[(8 + len(states_out) + 2):], logger_flag)
    transition_matrix_out = convert_tuple_dict_to_dict_of_dicts(transition_matrix_out)
    emission_matrix_out = convert_tuple_dict_to_dict_of_dicts(emission_matrix_out)
    a, d = baum_welch(states_out, le_alphabets, le_string, transition_matrix_out, emission_matrix_out)
    print(a, d)
