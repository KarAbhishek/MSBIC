from collections import deque
def maxSlidingWindow(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    idx = k
    window = deque(nums[:k])
    max_ls = [max(window)]
    while idx < len(nums):
        window.popleft()
        window.append(nums[idx])
        max_ls.append(max(window))
        idx += 1
    return max_ls

print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))