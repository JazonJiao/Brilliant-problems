def find(s):
    r = 0
    n = len(s)
    for i in range(n-1):
        for j in range(i+1, n):
            m = int(s[i : j])
            if m % 3 == 0:
                r += 1
    return r

print(find('6781234967'))
