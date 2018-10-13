# https://brilliant.org/practice/strings-intermediate/?p=3

def cipher(s):
    na = ord('a')
    s1 = 'the quick brown fox jumps over the lazy dog'
    s2 = 'fzq kpgwj vxbsa rbh lpnic bdqx fzq uomy ebt'
    table = [0]*26
    for i in range(len(s1)):
        if s1[i].isspace():
            continue
        n2 = ord(s2[i]) - na
        n1 = ord(s1[i])
        table[n2] = n1
    print(table)
    r = ''
    for ch in s:
        if ch.isspace():
            r += ' '
            continue
        nc = ord(ch) - na
        r += chr(table[nc])
    return r

print(cipher('qafqx rbxfy fsb oc fzq oacsqx'))

# SAMPLE ANSWER

def build_map(encrypted, decrypted):
    encryption_map = {}
    for i in range(0, len(encrypted)):
        encryption_map[encrypted[i]] = decrypted[i]
    print(encryption_map)
    return encryption_map

def enc_dec(encrypted, encryption_map):
    new = ''
    for i in encrypted:
        new += encryption_map[i]
    return new

m = build_map('fzq kpgwj vxbsa rbh lpnic bdqx fzq uomy ebt',
              'the quick brown fox jumps over the lazy dog')

print(enc_dec('qafqx rbxfy fsb oc fzq oacsqx', m))
# outputs "enter forty two as the answer"


def buildmap():
    na = ord('a')
    nz = ord('z')
    mp = {}
    mp[' '] = ' '
    for i in range(26):
        mp[chr(na+i)] = chr(nz-i)
    print(mp)
    return mp

m = buildmap()
print(enc_dec('r zn z yiroorzmg uzm', m))
