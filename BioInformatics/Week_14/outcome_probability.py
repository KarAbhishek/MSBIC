from BioInformatics.Week_14.hidden_path import get_matrix


def outcome_probability(emission_matrix, hidden_path, the_string):
    total_emission__prob = 1
    for char_idx, char in enumerate(the_string):
        total_emission__prob *= emission_matrix[hidden_path[char_idx], char]
    return total_emission__prob


if __name__ == '__main__':

    file = open('outcome_prob_data.txt')
    lines = file.read().splitlines()
    le_string = lines[0]
    le_alphabets = lines[2]
    # fair_emission_probability = 1.0/len(le_alphabets)
    hidden_path_out = lines[4]
    states_out = lines[6]
    emission_matrix = get_matrix(lines[8:])
    # print(transition_matrix_out)
    prob_out = outcome_probability(emission_matrix, hidden_path_out, le_string)
    print(prob_out)
    file.close()
