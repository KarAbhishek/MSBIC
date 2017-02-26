import string
import re
def pares(N, list):
    strin = ''
    for i, grouplen in enumerate(list):
        print(string.ascii_uppercase[i])
        #for j in range(grouplen):
        strin += string.ascii_uppercase[i] + '-'
        print(strin)
        N = N-grouplen
        
    strin = strin[:-1]
    for i in range(N):
        strin += '-'
    
    print('Marker',strin)
    obj = set()
    perm('', strin, obj)
    for i in obj:
        if(re.search('^(-)*(A)+(-)*(B)+$', (i)) != None):
            print(i)


'''def permutations(strin):
    if not strin:
        return ''
    ls= []
    for i, d in enumerate(strin):
        for perm in permutations(strin[:i] + strin[i+1:]):
            #if(re.search('^(-)*(A)+(-)*(B)+$', (d + perm)) != None):
            ls.append(d + perm)
            print(ls)
    return ls'''

def perm(prefix, orig, lst):
    if len(orig) == 0: lst.add(prefix)
    else :
        for i in range(len(orig)):
            perm(prefix+orig[i], orig[0:i]+orig[i+1:], lst)
            
            
t = [2,1]
N = 6
a = pares(N, t)
print(a)