def find(A): # A is a 2D array
    row = 0
    for i in range(0, len(A)):
        for j in A[i]:
            row = row + j

    colSum = 0
    col = 1
    for j in range(0, 10):
        for i in range(0, len(A)):
            col = col * A[i][j]
        colSum = colSum + col
        col = 1
    
    return colSum + row

B = [[5, 10, 10, 1, 6, 4, 3, 9, 6, 4],
    [2, 10, 9, 4, 9, 5, 1, 10, 1, 5],
    [1, 3, 7, 3, 10, 7, 5, 1, 7, 5],
    [5, 1, 2, 7, 3, 2, 4, 2, 1, 3],
    [7, 6, 6, 6, 4, 10, 5, 1, 5, 5],
    [3, 1, 10, 5, 8, 1, 9, 10, 2, 7],
    [1, 7, 1, 10, 5, 10, 5, 3, 3, 3],
    [6, 3, 10, 2, 5, 1, 6, 7, 10, 9],
    [1, 7, 9, 6, 2, 7, 10, 1, 9, 6],
    [10, 9, 6, 10, 4, 7, 6, 3, 4, 7]]

print(find(B))
