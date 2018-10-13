A = {'ka':'a','zu':'b','mi':'c','te':'d','ku':'e','lu':'f','ji':'g','ri':'h','ki':'i','zu':'j','me':'k','ta':'l','rin':'m','to':'n','mo':'o','no':'p','ke':'q','shi':'r','ari':'s','chi':'t','do':'u','ru':'v','mei':'w','na':'x','fu':'y','zi':'z'}

def find(s):
    arr = s.split('~')
    for b in arr:
        print(A[b])



s = 'chi~ri~ku~ka~to~ari~mei~ku~shi~chi~mo~chi~ri~ki~ari~no~shi~mo~zu~ta~ku~rin~ki~ari~ari~ki~na~te~ki~ru~ki~te~ku~te~zu~fu~ri~ka~ta~lu'
print(find(s))
