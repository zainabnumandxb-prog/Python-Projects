def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[-1]

    smaller = []
    equal = []
    greater = []

    for element in array:
        if element < pivot:
            smaller.append(element)
        elif element == pivot:
            equal.append(element)
        else:
            greater.append(element)

    return quick_sort(smaller) + equal + quick_sort(greater)

print(quick_sort([]))
print(quick_sort([20, 3, 14, 1, 5]))
print(quick_sort([83, 4, 24, 2]))
print(quick_sort([4, 42, 16, 23, 15, 8]))
print(quick_sort([87, 11, 23, 18, 18, 23, 11, 56, 87, 56]))