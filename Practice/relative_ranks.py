from operator import itemgetter
# Input: [1, 2, 4, 5, 3]
# Output: [5, 4, 2, 1, 3]
arr = [1, 2, 4, 5, 3]
arr_2d = [[idx, i] for idx, i in enumerate(arr)]
import numpy as np
print(np.array(arr_2d))
arr_2d.sort(key=itemgetter(1), reverse=True)
res = [i for i, _ in arr_2d]
print(np.array(arr_2d))