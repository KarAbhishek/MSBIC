

file = open('input_1.txt')
lines = file.read().splitlines()
strin = lines[0]
filter_list = lines[1:]
ls = []
for idx in range(len(strin)):
    k_mer = strin[idx:idx+len(filter_list[0])]
    if k_mer in filter_list:
        ls.append(idx)

print(' '.join(map(str, ls)))



# file = open('input_1.txt')
# lines = file.read().splitlines()
# strin = lines[0]
# filter_list = lines[1:]
# ls = []
# k_mer_list = []
# for idx in range(len(strin)):
#     k_mer_list.append(strin[idx:idx+len(filter_list[0])])
#
#
# for k_mer in filter_list:
#     try:
#         ls.append(k_mer_list.index(k_mer))
#     except ValueError:
#         pass
#
# print(' '.join(map(str, ls)))