# put your python code here
import sys

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

file = open('data/input')
lines = file.read().splitlines()
pat = lines[0]
dnaS = lines[1].split(' ')
print(d(pat, dnaS))
