from BioInformatics.Week_12.doesnt_work_trial_1 import trie_construct
def PrefixTrieMatching(Text, Trie):
    symbol = Text[0]
    v = 0  # root of tree
    counter = 0
    pattern_spelled = ''
    while True:
        if v not in Trie:
            print('Hello ', pattern_spelled)
            return pattern_spelled
        elif symbol in list(zip(*Trie[v]))[-1]:
            counter += 1
            bk_symbol = symbol
            if counter >= len(Text):
                print('Hello ', pattern_spelled)
                return
            symbol = Text[counter]

            pattern_spelled += symbol
            v = [i[0] for i in Trie[v] if i[-1] == bk_symbol]
            print(v)
            if v:
                v = v[0]
            # else:
            #
            #     print()
        else:
            # print("no matches found")
            return


def TrieMatching(Text, Trie):
    while Text:
        p = PrefixTrieMatching(Text, Trie)
        # print('Here is ', p)
        Text = Text[1:]


string_lists = ['ATCG', 'GGGT']
TrieMatching('AATCGGGTTCAATCGGGGT', trie_construct(string_lists)[1])