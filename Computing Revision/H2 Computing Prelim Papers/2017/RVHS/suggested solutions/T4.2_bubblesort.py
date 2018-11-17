def bubble_recursive(lst, n):
    if n < 2:
        return 0

    count = 0
    swapped = False

    for i in range(n-1):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
            swapped = True
        count += 1

    if swapped:
        return count + bubble_recursive(lst, n-1)
    else:
        return count

lst1 = [1, 15, 2, 4, 3, 9, 7, 10]
lst2 = [1, 15, 2, 4, 3, 9, 7, 10, 13, 5, 20]
c1 = bubble_recursive(lst1, len(lst1))
c2 = bubble_recursive(lst2, len(lst2))
print(lst1, c1)
print(lst2, c2)