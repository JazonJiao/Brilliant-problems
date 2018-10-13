def find(s):
    m = 0 # global maximum
    c = 1 # current max
    
    for i in range(1, len(s)):
        if ord(s[i]) < ord(s[i-1]):
            if m < c:
                m = c
            c = 1
        else:
            c += 1
    return m

print(find('azcbobobegghakl'))
print(find('woimoepzbjvxfafpyfpzgmxugjodtemcjcpoxobfgbsmokkmcdpmawcwwaxhqwabzdlplvteszqgtkamxjkswkpnzpxpudxcmigz'))
