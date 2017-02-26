'''def mein():
    lst =[]  
    perm('', 'Permute', lst)
    print(len(lst))
	
def perm(prefix, orig, lst):
    if len(orig) == 0: lst.append(prefix)
    else :
        for i in range(len(orig)):
            perm(prefix+orig[i], orig[0:i]+orig[i+1:], lst)'''
import string
   
def mein():
    #OriginalList = 'OriginalList'
    recurse('ssss', 0, 0, 4, 0, string.ascii_lowercase, 0, '')
    #for elem in gtSomething:   
     #   print(elem)
   
def recurse(prefix, lengthOfBead, lengthOfGap, totalLength, index, low, pick, prev):
    if(lengthOfBead + lengthOfGap == totalLength): 
        print('Bead:', lengthOfBead,' Gap:', lengthOfGap)       
        print(prefix)
        prefix =''
    if(lengthOfBead > totalLength or lengthOfGap > totalLength): return
    #if(lengthOfBead + lengthOfGap > totalLength): return;

    
    prefix = prefix[0:index]+low[pick]+prefix[index+1:]
    recurse(prefix, lengthOfBead+1, lengthOfGap, totalLength, index+1, low, pick, 'A')
    
    #pick +=1
    if prev == 'G':    
        pick +=1   
    prefix = prefix[0:index]+'G'+prefix[index+1:]
    recurse(prefix, lengthOfBead, lengthOfGap+1, totalLength, index+1, low, pick, 'G')    
     
    
mein()