
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
  
    def delete(A, n):
        '''delete value at index i of array A'''
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



# derangements of a given array. Written 8/02~04/2018
def genDerange(A):
    n = len(A)
    if n == 1:  # note: should not return 2D array, else recursion goes wrong
        return []
    if n == 2:
        return [[A[1], A[0]]]
    if n == 3:  # unnecessary but can speed up computation
        return [[A[1], A[2], A[0]], [A[2], A[0], A[1]]]
    
    # basic idea: put A[0] at each location from 1 to n-1,
    # each time the element at that position has two choices:
    # go to index 0, so need to derange the rest of elements (f(n-2))
    # or don't go to index 0, so need to derange all elements
    # except the original A[0] (f(n-1))
    
    result = []
    for i in range(n-1):
        sub = delete(A[1 : ], i)  # the array without A[0] and A[i+1]
        front = genDerange(sub)   # f(n-2)
        for j in front:
            result += [[A[i+1]] + j[ : i] + [A[0]] + j[i : ]]
        # A[i+1] is the element that's replaced by A[0]
        
        back = genDerange([A[i+1]] + sub)   # f(n-1)
        for k in back:
            result += [k[ : i+1] + [A[0]] + k[i+1 : ]]
    
    return result

a = genPerm([0,1,2,3,4,5,6,7,8,9])

print(a[999999])

