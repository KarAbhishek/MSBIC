from copy import deepcopy
def de_bruijn(k, n):
    """
    De Bruijn sequence for alphabet k
    and subsequences of length n.
    """
    try:
        # let's see if k can be cast to an integer;
        # if so, make our alphabet a list
        _ = int(k)
        alphabet = list(map(str, range(k)))

    except (ValueError, TypeError):
        alphabet = k
        k = len(k)

    a = [0] * k * n
    sequence = []

    def db(t, p):
        if t > n:
            if n % p == 0:
                sequence.extend(a[1:p + 1])
        else:
            a[t] = a[t - p]
            db(t + 1, p)
            for j in range(a[t - p] + 1, k):
                a[t] = j
                db(t + 1, t)
    db(1, 1)
    return "".join(alphabet[i] for i in sequence)

def subpeptides(peptide):
    l = len(peptide)
    looped = peptide + peptide
    for start in range(0, l):
        for length in range(1, l):
            print(looped[start:start+length])

def subpep(n):
    return n * (n + 1) / 2 + 1

def subpep1(n):
    return n * (n-1)

#print(subpep1(31315))
#subpeptides("ABC")

#print(de_bruijn(2, 8))
#print(de_bruijn("abcd", 2))




infile = open('AA_MassTablet.txt', 'r')
aa = {}
for line in infile:
    aa[line[0]] = line[2:].strip('\n')
infile.close()

# Ideal experimental spectrum
SpectrumIdealTemp = '0 71 97 99 101 101 113 114 129 131 163 186 202 202 211 227 228 230 230 234 260 287 299 301 324 329 331 331 359 365 374 388 400 413 430 430 445 460 462 464 487 501 510 514 517 531 558 561 561 576 593 611 615 616 630 632 673 675 689 690 694 712 729 744 744 747 774 788 791 795 804 818 841 843 845 860 875 875 892 905 917 931 940 946 974 974 976 981 1004 1006 1018 1045 1071 1075 1075 1077 1078 1094 1103 1103 1119 1142 1174 1176 1191 1192 1204 1204 1206 1208 1234 1305'
SpectrumIdealTemp = '0 71 101 115 115 128 147 147 163 216 218 229 230 234 275 278 294 331 344 349 365 376 381 393 422 459 464 491 493 494 496 523 528 565 594 606 611 622 638 643 656 693 709 712 753 757 758 769 771 824 840 840 859 872 872 886 916 987'
SpectrumIdeal = SpectrumIdealTemp.split()


def LinearSpectrum(peptide):
    # Find the linear spectrum of the peptide
    peptides = []
    sizes = ['0']
    peptides.append(peptide)
    n = len(peptide)
    for window in range(1, n):
        for i in range(0, n - window + 1):
            peptides.append(peptide[i:i + window])
    for string in peptides:
        total = 0
        for aminoacid in string:
            total += int(aa[aminoacid])
        sizes.append(str(total))
    return sizes


def CheckCompatibility(SpectrumCheck, SpectrumIdeal):
    # Check compatibility with the ideal spectrum
    temp = deepcopy(SpectrumIdeal)
    compatibility = True
    for SpecProt in SpectrumCheck:
        present = 0
        for SpecNum in temp:
            if SpecProt == SpecNum:
                present = 1
        if present == 1:
            temp.remove(SpecProt)
        if present == 0:
            compatibility = False
            return compatibility
    return compatibility


def FindMass(spectrum):
    temp = []
    for num in spectrum:
        temp.append(int(num))
    temp = sorted(temp)
    return temp[len(temp) - 1]


def IdealSequencing(SpectrumIdeal):
    # Find correct mass of the ideal spectrum
    CorrectMass = FindMass(SpectrumIdeal)

    Combos = []  # Store potential peptides
    Correct = []  # Store correct peptides
    for letter in aa:
        Combos.append(letter)

    # Recursive method for building and checking peptides
    while len(Combos) != 0:
        for string in Combos:
            for aminoacid in aa:
                if CheckCompatibility(LinearSpectrum(string + aminoacid), SpectrumIdeal) == True:

                    # If compatible thus far, and mass is correct, add to correct pile
                    if FindMass(LinearSpectrum(string + aminoacid)) == CorrectMass:
                        Correct.append(string + aminoacid)

                    # If compatible thus far, but mass is too small, retry with another amino acid appended next round
                    elif FindMass(LinearSpectrum(string + aminoacid)) < CorrectMass:
                        Combos.append(string + aminoacid)

            Combos.remove(string)

            # Selects unique peptides
    unique = {}
    for peptide in Correct:
        string = ''
        for aminoacid in peptide:
            if aminoacid == 'L' or aminoacid == 'I':
                string += 'L'
            else:
                string += aminoacid
        unique[string] = 1
    return unique


