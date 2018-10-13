def find(A):
    result = []
    for i in A:
        for j in A:
            for k in A:
                if valid(i, j, k):
                    result.append([i,j,k])
    return len(result)/6

def valid(a, b, c):
    if a == b or a == c or b == c:
        return False
    if a[0] == b[0] == c[0]:
        return False
    elif b[0] == a[0] or c[0] == b[0] or a[0] == c[0]:
        return True
    # three points are on the same line
    if (b[1] - a[1])/(b[0] - a[0]) == (c[1] - b[1])/(c[0] - b[0]):
        return False
    return True

def generate():
    result = []
    for i in range(4):
        for j in range(5):
            result += [(i,j)]
    return result

A = generate()
print(find(A))
