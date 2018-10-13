def insertion(A):
    L = len(A)
    for i in range(1, L):
        val = A[i]
        j = i
        while j > 0 and A[j - 1] > val:
            A[j] = A[j - 1]
            j -= 1
        A[j] = val
    return A



def find(A):
    L = len(A)
    A = insertion(A)
    third = A[-3]
    fifth = A[-5]
    return third + fifth

print(find([20, 24, 22, 13, 34, 13, 14, 33, 41, 10, 35, 1, 2, 24, 16, 20, 16, 23, 46, 41, 31, 7, 49, 25, 34, 15, 17, 18, 1, 30, 1, 17, 23, 43, 10, 4, 48, 44, 24, 23, 30, 0, 34, 30, 33, 27, 20, 42, 25, 5]))
