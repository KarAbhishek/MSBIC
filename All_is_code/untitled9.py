# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 21:03:49 2016

@author: user
"""

def func():
    print(d)
    return
    
def main():
    global d
    d = 12
    print(d)
    
main()
d=1
print(d)
func()