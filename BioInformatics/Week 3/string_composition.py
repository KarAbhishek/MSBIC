import sys


def string_composition(text, k):
    k_mer_set = list()
    for idx in range(len(text)-k+1):
        k_mer = text[idx:idx+k]
        k_mer_set.append(k_mer)
    sorted_set = sorted(list(k_mer_set))
    print('Size is ', len(sorted_set))
    return sorted_set


if __name__ == '__main__':
    file = open('data/input')
    lines = file.read().splitlines()
    k_out = int(lines[0])
    text_out = lines[1]
    output = string_composition(text_out, k_out)
    formatted_output = '\n'.join(output)
    print(formatted_output)

    file = open('output/3_2', 'w+')
    file.write(formatted_output)
    file.close()
