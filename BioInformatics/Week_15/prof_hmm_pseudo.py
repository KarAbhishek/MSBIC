def get_index_np(threshold, aln):
    cumulative_threshold = threshold * len(aln)
    import numpy as np
    np_aln = np.array([list(elem) for elem in aln])

    return {idx for idx in range(np_aln.shape[1]) if np.where(np_aln[:, idx] == '-')[0].shape[0] >= cumulative_threshold}


def profile_hmm_pseudo(threshold, multiple_alignment):
    indeled_cols = get_index_np(threshold, multiple_alignment)

    from collections import defaultdict

    def defaulter():
        return defaultdict(int)

    emission_matrix = defaultdict(defaulter)  # Separate the tuples to make it easier for pandas

    states = []
    for single_elem_idx, single_elem in enumerate(multiple_alignment):
        single_state = []
        idx = 1
        for j in range(len(single_elem)):
            if j not in indeled_cols:  # Set has O(1) retrieval
                single_state.append('D' if multiple_alignment[single_elem_idx][j] == '-' else 'M' + str(idx))
                idx += 1
                if multiple_alignment[single_elem_idx][j] != '-':
                    emission_matrix['M' + str(idx)][multiple_alignment[single_elem_idx][j]] += 1
            elif multiple_alignment[single_elem_idx][j] != '-':  # No indel
                single_state.append('I' + str(idx - 1))
                emission_matrix['I' + str(idx - 1)][multiple_alignment[single_elem_idx][j]] += 1
        states.append(single_state)

    for key in emission_matrix:
        summation = sum(emission_matrix[key].values())
        emission_matrix[key] = {sub_key: 1.0 * emission_matrix[key][sub_key] / summation for sub_key in
                                emission_matrix[key] if summation > 0}

    transition_matrix = defaultdict(defaulter)
    transition_matrix.update({'S': {'I0': 0, 'D1': 0, 'M1': 0}, 'I0': {'I0': 0, 'D1': 0, 'M1': 0}})
    transition_matrix['S'] = {init_state: transition_matrix['S'][init_state] + 1 for init_state, *ignore in states}

    for single_elem_idx in range(len(states)):
        for j in range(len(states[single_elem_idx]) - 1):
            transition_matrix[states[single_elem_idx][j]][states[single_elem_idx][j + 1]] += 1
        transition_matrix[states[single_elem_idx][len(states[single_elem_idx]) - 1]]['E'] += 1

    for key in transition_matrix:
        total = sum(transition_matrix[key].values())
        transition_matrix[key] = {sub_key: 1.0 * transition_matrix[key][sub_key] / total for sub_key in
                                  transition_matrix[key] if total > 0}

    index_list = ['S', 'I0'  # Initial Guaranteed States
                  ] + [a + str(idx) for idx in range(1, len(multiple_alignment[0]) - len(indeled_cols) + 1) for
                                a in 'MDI'] + ['E']  # Ending State
    return emission_matrix, transition_matrix, index_list


def print_it(emission, transition, index_list):
    import pandas as pd
    pd.set_option('display.width', 1000)
    df = pd.DataFrame(transition, index=index_list, columns=index_list).fillna(0)
    print(df.transpose().round(3), end='\n--------\n')

    df = pd.DataFrame(emission, index=alphabet, columns=index_list).fillna(0)
    print(df.transpose().round(3), end='\n--------')


if __name__ == '__main__':
    file = open('test')
    lines = file.read().splitlines()
    threshold_out = float(lines[0].strip())
    alphabet = lines[2].strip().split()
    alignment = lines[4:]
    em, tran, idx_ls = profile_hmm_pseudo(threshold_out, alignment)
    print_it(em, tran, idx_ls)
