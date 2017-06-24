def preprocess_and_get_dict(final_string):
    from collections import defaultdict
    sort_final_string = sorted(final_string)
    hm_1 = defaultdict(int)
    hm_2 = defaultdict(int)
    end_hm = {}
    start_end_hm = {}
    idx_path = {}
    last_column = []
    for idx, char in enumerate(final_string):
        hm_1[char] += 1
        hm_2[sort_final_string[idx]] += 1
        end_hm[char + str(hm_1[char])] = sort_final_string[idx] + str(hm_2[sort_final_string[idx]])
        start_end_hm[sort_final_string[idx] + str(hm_2[sort_final_string[idx]])] = char + str(hm_1[char])
        idx_path[sort_final_string[idx] + str(hm_2[sort_final_string[idx]])] = idx
        last_column.append(char + str(hm_1[char]))

    last_to_first = {}
    for edge_start, edge_end in start_end_hm.items():
        last_to_first[idx_path[edge_start]] = idx_path[edge_end]
    return end_hm, start_end_hm, last_to_first, last_column


def inverse_bwt(final_string):
    end_hm, _, _,  = preprocess_and_get_dict(final_string)
    curr_node = '$1'
    ret = []
    while True:
        curr_node = end_hm[curr_node]
        if curr_node == '$1':
            break
        ret.append(curr_node[0])
    ret.append('$')
    return ret


if __name__ == '__main__':
    ret_out = inverse_bwt('TTACA$AAGTC')
    print(''.join(ret_out))