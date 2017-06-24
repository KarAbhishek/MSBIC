def param_estimation(states, alphabet, ze_string, state_sequence):
    from collections import defaultdict
    transition_matrix = defaultdict(lambda: defaultdict(int))
    for state_idx in range(len(state_sequence)-1):
        transition_matrix[state_sequence[state_idx]][state_sequence[state_idx + 1]] += 1

    for key in transition_matrix:
        total = sum(transition_matrix[key].values())
        for single in transition_matrix[key]:
            transition_matrix[key][single] /= total
    # for state in states:
    #     for state_ in states:
    #         try:
    #             transition_matrix[state][state_] = state_sequence.count(state+state_)/state_sequence[1:].count(state)
    #         except ZeroDivisionError:
    #             transition_matrix[state][state_] = 1/len(states)

    emission_matrix = defaultdict(lambda: defaultdict(int))
    for state_idx, state in enumerate(state_sequence):
        emitted_char = ze_string[state_idx]
        emission_matrix[state][emitted_char] += 1

    for key in emission_matrix:
        total = sum(emission_matrix[key].values())
        for single in emission_matrix[key]:
            emission_matrix[key][single] /= total


    import pandas as pd
    tran_df = (pd.DataFrame(transition_matrix, index=states, columns=states).fillna(0).round(3))
    emm_df = (pd.DataFrame(emission_matrix, index=alphabet, columns=states).fillna(0).round(3))
    return tran_df.to_dict(), emm_df.to_dict()


if __name__ == '__main__':
    file = open('param_est_data')
    lines = file.read().splitlines()
    le_string = lines[0]
    alphabet_out = lines[2].split()
    state_sequence_out = lines[4]
    states_out = lines[6].split()
    param_estimation(states_out, alphabet_out, le_string, state_sequence_out)