def quick_sort(a, start, end):
    if start >= end:
        return
    p = partition(a, start, end)
    quick_sort(a, start, p-1)
    quick_sort(a, p+1, end)


def partition(a, low, high):
    pivot = a[high]
    sml_idx = low - 1
    for i in range(low, high):
        if a[i] < pivot:
            sml_idx += 1
            a[sml_idx], a[i] = a[i], a[sml_idx]
    a[sml_idx+1], a[high] = a[high], a[sml_idx+1]
    return sml_idx+1

a1 = [12, 11, 13, 5, 6, 7]
quick_sort(a1, 0, 5)
print(a1)