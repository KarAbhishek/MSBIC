import sys


def mostFrequentK_Mers(text, k):
    lset = set()
    maxTillNow = -1
    for i in range(len(text) - k + 1):
        patCount = patternCount(text, text[i:i + k])
        if maxTillNow == patCount:
            lset.add(text[i:i + k])
        elif maxTillNow < patCount:
            lset = set()
            lset.add(text[i:i + k])
            maxTillNow = patCount

    return lset


def patternCount(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            count += 1
    return count


lines = sys.stdin.read().splitlines()  # read in the input from STDIN
txt = lines[0]
K = int(lines[1])
print(mostFrequentK_Mers(txt, K))