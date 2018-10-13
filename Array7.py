def find(A, B):
    smallest = 1000
    for i in A:
        s,x,y = 23,0,0
        for j in i:
            if j == True:
                x += 1
            else:
                y += 1
            s += B[x][y]
        if s < smallest:
            smallest = s
    return s

c = []
def genComb(n, k):  # n choose k. Written 7/25/2018, took me 4 hours...
    assert(n >= k)
    if k == 0:
        return [[False] * n]
    if k == n:
        return [[True] * n]
    result = []
    front = genComb(n-1, k)
    for i in front:
        result += [[False] + i]
    back = genComb(n-1, k-1)
    for j in back:
        result += [[True] + j]
    return result
# note: all return types are 2D arrays

def genPerm(A):
    n = len(A)
    if n == 1:
        return [A]
    result = []
    for i in range(n):
        a = genPerm(delete(A, i))
        for j in a:
            result += [[A[i]] + j]
    return result

        
def delete(A, n):  # delete value at index i of array A
    L = len(A)
    assert(n < L)
    for i in range(n, L - 1):
        A[i] = A[i+1]
    return A[:-1]

genPerm([1,2,3,4])

# note: using + to add two lists will combine them

def generateComb(n=12):
    b = []
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    for m in range(l+1, n):
                        for o in range(m+1, n):
                            a = [True] * n
                            a[i] = False
                            a[j] = False
                            a[k] = False
                            a[l] = False
                            a[m] = False
                            a[o] = False
                            b.append(a)
    return b

B = [[23, 32, 62, 20, 77, 42, 31],
[15, 14, 10, 11, 48, 32, 30],
[14, 46, 71, 31, 53, 7, 82],
[20, 12, 78, 78, 46, 24, 43],
[37, 16, 12, 99, 15, 97, 85],
[13, 29, 82, 71, 63, 27, 75],
[44, 81, 80, 48, 2, 45, 17]]

# sample answer
num = 7
def min(x, y):
    if (x, y) == (num - 1, num - 1):
        return B[num - 1][num - 1]
    to_visit = [(x + 1, y), (x, y + 1)]
    minimum = 100000
    for m, n in to_visit:
        if (m < 0) or (m >= num) or (n < 0) or (n >= num):
            continue
        else:
            cost = B[x][y] + min(m, n)
            if cost < minimum:
                minimum = cost
    return minimum


print(find(genComb(12, 6), B))
print(min(0,0))

#Consider the square grid above. Suppose a person wants to move from the top left corner towards the bottom right corner. To move, a person can go down or right.
#Let S be the path traversed such that the sum of the cells in the path is minimized.
#What is the value of S?



