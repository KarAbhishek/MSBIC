
# def find_subpeptides(string):
#     ls = []
#     for i in range(len(string)//2):
#         rotated_string = string[i:]+string[:i]
#         for break_point in range(0, len(rotated_string)):
#             if rotated_string[:break_point] != '':
#                 ls.append(rotated_string[:break_point])
#             if rotated_string[break_point:] != '':
#                 ls.append(rotated_string[break_point:])
#     return ls

def find_subpeptides(string):
    bkp = string
    string += string
    ls=[]

    for i in range(len(string)//2):
        for j in range(1,len(string)//2):
            ls.append(string[i:i+j])
    return ls+[bkp]

if __name__ == '__main__':
    string = 'ELEL'
    print(' '.join(sorted(find_subpeptides(string), key=len)))
    #print(len(find_subpeptides(string)))
