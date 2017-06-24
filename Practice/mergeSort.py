def merge_sort(a, start, end):
    if start >= end: return
    mid = start + (end - start) // 2
    merge_sort(a, start, mid)
    merge_sort(a, mid + 1, end)
    merge(a, start, mid, end)


def merge(a, start, mid, end):
    left = a[start:mid + 1]
    right = a[mid + 1:end + 1]
    left_idx, right_idx = 0, 0
    i = start
    # for i in range(start, end+1):
    while left_idx < len(left) and right_idx < len(right):

        if left[left_idx] < right[right_idx]:
            a[i] = left[left_idx]
            left_idx += 1
        else:
            a[i] = right[right_idx]
            right_idx += 1
        i += 1
    while left_idx < len(left):
        a[i] = left[left_idx]
        left_idx += 1
        i += 1

    while right_idx < len(right):
        a[i] = right[right_idx]
        right_idx += 1
        i += 1


a1 = [12, 11, 13, 5, 6, 7]
merge_sort(a1, 0, 5)
print(a1)
