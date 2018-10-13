def find():
    f = open("D:/2018/CS2201/Brilliant/180813.txt", "r")
    s = f.read()
    A = s.split(', ')
    n = len(A)
    r = 0
    for e in range(n):
        A[e] = int(A[e])
    print(n)
    for i in range(n-1):
        for j in range(i+1, n):
            if abs(A[i] - A[j]) == 70:
                r += 1
    return r

#print(find())

# SAMPLE SOLUTION

with open('D:/2018/CS2201/Brilliant/180813.txt','rb') as numbers:
    exec('List = set( '+numbers.read()+ ')' ) #Extracting the numbers from the file

print(len([ i for i in List if (i+70) in List]))
