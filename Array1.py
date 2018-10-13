def average(A):
    l = len(A)
    s = 0
    for i in A:
        if i > 20:
            i = 20
        s = s + i
    return s / l

print(average({12, 10, 8, 36, 12, 10, 0, 20, 0, 2}))
print(average({28, 29, 11, 29, 2, 6, 4, 7, 13, 32}))
print(average([21, 32, 32, 12, 31, 20, 16, 6, 7, 11]))
print(average([32, 36, 17, 5, 10, 30, 20, 7, 33, 11]))
print(average([28, 10, 21, 8, 15, 15, 38, 30, 13, 4]))
print(average([16, 25, 15, 35, 4, 14, 22, 22, 39, 17]))
print(average([18, 5, 11, 6, 34, 8, 21, 3, 19, 22]))
print(average([1, 15, 38, 33, 17, 1, 3, 25, 22, 0]))
print(average([31, 1, 6, 2, 2, 14, 37, 27, 14, 14]))
print(average([2, 16, 2, 18, 16, 28, 25, 30, 8, 23]))
