a = [
    [1, 4, 2, 5, 8],
    [3, 4, 5, 8, 2],
    [4 ,2 ,6 ,4, 7],
    [5, 4, 2, 6, 4],
    [4, 4, 6, 4, 2],
    [4, 2, 7, 3, 8]
]

# b = [
#     [5, 2, 3, 5],
#     [0, 2, 2, 7],
#     [5, 3, 5, 5],
#     [2, 2, 1, 0],
#     [8, 8, 6, 9],
# ]

b = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
]

c = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]


for k in range(len(a)):
    for j in range(len(b[0])):
        s = 0
        for i in range(len(a[0])):
            s += a[k][i] * b[i][j]
            c[k][j] = s

for i in range(len(c)):
    print(c[i])