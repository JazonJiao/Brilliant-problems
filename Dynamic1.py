# the backpack problem, Aug 1, 2018

# pre: A is an array of 2-tuples where the 1st entry is weight
#      and 2nd entry is value; m is the maximum weight.
def backpack(A, m):
    n = len(A)
    # create an (m+1) * (n+1) array; cannot use W = [[0] * (m+1)] * (n+1),
    # or else W[0][0] = a will assign all W[i][0] to a
    W = []
    x = [0] * (m+1)
    for k in range(n+1):
        y = x.copy()
        W += [y]
    
    for i in range(1, n+1):
        weight = A[i-1][0]
        value = A[i-1][1]
        for j in range(m+1):
            if weight > j:
                W[i][j] = W[i-1][j]
            else:
                W[i][j] = max(W[i-1][j], W[i-1][j-weight] + value)
    return W



A = [(3,25),(2,20),(1,15),(4,40),(5,50),(9,55),(6,45),(7,58)]
w = [3,2,1,4,5,9,6,7]

#print(backpack(A,12))

# SAMPLE ANSWER

# v = list of item values or profit
# w = list of item weight or cost
# W = max weight or max cost for the knapsack
def Knapsack(v, w, W):
    # c is the cost matrix
    t = []
    n = len(v)
    # There are N+1 rows because we need to account for the possibility
    # of choosing from 0 up to and including N possible items.
    # There are W+1 columns because we need to account for possible
    # "running capacities" from 0 up to and including the maximum weight W.
    t = [[0] * (W + 1) for i in range(n + 1)]

    for i in range(0,n):
        for j in range(0,W+1):      
            if (w[i] > j):
                t[i][j] = t[i-1][j]
            else:
                t[i][j] = max(t[i-1][j],v[i] +t[i-1][j-w[i]])
    return t[n-1][W]

def getUsedItems(w, t):
    # item count
    i = len(t)-1
    currentW =  len(t[0])-1
    # set everything to not marked
    marked = []
    for j in range(i):
        marked.append(0)            
    while (i >= 0 and currentW >=0):
        if (i==0 and t[i][currentW] >0 )or t[i][currentW] != t[i-1][currentW]:
            marked[i] =1
            currentW = currentW-w[i]
        i = i-1
    return marked

print(getUsedItems(w, backpack(A,12)))

