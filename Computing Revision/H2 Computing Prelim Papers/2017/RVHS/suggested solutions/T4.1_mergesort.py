def merge_sort(lst):
    n = len(lst)
    if n < 2:
        return lst

    left = merge_sort(lst[:n//2])
    right = merge_sort(lst[n//2:])
    return merge(left, right)


def merge(left, right):
    results = [0] * (len(left)+len(right))
    i, j, index = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            results[index] = left[i]
            i = i + 1
        else:
            results[index] = right[j]
            j = j + 1
        index = index + 1
    while i < len(left):
        results[index] = left[i]
        i = i + 1
        index = index + 1
    while j < len(right):
        results[index] = right[j]
        j = j + 1
        index = index + 1
    return results

print(merge_sort([1, 15, 2, 4, 3, 9, 7, 10]))