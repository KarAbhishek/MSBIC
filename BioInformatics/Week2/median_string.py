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


def d(pattern, dna):
    k = len(pattern)
    dist = 0
    for txt in dna:
        hamming = float('inf')
        for i in range(len(txt) - k + 1):
            k_mer_pat_compl = txt[i:i + k]
            curr_ham = hamming_distance(pattern, k_mer_pat_compl)
            if hamming > curr_ham:
                hamming = curr_ham
        dist += hamming
    return dist


def median_string(dna, k):
    distance = float('inf')
    start_index = patternToNum(''.join(['A' for i in range(k)]))
    end_index = patternToNum(''.join(['T' for i in range(k)]))
    #print(distance, start_index, end_index)
    for i in range(start_index, end_index + 1):
        k_mer_pattern = numToPattern(i, k)
        total_ham_dist = d(k_mer_pattern, dna)
        if distance > total_ham_dist:
            distance = total_ham_dist
            median = k_mer_pattern
    return median


print(median_string(['ACCATAGTACCCGGGTCTGGTATGTGTTGGTGTCGCGTGGCA',
                     'GCACAGCTCCGGGCGAAAGGTATGGTACCGATTCCGCAGCTA',
                     'AGAGTGTCAAGTAGGCAGGTAGCACGTATGGGTTACGTAGTT',
                     'TATAGCCGTACACGGTGTGTTATGCGTATGGCGTATGACAGT',
                     'ACCGGGTAATTCAGTCTGTGGTACGTTGGTCGTATGGTGCCG',
                     'CACAGGTAGCAGCACGTGCTTCCACGTATGTGGCCGCGGTTG',
                     'TGTATGGGAGGGAAACATGGATAGCAGGTGTAAGCAAGGCCG',
                     'CGTATGGCGGAACTTTGGGTTTTCCACAGGGTTACATCTGTC',
                     'TGTATGAAGCTTAGCAGAAACATGGTATAGACGCCCACGAAA',
                     'GGTATGAAAGGCCCCCATTCTAGTAACCCGTCGACCAACTTT'], 6))
