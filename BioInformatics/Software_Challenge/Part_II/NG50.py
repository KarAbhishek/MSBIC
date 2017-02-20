def NG(statistic, lis, genome_length):
    threshold = (statistic * genome_length)/100
    sum_i = 0
    for i in lis[::-1]:
        sum_i += i
        if sum_i >= threshold:
            return i
    return 0

if __name__ == '__main__':
    print(NG(50, [20, 20, 30, 30, 50, 50 ,60, 60, 80, 200], 1000))