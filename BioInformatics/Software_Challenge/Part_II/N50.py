def N(statistic, lis):
    threshold = (statistic * sum(lis))/100
    sum_i = 0
    for i in lis[::-1]:
        sum_i += i
        if sum_i >= threshold:
            return i
    return 0


if __name__ == '__main__':
    print(N(50, [20, 20, 30, 30, 60, 60, 80, 100, 200]))