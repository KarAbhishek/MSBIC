def size_spectrum_dict(spect, thres, max_score):
    prefix = spect_to_prefix(spect)
    for i in prefix:
        for amino_mass in hm.keys:
            s_i = score(i)
            size_i_t += size(i-amino_mass, thres-s_i)


spec = list(map(int, '4 -3 -2 3 3 -4 5 -3 -1 -1 3 4 1 3'.split()))
threshold = 1
max_scor= 8
size_spectrum_dict(spec, threshold, max_scor)