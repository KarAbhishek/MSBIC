def num_of_breakpoints(seq_list):
    return len([1 for idx in range(1, len(seq_list)) if seq_list[idx] - seq_list[idx-1] != 1])


seq_set = ''
seq_set = seq_set[1:-1]
split_seq = seq_set.split(' ')
seq_list = list(map(int, split_seq))
seq_list = [0] + seq_list + [len(seq_list)+1]
print(num_of_breakpoints(seq_list))