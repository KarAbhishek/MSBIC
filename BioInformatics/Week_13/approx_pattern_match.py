# put your python code here

def hamming_distance(str1, str2):
    count = 0
    for idx, elem in enumerate(str1):
        if str2[idx] != elem:
            count += 1
    return count

def pattern_list(text, pattern, d):
    start_pos = []
    for i in range(len(text) - len(pattern) + 1):
        if hamming_distance(text[i:i + len(pattern)], pattern) <= d:
            start_pos.append(i)
    return start_pos

# readL = sys.stdin.read().splitlines()
# st1 = readL[0]
# st2 = readL[1]
# st3 = int(readL[2])
# print(pattern_list(st1, st2, st3))

file = open('input_1.txt')
lines = file.read().splitlines()
pattern = lines[0]
list_pat = lines[1].split()
d = int(lines[2])
ls = []
for i in list_pat:
    ls += pattern_list(pattern, i, d)
print(' '.join(map(str, sorted(ls))))