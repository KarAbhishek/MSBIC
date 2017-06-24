def two_sum(nums, target):
    # hm = {i:idx for idx, i in enumerate(nums)}
    hm = {}
    for idx, i in enumerate(nums):
        if target-i in hm:
            return idx, hm[target-i]
        else:
            hm[i] = idx
    return None, None

two_sum([3,2,4], 6)