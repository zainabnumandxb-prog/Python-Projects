def dfs_n_queens(n):
    if n < 1:
        return []

    solutions = []
    stack = [(0, [])]

    while stack:
        row, board = stack.pop()

        if row == n:
            solutions.append(board)
            continue

        for col in range(n - 1, -1, -1):
            is_safe = True
            for prev_row in range(row):
                prev_col = board[prev_row]
                if prev_col == col or abs(prev_row - row) == abs(prev_col - col):
                    is_safe = False
                    break

            if is_safe:
                stack.append((row + 1, board + [col]))

    return solutions

print(dfs_n_queens(5))