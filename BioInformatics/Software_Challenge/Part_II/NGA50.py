from BioInformatics.Software_Challenge.Part_II.NG50 import NG
def NGA(statistic, lis, genome_length, break_points):
    for break_point in break_points:
        for idx, i in enumerate(lis):
            if break_point[0] == i:
                del lis[idx]
                lis+=break_point[1]
    lis.sort()
    return NG(statistic, lis, genome_length)


if __name__ == '__main__':
    print(NGA(50, [20, 20, 30, 30, 60, 60, 80, 100, 200], 1000, [[100, [50, 50]]]))