def bitToDecimal(bnary):
    #sumT = bnary[-1]
    sumT = 0
    for idx, i in enumerate(bnary[::-1]):
        #print(i)
        sumT += 2**idx * int(i)

    return sumT

def decimal_to_bit(dec):
    sum =''
    if dec ==0: return '0'
    while(dec!=0):
        sum += str(dec%2)
        dec //= 2
    return sum[::-1]


def findSubString(bary, k):
    #k = 4
    decim_String = bitToDecimal(bnary=bary)
    l = len('101')
    decim_len = k - l
    found_count = 0
    for i in range(2**k):
        while decim_len >= 0:
            mask = (1 << k) - (1 << (k-decim_len))
            if mask & i == 0:
                found_count += 1
                break
            decim_String <<= 1
            decim_len -= 1
    return found_count

def find_substring(bnary, k):
    #bnary = '01'
    lim = k - len(bnary)
    bnary_dec = bitToDecimal(bnary)
    found_count = 0
    for i in range(2**k):
        bkp_bnary = bnary_dec
        limiter = lim
        #print(decimal_to_bit(i),'    Limiter: ', limiter)
        while limiter > 0:
            print('bkp_bnary & i : ', decimal_to_bit(bkp_bnary), decimal_to_bit(i))
            if bkp_bnary & i != 0:
                found_count += 1
                break
            bkp_bnary <<= 1
            limiter -= 1

    return found_count

print(find_substring('01', 4))
