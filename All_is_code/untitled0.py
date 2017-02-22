# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 06:02:55 2016

@author: user
"""

def solution(A, D):
    q = [0] * D;
    i = 0
    A.append(-1)
    A.insert(0, 0)
    dp = [0] * len(A)
    dp[:D - 1] = A[:D - 1]
    for i in range(D - 1):
        while q and dp[i] <= dp[q[-1]]:
            q.pop()
        q.append(i)
    for i in range(D - 1, len(dp)):
    
        dp[i] = max(dp[q[0]], A[i])
        while q and q[0] <= i - D:
            q.pop(0)
        while q and dp[i] <= dp[q[-1]]:
            q.pop()
        q.append(i)
        #print dp
    return dp[-1]

print (solution([1,-1,0,2,3,5], 3))
print (solution([-1,-1,-1,3], 3))
print (solution([2,3,1,4],3))