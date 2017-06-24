from BioInformatics.Week_13.inverse_BWT import preprocess_and_get_dict


def bw_matching(bwt_text, patterns):
    _, start_end_dict, last_to_first, last_column = preprocess_and_get_dict(bwt_text)
    ret = []
    for pattern in patterns:
        ret.append(bw_single_pattern_match(last_column, pattern, last_to_first))
    return ret


def bw_single_pattern_match(last_column, pattern, last_to_first):
    top = 0
    bottom = len(last_column) - 1
    while top <= bottom:
        if pattern:
            symbol = pattern[-1]
            pattern = pattern[:-1]
            top_idx, bottom_idx = None, None
            for position in range(top, bottom+1):
                if last_column[position][0] == symbol:
                    top_idx = position
                    break
            for position in range(top, bottom+1):
                if last_column[position][0] == symbol:
                    bottom_idx = position
            if top_idx is None or bottom_idx is None:
                return 0
            top = last_to_first[top_idx]
            bottom = last_to_first[bottom_idx]
        else:
            return bottom - top + 1


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

if __name__ == '__main__':
    file = open('bw_matching_data.txt')
    lines = file.read().splitlines()
    bwt_text_out = lines[0]
    patterns_out = lines[1].split()
    out = bw_matching(bwt_text_out, patterns_out)
    print(' '.join(map(str, out)))
