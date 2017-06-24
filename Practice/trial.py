import sys


num = 5
mask = 1
while num != 0:
    mask <<= 1
    num >>= 1
print(bin(mask))
all_1 = mask - 1

true_mask = ~all_1
print(bin(true_mask))
compl = ~(true_mask | num) ^ (1 << sys.getsizeof(-1))
print(bin(1 << sys.getsizeof(-1)))
print(bin(compl))
