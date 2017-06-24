from BioInformatics.Week_14.hidden_path import get_matrix


def forward_backward(string, states, transition_matrix, emission_matrix):
    from collections import defaultdict
    forward = defaultdict(defaultdict)

    for state in states:
        forward[0][state] = (1.0 / len(states)) * emission_matrix[(state, string[0])]
    for idx in range(1, len(string)):
        for state_ in states:
            forward[idx][state_] = 0
            for state in states:
                forward[idx][state_] += forward[idx - 1][state] * transition_matrix[state, state_] * \
                                               emission_matrix[state_, string[idx]]
    # ret = [forward[len(string) - 1][state] for state in states]
    backward = defaultdict(lambda:defaultdict(int))
    for state in states:
        backward[len(string) - 1][state] = 1.0
    for idx in range(len(string) - 1)[::-1]:
        for state_ in states:
            for state in states:
                backward[idx][state_] += backward[idx + 1][state] * transition_matrix[state_, state] * emission_matrix[state, string[idx + 1]]
    ret = {}
    for idx in range(len(string)):
        ret[string[idx]] = {}
        total = 0
        for state in states:
            ret[string[idx]][state] = forward[idx][state] * backward[idx][state]
            total += ret[string[idx]][state]
        for state in states:
            ret[string[idx]][state] = ret[string[idx]][state] / total

    import pandas as pd
    print(pd.DataFrame(ret).transpose())
    return ret


if __name__ == '__main__':
    file = open('test')
    lines = file.read().splitlines()
    le_string = lines[0]
    le_alphabets = lines[2]
    states_out = lines[4].split()
    logger_flag = True
    transition_matrix_out = get_matrix(lines[6:6 + (len(states_out) + 1)], logger_flag)
    emission_matrix_out = get_matrix(lines[(6 + len(states_out) + 2):], logger_flag)
    # print(le_string, le_alphabets, states_out, transition_matrix_out, emission_matrix_out)
    tree_out = forward_backward(le_string, states_out, transition_matrix_out, emission_matrix_out)
    print(tree_out)
