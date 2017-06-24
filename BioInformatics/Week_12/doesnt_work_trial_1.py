from collections import defaultdict
def trie_construct(string_lists):
    hm = []
    counter_main = 0
    for single_string in string_lists:
        leading_edge = 0
        for char_idx, single_char in enumerate(single_string):
            weight = single_char
            if not hm or (hm and (char_idx >= len(hm) or weight != hm[char_idx][2])):
                counter_main += 1
                lagging_edge = counter_main
                # Create leading_edge->lagging_edge:weight
                hm.append([leading_edge, lagging_edge, weight])
            else:
                lagging_edge = hm[char_idx][1]
            leading_edge = lagging_edge


    dicto = defaultdict(list)
    for elem in hm:
        dicto[elem[0]].append(elem[1:])
    return hm, dicto


if __name__ == '__main__':
    file = open('input_1.txt')
    string_lists_out = file.read().splitlines()
    out, dict_out = trie_construct(string_lists_out)
    fmt_out = lambda x:str(x[0])+'->'+str(x[1])+':'+str(x[2])
    print('\n'.join(list(map(fmt_out, out))))
    print(dict_out)