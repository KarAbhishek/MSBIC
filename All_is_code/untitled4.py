# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 20:50:15 2016

@author: user
"""

def unique(str, str1):
    st=[]
    st1=[]
    for char in str:
        st.append(char.lower())
        print(st.sort())
    for char in str1:
        st1.append(char.lower())
        print(st1.sort())
    if st==st1:
        print('Yes')
    else:
        print('No')
        
def urlify(str):
    return str.replace(' ', '%20')

def palindromePerm(str, orig):
    if orig in str+str:
        return True
    else:
        return False
        
#def zeromatrix(a):
    
    
def strCompr(a):
    prev = ''
    count = 1
    for s in a:
        if s==prev:
            count += 1
        else:
            count = 1
            prev = s
            print(prev+str(count))
    
#print(unique("Chuc", "hucc"))
#print(urlify('html mofoa'))
#print(palindromePerm("tlewaterbo","waterbottle"))
print(strCompr('aaaabbcc'))
