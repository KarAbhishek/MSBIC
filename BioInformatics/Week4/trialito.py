def spec_convolution(spectrum):
    for i in spectrum:
        for j in spectrum:
            if (i-j)>0:
                print(i-j, end=' ')


spectrum = '700 876 771 512 113 113 589 517 115 404 271 276 415 131 632 702 948 220 863 57 587 991 756 1104 643 228 976 592 976 461 333 0 259 635 163 919 241 384 469 316 689 530 185 884 828 515 402 989 643 472 720 973 461 354 941 348 479 287 750 833 625 1047 356 788 128 574 128 241 156 817 991 748 845 863'
spectrum = list(map(int, spectrum.split(' ')))
spec_convolution(spectrum)