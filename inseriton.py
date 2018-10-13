def insertion(A):
    L = len(A)
    numSwap = 0
    for i in range(1, L):
        val = A[i]
        j = i
        while j > 0 and A[j - 1] > val:
            A[j] = A[j - 1]
            j -= 1
            numSwap += 1
        A[j] = val

    print(numSwap)
    return A
