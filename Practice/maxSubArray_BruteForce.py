def k_len_slice(ls, start_pos, k):
    return ls[start_pos:start_pos+k]

ls = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_slice = float('-inf')
for k in range(1, len(ls)):
    for start_pos in range(len(ls)-k+1):
        slice_ = k_len_slice(ls, start_pos, k)
        sum_slice = sum(slice_)
        if sum_slice > max_slice:
            max_slice = sum_slice
print(max_slice)