def selection_sort(array: list):
    n = len(array)

    for i in range(n):

        smallest_index = i
     
        for j in range(i + 1, n):
            if array[j] < array[smallest_index]:
                smallest_index = j

        if smallest_index != i:
            array[i], array[smallest_index] = array[smallest_index], array[i]

    return array

print(selection_sort([33, 1, 89, 2, 67, 245]))