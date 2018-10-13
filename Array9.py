
def find(A):
    s = 0
    for i in A:
        if i[0] != 0 and i[1] != 1 and i[2] != 2 and i[3] != 3 and i[4] != 4 and i[5] != 5:
            s += 1
    return s

# n choose k. Written 7/25/2018, took me 4 hours...
# note: all return types are 2D arrays
def genComb(n, k):  
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
  
def delete(A, n):  # delete value at index i of array A
    B = A.copy()  # A.copy() is the key!!!!!!! Without it, I spent 1 hour debugging...
    L = len(B)
    assert(n < L)
    for i in range(n, L - 1):
        B[i] = B[i+1]
    return B[:-1]

# permutations of a given array, runtime O(n!). Written 7/26/2018
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


# k-permutations of a given array. Written 7/26/2018
def genPerm(A, k = None):
    n = len(A)
    if k == None:
        k = n
    assert(n >= k)
    result = []
    if k == 1:
        for a in A:
            result += [[a]]
        return result
    for i in range(n):
        a = genPerm(delete(A, i), k-1)
        for j in a:
            result += [[A[i]] + j]
    return result

# all derangements of a given array
#def derange(A):
    



print(find(genPerm([0,1,2,3,4,5])))
