# given an array that has the same elements except one small element,
# determine the small element in log_3(n) time, return its value

def find(A):
    L = len(A)
    L1 = L // 3
    L2 = 2 * L1
    a1 = A[: L1]
    a2 = A[L1 : L2]
    a3 = A[L2 :]
    s1 = sum(a1)
    s2 = sum(a2)
    s3 = sum(a3)
    if s1 < s2:
        
