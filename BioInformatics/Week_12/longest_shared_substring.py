import sys
import numpy as np
def dp_change(money, coins):
    min_coins = [0] + [float('inf') for i in range(1, money+1)]
    for i in range(1, money+1):
        for j in range(len(coins)):
            if i >= coins[j]:
                if min_coins[i-coins[j]]+1 < min_coins[i]:
                    min_coins[i] = min_coins[i-coins[j]] + 1
    print(min_coins[money])

# def dp_change_main(money,coins):
#     dp_change_main(money, coins, 0)
#
# def dp_change_1(moneyleft, denominations, count):
#     if moneyleft <= 0:
#         return
#     for i in denominations:
#         dp_change(moneyleft-i, count+1)

def manhattan_problem(n, m, down, right):
    s = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(1, n+1):
        s[i][0] = s[i-1][0] + down[i-1][0]
    for j in range(1, m+1):
        s[0][j] = s[0][j-1] + right[0][j-1]
    for i in range(1, n+1):
        for j in range(1, m+1):
            s[i][j] = max(s[i - 1][j] + down[i-1][j], s[i][j - 1] + right[i][j-1])
    return s[n][m]


# def output_lcs(str1, str2, i, j):
#     if i == 0 or j == 0:
#         return 0
#     if str1[i-1] == str2[j-1]:
#     return 1+output_lcs(str1, str2, i-1, j-1)
#     else:
#         #print(ans[i-1], str1[i - 1])
#         return max(output_lcs(str1, str2, i, j-1), output_lcs(str1, str2, i-1, j))


# def output_lcs(str1, str2):
#     str_matrix = [0 for i in str1]
#     for idx in range(len(str2)):
#         nxt_row = [0]
#         if str1 == str2:
#             if str_matrix[idx-1][idx-1]+1 > max_lcs:
#                 max_lcs = str_matrix[idx-1][idx-1]+1
#             nxt_row.append()

def LCS_backtrack(v, w):
    s = [[-1 for i in range(len(w) + 1)] for j in range(len(v) + 1)]
    max_s = [float('-inf'), -1]
    backtrack = [['N' for i in range(len(w) + 1)] for j in range(len(v) + 1)]
    for i in range(len(v) + 1):
        s[i][0] = 0
    for j in range(len(w) + 1):
        s[0][j] = 0
    for i in range(1, len(v) + 1):
        for j in range(1, len(w) + 1):
            s[i][j] = s[i - 1][j - 1] + 1 if v[i - 1] == w[j - 1] else 0
            # if s[i][j] == s[i - 1][j]:
            #     backtrack[i][j] = 'D'
            # elif s[i][j] == s[i][j - 1]:
            #     backtrack[i][j] = 'R'
            # elif s[i][j] == s[i - 1][j - 1] + 1 and v[i - 1] == w[j - 1]:
            #     backtrack[i][j] = 'C'
            if max_s[0] < s[i][j]:
                max_s = [s[i][j], i]


    return v[max_s[1]-max_s[0] : max_s[1]]

def output_lcs(backtrack, v, i, j):
    if i == 0 and j == 0:
        return
    if backtrack[i][j] == 'D':
        output_lcs(backtrack, v, i - 1, j)
    elif backtrack[i][j] == 'R':
        output_lcs(backtrack, v, i, j - 1)
    elif backtrack[i][j] == 'C':
        output_lcs(backtrack, v, i - 1, j - 1)
        print(v[i - 1], end='')


