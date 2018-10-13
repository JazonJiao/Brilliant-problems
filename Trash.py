def genComb(n, k):  # n choose k, written 7/25/2018
    assert(n >= k)
    if k == 0:
        return [False] * n
    if k == n:
        return [True] * n
    else:    # if k < n:
        front = genComb(n-1, k)
        if type(front[0]) is bool:
            front += [True]
        elif type(front[0]) is list:
            for i in front:
                i += [True]
        
        back = genComb(n-1, k-1)
        if type(back[0]) is bool:
            back += [False]
        elif type(back[0]) is list:
            for j in back:
                j += [False]
        if type(front[0]) == bool and type(back[0]) == bool:
        return [front] + [back]
    elif type(front[0]) == list and type(back[0]) == bool:
        return front + [back]
    elif type(front[0]) == bool:
        return [front] + back
    else:
        return front + back

##    def transform(A, n):
##    l = len(A)
##    a = l // n
##    M = []
##    for i in range(a):
##        arr = []
##        for j in range(n):
##            arr.append(A[i * n + j])
##        M += arr
##    return M
        
##    if n == 1:
##        assert(k == 0 or k == 1)
##        if k == 0:
##            return False
##        else if k == 1:
##            return True
##    a = [True]
##    a.append(genComb(n-1, k-1))
##    b = [False]
##    b.append(genComb(n-1, k))
##    c.append
