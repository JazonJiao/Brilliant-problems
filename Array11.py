'''https://brilliant.org/practice/abstract-data-types-level-3-challenges/?subtopic=types-and-data-structures&chapter=abstract-data-types'''
# 2018-08-12

def holes(P, A):
    '''given the number of people and an array of hole sizes,
       return the output sequence'''
    for n in A:
        H = P[n-1 :: -1]  # CAUTION: P[n-1:0:-1] will omit the first element
        P = P[n : ] + H
    return P

def hole(P, A):
    '''given output, return the input sequence of people'''
    p = len(P)
    for i in range(len(A)-1, -1, -1):
        n = A[i]
        #P = P[p-1 : p-1-n : -1] + P[ : p-n]
        P = P[p-1 : p-n : -1] + [P[p-n]] + P[ : p-n]
    return P
# WARNING: WHEN INDEX IS -1, IT REPRESENTS THE LAST ELEMENT


P = [p for p in range(1,9+1)]  # sequence of people

A = [3, 5, 9, 8, 5, 1, 8, 5, 4, 5, 3, 8, 6, 7, 2,
     6, 3, 9, 2, 5, 2, 7, 8, 6, 7, 3, 6, 9, 2, 5]

B = [3, 5, 2]

print(hole([p for p in range(1,6+1)], B))
print(hole([q for q in range(1,9+1)], A))


# SAMPLE SOLUTION
def holes_hard(people, holes):  # people can be either a list or a string, holes is a list
    for hole in holes[::-1]:
        people = people[-hole:][::-1] + people[:-hole]
    return people

