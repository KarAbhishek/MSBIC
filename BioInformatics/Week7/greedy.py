import operator as op


def apply_reversal_sorting(k, p):
    end_loc = [idx for idx, i in enumerate(p) if i == k or i == -k][0]
    return p[:k-1]+list(map(op.neg, p[k-1:end_loc+1][::-1]))+p[end_loc+1:]


def not_sorted(x, y):
    return x != y


def greedy_sort(p):
    ls = []
    approx_reversal_distance = 0
    for k in range(1, len(p)+1):
        if not_sorted(p[k-1], k):
            p = apply_reversal_sorting(k, p)
            ls.append(p[:])
            approx_reversal_distance += 1
        if p[k-1] == -k:
            p[k-1] = k
            ls.append(p)
            approx_reversal_distance += 1
    return ls


if __name__ == '__main__':
    seq_set = ''
    seq_set = seq_set[1:-1]
    split_seq = seq_set.split(' ')
    seq_list = list(map(int, split_seq))
    l = [list(map(str, i)) for i in greedy_sort(seq_list)]
    l_fu = lambda j:'+'+j if j.find('-')==-1 else j
    ret_var = ['('+str(' '.join(map(l_fu, i)))+')' for i in l]

    file = open('xx.txt', 'w+')
    file.write('\n'.join(ret_var))
    file.close()