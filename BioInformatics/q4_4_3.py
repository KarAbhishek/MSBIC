
def find_subpeptides(string):
    ls = []
    for i in range(len(string)//2):
        rotated_string = string[i:]+string[:i]
        for break_point in range(1, len(rotated_string)):
            ls.append(rotated_string[:break_point])
            ls.append(rotated_string[break_point:])
    return ls

string = 'ELEL'
print(' '.join(sorted(find_subpeptides(), key=len)))