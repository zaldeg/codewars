def valid_solution(board):
    s = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    for i in board:
        for j in i:
            if j == 0:
                return False
    for i in board:
        if set(i) != s:
            return False
    for i in range(9):
        if set((j[i] for j in board)) != s:
            return False
    for a in range(1, 8, 3):
        for b in range(1, 8, 3):
            # test = set()
            if s != set(
                board[i][j] for i in range(a - 1, a + 2) for j in range(b - 1, b + 2)
            ):
                # for i in range(a - 1, a + 2):
                #     for j in range(b - 1, b + 2):
                #         test.add(c[i][j])
                # if test != s:
                return False

    return True


c = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]

print(valid_solution(c))
