def special():
    G = [[False] * 10003 for i in range(10003)]
    f = open("D:/2018/CS2201/Brilliant/180802.txt")
    s = ''
    while True:
        s = f.readline()
        if s == '':
            break
        t = s.split()
        G[int(t[0])][int(t[1])] = True
    for i in range(10003):
        s = 0
        for j in range(10003):
            if G[j][i] == True:
                s += 1
        print(s)
        if s == 214:
            print('214= ', i)
        elif s == 673:
            print('673= ', i)
            

def find(A):
    G = [[] for i in range(10003)]
    r = set()  # IMPORTANT GRAMMAR! use r = {} then it's dictionary
    f = open("D:/2018/CS2201/Brilliant/180802.txt")
    s = ''
    while True:
        s = f.readline()
        if s == '':
            break
        t = s.split()  # automatically split b/w any number of spaces!
        G[int(t[0])].append(int(t[1]))

    for i in A:
        t1 = G[i]
        for j in t1:
            t2 = G[j]
            for k in t2:
                if k != 4394:
                    r.add(k)
        print(len(r))

A = [1, 17, 793, 1200, 3402]
find(A)
#special()


# SAMPLE ANSWER

# import call records
calls = open('2015_march_calls.txt').readlines()[1:]
calls = [[x for x in _.strip().split()] for _ in calls]

# make dict with call partners for each community member
call_dict = {}
for k, v in calls:
    call_dict.setdefault(k, []).append(v)
    call_dict.setdefault(v, []).append(k)

def dfs_hop(G, v, hops_left, reached=None):   
    # initialize our 'reached' list
    if reached is None:
        reached = []
    # append the node under consideration to the `reached` list
    reached.append(v)
    # go through every vertex in the 0-hop neighbor
    # list of current node
    for vertex in G[v]:
    # if the vertex has not been reached, and we have hops left,
    # call depth-first-search on the vertex, and decrement the 
    # number of hops_left by 1
        if vertex not in reached and hops_left >= 0:
            dfs_hop(G, vertex, hops_left - 1, reached)
    # return the list of reached vertices, unique by construction
    return reached

dfs_hop(call_dict, v, 2)
