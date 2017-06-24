def b_nary(ls):
    print(b_nary_helper(ls, 0, len(ls)-1))


def b_nary_helper(ls, low, high):
    mid = low + (high-low)//2
    if ls[mid-1] > ls[mid]:
        return mid
    if ls[low] > ls[high]:
        return b_nary_helper(ls, low, mid)
    else:
        return b_nary_helper(ls, mid+1, high)


ls = [77, 86, 88, 1, 2, 3, 4, 7, 68, 69]
b_nary(ls)