# dp_change(16810,
# list(map(int, '24,21,14,8,5,3,1'.split(','))))
sys.setrecursionlimit(2000)
str1 = 'GTTTGGAAGGCGCGTATTATCAACTCCCCTTCTGCCAAGAATAGCACACCATTGGTGGTCTCCATTGTGGGGGTCCTAAAGTCAGATCGAGCTCCACGAGGGCACTAGCTAAGCGCGGGACATAGACAACCGTGCCTCCTTGTATACAGCCCCTAAGACTTGCACATCGATACAGTAATAAGCTGATACTGGATACTCTTGGTCACCAGTCCTGGGACGGTGGCGGTGTGCCCTTCTAGGTCGGAATAAGGCTAAATCGACCAGTCATGGGACGCACACACGGATTTATAGACGGCCGTGTCCCGTTACGCCTACTCCAAATAAGTACCTGGAGTCCTCTGGCAACACTGGTACTATTTAGACACGACAAAGTACACAGCGGGAGGACCCAACCGAGCAATGCGTAAGCCTCAAAAACCTACGATACTTTGGCACGGCAGGAATCGGTTGCCGACTACTGCAAACGAATGAGCACAACTACAGAAGCTTTCTGACCCAATAAGATGCCACTATGCCCCACTCGCATCGGTAGTAAACTACTTTGGCATTAGCGGTCAAGGCGATTCCTCAAGTAAGTGAATTTGACTAGCACGGCGGCGTCGTAAATAGTCTCGTGGTGAGCTTCAAGCATCTGCATATGTAACTCATGGCCATGACAGCCGACAATTCACCTTTCCCCTCCCCTTATAGAGACAAAGCGGTGCGTGTTCATAGTGCCGTCAACAACCAATACGATTATGCCTTCTTCCTAGTACGCCTATCTAGATTAGTGGATTTCTGGGTTCCATCAACCCTCCGAGTTATGGGAACTTTCTGACGCTCGAACTGGTCATAGCACAAGGGCAGATCGCCTCTACCGTCCACTACGCCGTTACACCGCTAGGTCTATTCTGCGCACGACCACGTTTTGTATGCCACTAAAAGTGACAGCGTCTCCGAGTCAGGAGCTGCTGACTGAAAGCTTCGAGATACACAATGAAAGCCCACGGCACGCACACTG'
str2 = 'TTTTGCCAGTGCAGGCTGGTGACAGATTAACGAAAGGTAGCTTCCCCGTCACGGCCGTCATGCATAGCATTGGCCAGGGGGTGGTAGAGCCAAAGGCCGTCGACGCGGCGTATACCCGAAGTACCCGGCAAGATGATTAACGGAGTTCCCGGACGACGCATTATCTCCAATGATGTTATCCCAGTCATAATGAAATGGTCGACTACACGGGTAGAAAAAAGCACAACCCGTAGCGACGGGCATTCCGCGCAGGAGTGTACCGTCTCCTTACGTTATAGTTTACTGCAGAGCTAGCGGACATTATACCTTCGTCGCGTAAGAACTTTCGGCCGGGCGGACTTTAATCTATTCGACATACGCCTGGAACGGGGGCATAGCCACTTGGCTGACTTGGAAAGAGACCCGTCTACCCCTTGCCGCAGGGGCACGCTTGTTGAAATGTCAAGAACAGTCTCGGGGAATTACGGGTCCTCGCGACAGGAATGCCTGAGATCCGGTTTTATCCGACTCTACGTGGTGTGGTGTTCTCATATACACAACGCCGTAGGTGGCCAATTCAGACTGCTCAGATAACAGGATCGGAAAACGCGTTGACTAAAGCAGTTTCGATATGAGTTTCGTCCCCGCTCTCCGGCTCGTTAAAATGACGGGACCTTATAATAGAGTGTCCGCAGCGGGCTTCCAGGCAACTCATGCTTTGGGACGCGCCCTATTAGATCGAAGTTAGCTGAGTTGGAGAAGAGAGTCAAATTGAAAGCGCGCTGACATCGCTACCAGACTTTTACGCGTCTGGACTCTCGACCTCGGGGCTTCCAGCAAGGCTTGCGCTTCTAGTACTTAGGGGTTCTCAGGCGCAAAATAAGCCCTACCGAATACTCCAAGTCTACATTACTTGTACAGCAAACGCGCGTAACAAGGCCACGGCGGCTAAATGTGTGACCTATCCGGGATACGACCAGTCCCCTCCCACACCATTCTGGATTCGAGCAGTCGTCCGTAG'
z = LCS_backtrack(str1, str2)
print(z)
#output_lcs(z, str1, len(str1), len(str2))
# file = open('man_hat_data')
# lines = file.read().splitlines()
# n = int(lines[0].split(' ')[0])
# m = int(lines[0].split(' ')[1])
# down = [list(map(int,single_line.split(' '))) for single_line in lines[1:n+1]]
# right = [list(map(int,single_line.split(' '))) for single_line in lines[n+2:]]
# print(manhattan_problem(n, m, down, right))