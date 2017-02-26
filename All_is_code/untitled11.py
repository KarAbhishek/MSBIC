# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 05:43:18 2016
@author: Abhishek
"""

def mein(N, groups):
    start = []
    end = []
    startIndex = 0
    endIndex = N-1
    for groupSize in groups:
        start.append(startIndex)
        startIndex+=groupSize
    for groupSize in reversed(groups):
        end.append(endIndex)
        endIndex-=groupSize
    end.reverse()
    #print(start, end)
    for i in recurse(0, start, end, groups):
        print(i)
        
    
def recurse(index, start, end, groups):
    flag = True
    for i in range(len(start) - 1):
        if(start[i+1] < start[i] + groups[i] + 1):
            flag = False
    if flag:    yield start
    for j in reversed(range(index, len(end))):
        if end[j] > start[j]:
            start[j] += 1
            for i in recurse(j,start,end, groups):
                yield i
            start[j] -= 1

mein(10, [2, 1, 1])