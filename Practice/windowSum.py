def window_sum(ls, k):

    window = ls[:k]
    if window is None:
        return []
    ret = [sum(window)]
    for i in range(k, len(ls)):
        window.pop(0)
        window.append(ls[i])
        ret.append(sum(window))
    return ret

print(window_sum([1, 2, 3, 4], 3))
