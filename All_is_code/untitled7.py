# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 13:01:01 2016

@author: user
"""

def CountBits(n):
    ls = []
    count = 1
    ls.append(0)
    while(n>0):
        
        if n&1 > 0:
            ls.append(count)
        n = n >> 1
        count += 1
        
    ls[0] = len(ls)-1
    return ls
    
