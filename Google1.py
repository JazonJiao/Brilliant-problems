# Code Jam Kickstart; Sept 13, 2018
def solve():
    f = open("D:/2018/Brilliant/180913.txt", "r")
    t = int(input())
    for i in range(1, t+1):
        n = int(input())
        arr = [int(e) for e in input().split()]
        A = []
        B = []
        for j in range(0, n):
            A.append(arr[2*j])
            B.append(arr[2*j+1])
        p = int(input())
        P = [0] * p
        for j in range(0, p):
            c = int(input())
            for k in range(0, n):
                if c in range(A[k], B[k]+1):
                    P[j] += 1
        print("Case #", end = "")
        print(i, end = "")
        print(": ", end = "")
        for j in range(0, p):
            print(P[j], end = " ")
        print()
    
solve()
