from BioInformatics.Week_14.hidden_path import get_matrix


def likelihood(string, states, transition_matrix, emission_matrix):
    from collections import defaultdict
    placeholder_dict = defaultdict(defaultdict)

    for state in states:
        placeholder_dict[0][state] = (1.0 / len(states)) * emission_matrix[(state, string[0])]
    for idx in range(1, len(string)):
        for item in states:
            placeholder_dict[idx][item] = 0
            for state in states:
                placeholder_dict[idx][item] += placeholder_dict[idx - 1][state] * transition_matrix[state, item] * emission_matrix[
                    item, string[idx]]
    res = [placeholder_dict[len(string) - 1][state] for state in states]
    return sum(res)


if __name__ == '__main__':
    file = open('viterbi_data')
    lines = file.read().splitlines()
    le_string = lines[0]
    le_alphabets = lines[2]
    states_out = lines[4].split()
    transition_matrix_out = get_matrix(lines[6:6 + (len(states_out) + 1)])
    emission_matrix_out = get_matrix(lines[(6 + len(states_out) + 2):])
    print(le_string, le_alphabets, states_out, transition_matrix_out, emission_matrix_out)
    prob_out = likelihood(le_string, states_out, transition_matrix_out, emission_matrix_out)
    print('Here ', prob_out)
    file.close()
