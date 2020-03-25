def mmultiply_matrix(a, b):
    return [
        [a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
        [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]],
    ]


Q = [[5, 3], [2, 2]]

print(multyply_fib(Q, Q))


# def multiply_matrix(a, b):
#     result = [[0 for i in range(len(b[0]))] for j in range(len(a))]
#     for y in range(len(result)):
#         for x in range(len(result[0])):
#             result[y][x] = sum([a[y][i] * b[i][x] for i in range(len(b))])
#     return result
