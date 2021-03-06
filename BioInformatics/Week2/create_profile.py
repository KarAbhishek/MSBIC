def create_profile(motif):
    hm = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    l = [[0 for x in range(len(motif[0]))] for y in range(4)]
    for i in range(len(motif[0])):
        #hm = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for x in range(len(motif)):
            l[hm[motif[x][i]]][i] += 1.0/len(motif)
    return l

print(create_profile(['AAC', 'CGT','ACT','TTT']))
#<class 'list'>: [[0.241, 0.205, 0.253, 0.217, 0.277, 0.229, 0.265, 0.205, 0.313, 0.289, 0.289, 0.241], [0.241, 0.325, 0.253, 0.253, 0.217, 0.277, 0.193, 0.277, 0.277, 0.277, 0.289, 0.193], [0.301, 0.217, 0.205, 0.289, 0.229, 0.253, 0.277, 0.193, 0.193, 0.229, 0.253, 0.289], [0.217, 0.253, 0.289, 0.241, 0.277, 0.241, 0.265, 0.325, 0.217, 0.205, 0.169, 0.277]]