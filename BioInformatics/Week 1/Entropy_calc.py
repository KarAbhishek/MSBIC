import numpy as np

def entropy_calc(prob):
    return -prob * np.log2(prob)

ls = {}
# ls.append(entropy_calc(0.7)+entropy_calc(0.2)+entropy_calc(0.1))
# ls.append(entropy_calc(0.6)+entropy_calc(0.2)+entropy_calc(0.2))
# ls.append(entropy_calc(1))
# ls.append(entropy_calc(1))
# ls.append(entropy_calc(0.9)+entropy_calc(0.1))
# ls.append(entropy_calc(0.9)+entropy_calc(0.1))
# ls.append(entropy_calc(0.9)+entropy_calc(0.1))
# ls.append(entropy_calc(0.5)+entropy_calc(0.4)+entropy_calc(0.1))
# ls.append(entropy_calc(0.8)+entropy_calc(0.1)+entropy_calc(0.1))
# ls.append(entropy_calc(0.7)+entropy_calc(0.2)+entropy_calc(0.1))
# ls.append(entropy_calc(0.4)+entropy_calc(0.3)+entropy_calc(0.3))
# ls.append(entropy_calc(0.6)+entropy_calc(0.4))
ls['(A:0.25, C:0.25, G:0.25, T:0.25)'] = (entropy_calc(0.25)+entropy_calc(0.25)+entropy_calc(0.25)+entropy_calc(0.25))
ls['(A:0.3, C:0.2, G:0.3, T:0.2)'] = (entropy_calc(0.3)+entropy_calc(0.2)+entropy_calc(0.3)+entropy_calc(0.2))
ls['(A:0, C:1, G:0, T:0)'] = (entropy_calc(1))
ls['(A:0.2, C:0, G:0, T:0.8)'] = (entropy_calc(0.8)+entropy_calc(0.2))
ls['(A:0, C:0, G:0.5, T:0.5)'] = (entropy_calc(0.5)+entropy_calc(0.5))
#print({ls[key]:key for key in ls})

ls1 = {ls[key]: key for key in ls}
for key in sorted(ls1.keys()):
    print("%s: %s" % (key, ls1[key]))
