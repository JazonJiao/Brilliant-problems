def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

def Comb(n, k):
    return fact(n) / (fact(k)*fact(n-k))

s = 0
for i in range(10):
    c = Comb(10, i)
    s += c*((1/3)**i)*((2/3)**(10-i))*i*(10-i)
    print(s)

print(s)
