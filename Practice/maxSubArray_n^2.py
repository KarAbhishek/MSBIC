def k_len_slice(ls, start_pos, k):
    return ls[start_pos:start_pos+k]


ls = [1, 2]
max_slice = float('-inf')
for k in range(1, len(ls)+1):
    curr_slice = sum(ls[:k])
    max_slice = curr_slice if max_slice < curr_slice else max_slice
    for start_pos in range(1, len(ls) - k + 1):
        curr_slice -= ls[start_pos - 1]
        curr_slice += ls[start_pos + k - 1]
        if max_slice < curr_slice:
            max_slice = curr_slice
print(max_slice)
