def adjacency_list_to_matrix(dictionary:dict):

    n = len(dictionary)
    matrix = [[0]*n for _ in range(n)]

    for node, neighbors in dictionary.items():
        for neighbor in neighbors:
            matrix[node][neighbor] = 1

    for row in matrix:
        print(row)

    return matrix

print(adjacency_list_to_matrix({0: [1, 2], 1: [2], 2: [0, 3], 3: [2]}))