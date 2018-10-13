def find1(A):
    lim = 2 ** 15
    for i in range(0, lim):
        s = 0
        for j in range(0, 15):
            if (i // (2 ** j)) % 2 == 1:
                s = s + A[j]
        if s == 316:
            return True
    return False

def find(A):
    for i in range(0, 15):
        for j in range(i+1, 15):
            s = 0
            for k in range(i, j):
                s = s + A[k]
                if s == 316:
                    return True
    return False
                

B = [61, 6, 39, 29, 30, 72, 98, 36, 42, 66, 24, 58, 13, 16, 73]
C = [87, 78, 4, 10, 48, 43, 33, 70, 21, 18, 75, 66, 39, 80, 87]
D = [82, 72, 39, 67, 65, 93, 28, 2, 89, 39, 68, 29, 61, 14, 98]
E = [45, 5, 14, 75, 100, 37, 98, 64, 90, 52, 66, 30, 18, 89, 19]

print(find(B))
print(find(C))
print(find(D))
print(find(E))

## EXAMPLE O(N) SOLUTION BY BRILLIANT

def Cts_Efficient(List,k):
    Cumulative = 0
    i = 0
    Start = 0
    for i in range(len(List)):
        Integer = List[i]
        Cumulative += Integer
        while (Cumulative > k and Start < i - 1):
            Cumulative = Cumulative - List[Start]
            Start += 1
        if Cumulative == k:
            return True
    return False

Choices = [
    [61, 6, 39, 29, 30, 72, 98, 36, 42, 66, 24, 58, 13, 16, 73],
    [87, 78, 4, 10, 48, 43, 33, 70, 21, 18, 75, 66, 39, 80, 87],
    [82, 72, 39, 67, 65, 93, 28, 2, 89, 39, 68, 29, 61, 14, 98],
    [45, 5, 14, 75, 100, 37, 98, 64, 90, 52, 66, 30, 18, 89, 19]
]

for choice in Choices:
    if Cts_Efficient(choice,316):
        print(choice)
