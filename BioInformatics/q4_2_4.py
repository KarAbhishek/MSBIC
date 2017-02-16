import sys

def load_genetic_code():
    hm = {}
    file = open('data/Genetic_Code')
    lines = file.read().splitlines()
    for line in lines:
        k, v = line.split(' ')
        hm[k] = v
    return hm


def protein_translation(pattern, genetic_code):
    try:
        return [genetic_code[pattern[i:i+3]] for i in range(len(pattern)-1)[::3]]
    except KeyError:
        print('Z' * int(len(pattern)/3))


if __name__ == '__main__':
    file = open("data/4_2_4_data")
    lines = file.read()
    pattern_out = lines
    genetic_code_out = load_genetic_code()
    output = protein_translation(pattern_out, genetic_code_out)

    formatted_output = ''.join(output[:-1])

    print(formatted_output)
