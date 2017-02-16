import itertools


def numToPattern(idx, k):
    if k == 1:
        return numToSymbol(idx)
    return numToPattern(int(idx / 4), k - 1) + numToSymbol(idx % 4)


def numToSymbol(sym):
    if sym == 0:
        return 'A'
    if sym == 1:
        return 'C'
    if sym == 2:
        return 'G'
    if sym == 3:
        return 'T'


def patternToNum(pattern):
    if pattern == '':
        return 0
    return 4 * patternToNum(pattern[:-1]) + symbolToNum(pattern[-1])


def symbolToNum(sym):
    if sym == 'A':
        return 0
    if sym == 'C':
        return 1
    if sym == 'G':
        return 2
    if sym == 'T':
        return 3


def hamming_distance(str1, str2):
    count = 0
    for idx, elem in enumerate(str1):
        if str2[idx] != elem:
            count += 1
    return count


def approx_pattern_count(text, pattern, d):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if hamming_distance(text[i:i + len(pattern)], pattern) <= d:
            count += 1
    return count


def pattern_list(text, pattern, d):
    start_pos = []
    for i in range(len(text) - len(pattern) + 1):
        if hamming_distance(text[i:i + len(pattern)], pattern) <= d:
            start_pos.append(i)
    return ' '.join(map(str, start_pos))


def generate_possible_k_mers(k):
    return [''.join(i) for i in itertools.product('AGCT', repeat=k)]


# print(pattern_list('AACAAGCTGATAAACATTTAAAGAG', 'AAAAA', 2))
print(approx_pattern_count('', 'TCATCA', 2))




def freq_words(text, k, d):
    final_ls = []
    max_cnt = 0
    itr = generate_possible_k_mers(k)
    for i in itr:
        curr_cnt = approx_pattern_count(text, i, d)
        if curr_cnt > max_cnt:
            max_cnt = curr_cnt
            final_ls = [i]
        elif curr_cnt == max_cnt:
            final_ls.append(i)

    return ' '.join(final_ls)


def neighbours(pattern, d):
    if d == 0:
        return pattern
    if len(pattern) == 1:
        return {'A', 'G', 'C', 'T'}
    neighbourhood = set()
    for i in neighbours(pattern[1:], d):
        if hamming_distance(pattern[1:], i) < d:
            for nucleotide in 'AGCT':
                neighbourhood = neighbourhood.union([nucleotide + i])
        else:
            neighbourhood = neighbourhood.union([pattern[0] + i])
    return neighbourhood

def FrequentWordsWithMismatches(Text, k, d):
    FrequentPatterns = set()
    Neighborhoods = list()
    for i in range(len(Text) - k + 1):
        Neighborhoods += neighbours(Text[i: i + k], d)
        Neighborhoods += neighbours(Text[i: i + k], d)
    #NeighborhoodArray = deepcopy(Neighborhoods)
    #Count = [0 for x in range(len(Neighborhoods))]
    #Index = [0 for x in range(len(Neighborhoods))]
    Count = []
    Index = []
    for i in range(len(Neighborhoods)):
        Pattern = Neighborhoods[i]
        #Index[i] = patternToNum(Pattern)
        Index.append(patternToNum(Pattern))
        #Count[i] = 1
        Count.append(1)
    SortedIndex = sorted(Index)
    for i in range(len(Neighborhoods) - 1):
        if SortedIndex[i] == SortedIndex[i + 1]:
            Count[i + 1] = Count[i] + 1
    maxCount = max(Count)
    for i in range(len(Neighborhoods)):
        if Count[i] == maxCount:
            Pattern = numToPattern(SortedIndex[i], k)
            FrequentPatterns.add(Pattern)
    return ' '.join(FrequentPatterns)

def findRverseComplement(text):
    retVar =''
    for i in text[::-1]:
        if i == 'A':
            retVar+='T'
        if i == 'G':
            retVar+='C'
        if i == 'C':
            retVar+='G'
        if i == 'T':
            retVar+='A'
    return retVar

'''
start_time = time.clock()
print(FrequentWordsWithMismatches(
    'TTCACGCTTCACGCCGCTCACGCCGCCGCAAATTCAAAAATCATTCACGCATCATCAAAATTCAAAAAAATCACGCTTCAAAATCAATCATCACGCTTCAAAAAAATTCATTCAATCACGCAAAATCACGCAAACGCTTCACGCCGCAAACGCCGCTTCATCATCACGCTTCACGCTCACGCCGCTCAAAAAAATCACGCCGCTTCACGCTTCATCATCAAAATCAAAATTCAATCATCATTCATCATCATCAAAATTCAATCATCACGCAAAAAAATCAATCAAAATTCATCATTCAATCATCATTCAATCAAAACGCATCAAAACGCTTCACGCCGCAAAATCAAAACGCATCACGCATCAATCATTCAATCACGCAAAAAA',
    7, 3))
print('The time taken is', time.clock() - start_time, "seconds")
'''

print('\n'.join(neighbours(pattern = 'AGAGTTAGAA', d = 3)))
#print(approx_pattern_count('ACCCACTGACAAAATAATATACCTTAAGGCCCGCCGTGCGCGCTTAGCACTCAAGATTAAAAACGACAGCGCTCTGAGCCATCGTTAGCCTGGGGCGTCAAGTAAACATGAGGTCACGCGGATTTCTAGATGGTCGCCCTGGAGCTGTGTAGAATTTCACTTTTCAATTGGGAAAACTCCCCGCTCGGCAGCCCTTGCAACTAGCTTAGGGGCACTGGATCAGAGTCTACAGTGCTACAGCACCGTGATTAAACGAGCTTCGTCACAGATCAATCAACATCCGTGCATTGCGCGGTGTAGCTGCTGATCCTCGCGGTGTAGC', 'CCGTG', 3))


