from BioInformatics.Week_13.inverse_BWT import preprocess_and_get_dict


def generate_checkpoint(strin, threshold):
    from collections import defaultdict

    checkpoint = defaultdict()
    k = len(strin) // (threshold + 1)
    for idx in range(0, len(strin), k):
        curr_status = idx+1
        if curr_status > threshold:
            checkpoint[idx] = strin[idx:]  # If Beyond threshold lump everything together
            break
            print('lolo', checkpoint[idx])
        else:
            print('lala', checkpoint[idx])
            checkpoint[idx] = strin[idx: idx + k]  # Take k_mer

    return checkpoint


def matches(strin_1, strin_2, threshold):
    mismatch_count = 0
    for idx in range(len(strin_1)):
        if strin_1[idx] == strin_2[idx]:
            mismatch_count += 1
            if mismatch_count > threshold:
                return False
    return True


def bw_matching(bwt_text, patterns):
    _, start_end_dict, _, _ = preprocess_and_get_dict(bwt_text)
    ret = []
    for pattern in patterns:
        ret.append(single_pattern_match(start_end_dict, pattern))
    return ret


def single_pattern_match(start_end_dict, pattern):
    later_starts = list(start_end_dict.keys())
    for char_idx in range(1, len(pattern))[::-1]:
        last_char = pattern[char_idx]
        penultimate_char = pattern[char_idx - 1]
        later_starts = [edge_end for edge_start, edge_end in start_end_dict.items() if
                        edge_start[0] == last_char and edge_end[0] == penultimate_char and edge_start in later_starts]
        if not later_starts:
            return 0

    return len(later_starts)


bwt_ret = bwt(bwt_text_out)
suf_arr_ret = (suffix_arrays(bwt_ret))

print(suf_arr_ret)