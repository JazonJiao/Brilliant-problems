def pascal(n):
    if n == 1:
        return [1]
    else:
        pas_line = pascal(n - 1)
        line = []
        for i in range(len(pas_line) - 1):
           # sum the the two top adjacent elements
           line.append(pas_line[i] + pas_line[i + 1]) 
        line.insert(0, 1)
        line.append(1)
    return line

print(pascal(23))

# Pascal's Triangle (To Row 1000)
binom = {}
for n in range(0, 1000):
    for k in range(0, n + 1):
        if k == 0 or k == n:
            binom[(n, k)] = 1
        else:
            binom[(n, k)] = binom[(n - 1, k)] + binom[(n - 1, k - 1)]

# Compute Win Probability
def prob(n, p):
    total = 0
    for x in range(0, n):
        total += ((1 - p) ** x) * binom[(n - 1 + x, x)]
    total *= (p ** n)
    return total