Peptides = IdealSequencing(SpectrumIdeal)
print ("asd")
ans=[]
for peptide in Peptides:
    temp = ""
    for char in peptide:
        temp = temp +"-"+ aa[char]
    ans.append (temp[1:])

# for each in set(ans):
#     #print (each)
#print (set(ans))
#186-128-113 186-113-128 128-186-113 128-113-186 113-186-128 113-128-186


def AAtoWeight(pep):
    AAs = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'N': 114, 'D': 115, 'K': 128,
           'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}
    weight = 0
    for p in pep:
        weight += AAs[p]
    return weight


def expand(leaders):
    AAs = ['G', 'A', 'S', 'P', 'V', 'T', 'C', 'I', 'N', 'D', 'K', 'E', 'M', 'H', 'F', 'R', 'Y', 'W']
    newLead = []
    for l in leaders:
        for aa in AAs:
            newLead.append(l + aa)

    return newLead


def spectrumInt(spectrum):
    spectrum = spectrum.split()
    intSpec = []

    for s in spectrum:
        intSpec.append(int(s))

    return intSpec


def removeBad(leaderboard, removeList):
    for r in removeList:
        if r in leaderboard:
            leaderboard.remove(r)

    return leaderboard


def cycloSubPep(pep):
    fragments = []
    fragments.append("")
    # print pep
    size = 1
    while size < len(pep):
        x = 0
        while x < len(pep):
            y = (x + size) % len(pep)

            if x < y:
                fragments.append(pep[x:y])
            else:
                fragments.append(pep[x:] + pep[:y])

            x += 1
        size += 1

    fragments.append(pep)

    # print fragments
    return fragments


def theoSpec(pep):
    tSpec = []
    allFragments = []
    allFragments = cycloSubPep(pep)

    for aF in allFragments:
        tSpec.append(AAtoWeight(aF))

    return tSpec


def score(pep, spec):
    value = 0
    testSpec = list(spec)

    tpep = theoSpec(pep)
    # print tpep
    for x in tpep:
        if x in testSpec:
            value += 1
            testSpec.remove(x)

    return value


def keepHigh(sca, k):
    highScores = []
    sortedHS = sorted(sca.items(), key=lambda x: x[1], reverse=True)
    # print sortedHS
    # print len(sortedHS)
    # print k
    x = 0
    while (x < k and x < len(sortedHS)):
        # print x, sortedHS[x][0], sortedHS[x][1]
        highScores.append(sortedHS[x][0])
        x += 1

    if k < len(sortedHS):
        tieScore = sortedHS[k - 1][1]
        # print tieScore

        y = k
        while y < len(sortedHS) and tieScore == sortedHS[y][1]:
            # print y, sortedHS[y][0], sortedHS[y][1]
            highScores.append(sortedHS[y][0])
            y += 1

    return highScores


def cut(leaderboard, spectrum, k):
    leaderDic = {}
    for pep in leaderboard:
        sc = 0
        sc = score(pep, spectrum)
        # print pep, sc
        leaderDic[pep] = sc

    # print leaderDic
    highScores = keepHigh(leaderDic, k)
    # print highScores

    return highScores


def massPrint(pep):
    s = ""
    for m in pep:
        s += str(AAtoWeight(m)) + "-"
    return s


def getFile():
    from os.path import expanduser
    home = expanduser("~")
    fileName = "dataset_24_4.txt"
    path = home + '//Downloads//' + fileName
    # print path
    fileToOpen = open(path, 'r')
    return fileToOpen


