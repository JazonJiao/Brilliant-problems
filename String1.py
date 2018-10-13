def Cipher(s, n):
    ''' return the shifted string, s, based on number of chars shifted, n'''
    result = ''
    for t in s:
        if not t.isspace():
            m = ord(t)+n
            if m > ord('z'):
                m -= 26
            if m < ord('a'):
                m += 26
            result += chr(m)
        else:
            result += ' '
    return result

s = 'qafqx rbxfy fsb oc fzq oacsqx'

for i in range(-26, 0):
    print(Cipher(s, i))

