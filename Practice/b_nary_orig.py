def b_nary(ls):
    print(b_nary_helper(ls, 0, len(ls), 69))


def b_nary_helper(ls, low, high, target):
    mid = low + (high-low)//2
    if ls[mid] == target:
        return mid
    if ls[mid] > target:
        return b_nary_helper(ls, low, mid, target)
    else:
        return b_nary_helper(ls, mid+1, high, target)


ls = [1, 2, 3, 4, 7, 68, 69, 86, 88]
b_nary(ls)