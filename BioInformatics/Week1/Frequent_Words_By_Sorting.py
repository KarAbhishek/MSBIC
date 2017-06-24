import time


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


def finding_frequent_words_by_sorting(text, k):
    frequent_Patterns = set()
    count = []
    index = []
    for i in range(len(text) - k + 1):
        pattern = text[i:i + k]
        index.append(patternToNum(pattern))
        count.append(1)
    sorted_index = sorted(index)
    for i in range(1, len(text) - k + 1):
        if sorted_index[i] == sorted_index[i - 1]:
            count[i] = count[i - 1] + 1
    max_count = max(count)
    for i in range(len(text) - k + 1):
        if count[i] == max_count:
            pattern = numToPattern(sorted_index[i], k)
            frequent_Patterns.add(pattern)
    return frequent_Patterns

start_time = time.clock()
print(' '.join(finding_frequent_words_by_sorting(
    'AACCGTTGCTAACCGTTGCTCCCGGTAACACCGTGGCCACCGTGGCCCCCGGTAACACCGTGGCCCCGATAAACACCGATAAACAACCGTGGCCACCGTGGCCACCGTGGCCCCGATAAACAAACCGTTGCTCCCGGTAACTGGCTGGAAGTGGCTGGAAGTGGCTGGAAGTGGCTGGAAGTGGCTGGAAGTGGCTGGAAGACCGTGGCCTGGCTGGAAGAACCGTTGCTCCCGGTAACCCGATAAACACCCGGTAACTGGCTGGAAGCCCGGTAACCCGATAAACAACCGTGGCCCCCGGTAACTGGCTGGAAGTGGCTGGAAGACCGTGGCCAACCGTTGCTTGGCTGGAAGACCGTGGCCCCCGGTAACCCCGGTAACAACCGTTGCTCCCGGTAACAACCGTTGCTTGGCTGGAAGCCGATAAACATGGCTGGAAGACCGTGGCCTGGCTGGAAGAACCGTTGCTCCCGGTAACAACCGTTGCTCCGATAAACATGGCTGGAAGCCGATAAACAAACCGTTGCTCCCGGTAACCCCGGTAACTGGCTGGAAGTGGCTGGAAGTGGCTGGAAGAACCGTTGCTACCGTGGCCAACCGTTGCTAACCGTTGCTCCCGGTAACCCGATAAACACCCGGTAACTGGCTGGAAGTGGCTGGAAGTGGCTGGAAGCCGATAAACAACCGTGGCCCCGATAAACACCCGGTAACACCGTGGCCAACCGTTGCTACCGTGGCCCCCGGTAACCCGATAAACACCCGGTAACTGGCTGGAAGTGGCTGGAAGTGGCTGGAAGAACCGTTGCTTGGCTGGAAGCCCGGTAACTGGCTGGAAGCCCGGTAACTGGCTGGAAGAACCGTTGCTCCGATAAACACCGATAAACATGGCTGGAAGTGGCTGGAAG',
    13)))
print('The time taken is', time.clock() - start_time, "seconds")