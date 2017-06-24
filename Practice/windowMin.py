def window_min(ls, k):
    window = ls[:k]
    if window is None:
        return []
    ret = [min(window)]
    for i in range(k, len(ls)):
        window.pop(0)
        window.append(ls[i])
        ret.append(min(window))
    return ret

print(window_min([1, 2, 3, 4], 3))
