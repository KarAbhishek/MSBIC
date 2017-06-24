import sys


def pattern_count(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            count += 1
    return count


def count_dict(text, k):
    count = {}
    for i in range(len(text) - k + 1):
        pattern = text[i:i + k]
        count[i] = pattern_count(pattern, text)
    return count


def frequent_words(text, k):
    frequent_patterns = []
    count = count_dict(text, k)
    m = max(count.values())
    for i in count:
        if count[i] == m:
            frequent_patterns.append(text[i:i + k])
    return frequent_patterns


lines = sys.stdin.read().splitlines()  # read in the input from STDIN
txt = lines[0]
K = int(lines[1])
print(frequent_words(txt, K))