if __name__ == '__main__':
    #f = getFile()
    #     f.readline()
    k = 413
    Stringito='0 87 87 97 99 99 99 99 99 101 101 113 113 113 113 114 128 131 137 137 147 147 156 156 186 186 212 212 212 213 214 224 225 227 230 230 238 241 243 244 246 250 255 257 257 260 284 300 313 317 323 325 326 329 338 342 344 349 351 355 356 357 359 368 370 371 372 377 383 394 413 416 426 437 443 450 452 454 456 462 469 469 469 470 470 473 476 481 485 485 507 514 515 541 550 551 563 563 563 568 569 572 574 580 582 582 584 584 594 598 599 601 606 612 613 616 638 664 673 678 681 681 683 693 693 697 697 698 700 700 700 711 712 713 719 719 719 729 740 775 785 787 792 794 796 799 806 810 811 811 814 818 820 820 820 824 825 826 828 841 853 856 886 898 905 907 910 913 919 922 922 923 923 924 925 927 931 941 943 954 954 957 957 967 976 997 1000 1006 1021 1022 1026 1032 1035 1036 1038 1042 1044 1053 1055 1063 1066 1067 1068 1069 1070 1075 1078 1094 1113 1134 1135 1137 1143 1152 1153 1154 1156 1162 1162 1166 1166 1167 1168 1169 1175 1179 1181 1181 1182 1188 1207 1236 1241 1251 1254 1257 1261 1269 1275 1276 1279 1280 1280 1280 1281 1281 1282 1290 1293 1294 1299 1303 1306 1335 1338 1367 1370 1374 1379 1380 1383 1391 1392 1392 1393 1393 1393 1394 1397 1398 1404 1412 1416 1419 1422 1432 1437 1466 1485 1491 1492 1492 1494 1498 1504 1505 1506 1507 1507 1511 1511 1517 1519 1520 1521 1530 1536 1538 1539 1560 1579 1595 1598 1603 1604 1605 1606 1607 1610 1618 1620 1629 1631 1635 1637 1638 1641 1647 1651 1652 1667 1673 1676 1697 1706 1716 1716 1719 1719 1730 1732 1742 1746 1748 1749 1750 1750 1751 1751 1754 1760 1763 1766 1768 1775 1787 1817 1820 1832 1845 1847 1848 1849 1853 1853 1853 1855 1859 1862 1862 1863 1867 1874 1877 1879 1881 1886 1888 1898 1933 1944 1954 1954 1954 1960 1961 1962 1973 1973 1973 1975 1976 1976 1980 1980 1990 1992 1992 1995 2000 2009 2035 2057 2060 2061 2067 2072 2074 2075 2079 2089 2089 2091 2091 2093 2099 2101 2104 2105 2110 2110 2110 2122 2123 2132 2158 2159 2166 2188 2188 2192 2197 2200 2203 2203 2204 2204 2204 2211 2217 2219 2221 2223 2230 2236 2247 2257 2260 2279 2290 2296 2301 2302 2303 2305 2314 2316 2317 2318 2322 2324 2329 2331 2335 2344 2347 2348 2350 2356 2360 2373 2389 2413 2416 2416 2418 2423 2427 2429 2430 2432 2435 2443 2443 2446 2448 2449 2459 2460 2461 2461 2461 2487 2487 2517 2526 2526 2536 2536 2542 2545 2559 2560 2560 2560 2560 2572 2572 2574 2574 2574 2574 2574 2576 2586 2586 2673'
    spectrum = Stringito.rstrip()
    #f.close()
    spectrum = spectrumInt(spectrum)

    print (k)
    print (spectrum)
    parentMass = spectrum[-1]
    print (parentMass)

    leaderboard = [""]
    leaderPeptide = ""

    x = 0
    done = False
    while not done and len(leaderboard) != 0:
        leaderboard = expand(leaderboard)
        removeList = []
        for p in leaderboard:
            if AAtoWeight(p) == parentMass:
                if score(p, spectrum) > score(leaderPeptide, spectrum):
                    leaderPeptide = p

            if AAtoWeight(p) > parentMass:
                removeList.append(p)

        leaderboard = cut(leaderboard, spectrum, k)
        leaderboard = removeBad(leaderboard, removeList)
        print(    leaderboard)
        print(     len(leaderboard))
        print(     "")

print (massPrint(leaderPeptide)[:-1])