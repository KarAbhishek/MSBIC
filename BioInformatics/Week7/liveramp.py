def get_pad(n):
    strin = ''
    while n != 0:
        strin += '0'
        n //= 2
    return strin


def get_binary_string(n, pad):
    ls= []
    while n != 0:
        ls.append(str(n % 2))
        n //= 2
    ret = ''.join(ls[::-1])
    padder = lambda x: pad[:len(pad) - len(ret)]+x
    print(padder(ret))
    return ret


def find_largest_time(num_list):
    pad = get_pad(len(num_list) - 1)

    for comb_mnemonic in range(2**len(num_list)):
        bin_str = get_binary_string(comb_mnemonic, pad)
        counter = 0
        while comb_mnemonic != 0:
            ultimate_list = []
            if comb_mnemonic & 1 == 1:
                ultimate_list.append(num_list[counter])

            counter += 1
            comb_mnemonic >>= 1
        #[idx for idx, i in enumerate(num_list) if bin_str[idx] == '1']


# def largest_time(num_list):
#     maxnum = float('-inf')
#     for i in num_list:
#         for j in num_list:
#             for k in num_list:
#                 for l in num_list:
#                     if i in range(3) and j in range(10) and k in range(7) and k in range(10):
#                         num = 1000*i + 100*j + 10 * k+ l
#                         if num > maxnum and num <= 2400:
#                             maxnum = num
#                             print(str(i)+str(j)+':'+str(k)+str(l))

def find_largest_time(num_string):
    num_perm = []
    permutations(num_string, num_perm)

    maxnum = float('-inf')
    for n in num_perm:
        new_num = int(n)
        # for i in n:
        #     new_num = new_num*10 + int(i)

        if maxnum < new_num <= 2400:
            i = int(n[0])
            j = int(n[1])
            k = int(n[2])
            l = int(n[3])
            if i in range(3) and j in range(10) and k in range(7) and k in range(10):
                maxnum = new_num
                print(str(i)+str(j)+':'+str(k)+str(l))



def permutations(string, ls, prefix=''):
    if string == '':
        ls.append(prefix)
    for i in range(len(string)):
        permutations(string[:i] + string[i+1:], ls, string[i]+prefix)

#get_pad(16)
inputted = [2,5,9,3]
find_largest_time(''.join(map(str, inputted)))
#permutations('ABCD')