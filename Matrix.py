def getcolumn( matrix , index ):
    return [ [r[index]] for r in matrix ]

def ADD( A , B ):
    return [ [A[j][i] + B[j][i]
              for i in range(len(A[0]))] for j in range(0,len(A[0]))]

def mult1D(row , col):
    return [sum([row[i] * col[i][0] for i in range(len(row))])]

def transpose(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]

print(transpose([[1,2,3],[4,5,6],[7,8,9]]))
