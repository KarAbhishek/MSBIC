from BioInformatics.Week_14.viterbi_algo import viterbi_algorithm, get_matrix, backtrack_viterbi
from BioInformatics.Week_15.param_estimation import param_estimation


def convert_tuple_dict_to_dict_of_dicts(matrix):
    import pandas as pd
    idx = pd.MultiIndex.from_tuples(matrix.keys())
    matrix = (pd.DataFrame(list(matrix.values()), index=idx, columns=['Score'])
              .unstack(fill_value=0)['Score'].to_dict())
    return matrix


def convert_dict_of_dicts_to_tuple_dict(dict_of_dicts):
    import pandas as pd
    df = pd.DataFrame(dict_of_dicts)
    return {(col, idx): df[col][idx] for col in df.columns.values for idx in df.index.values}


if __name__ == '__main__':
    file = open('test')
    lines = file.read().splitlines()
    num = int(lines[0])
    le_string = lines[2]
    le_alphabets = lines[4].split()
    states_out = lines[6].split()
    logger_flag = True
    transition_matrix_out = get_matrix(lines[8:8 + (len(states_out) + 1)], logger_flag)
    emission_matrix_out = get_matrix(lines[(8 + len(states_out) + 2):], logger_flag)
    print(transition_matrix_out, emission_matrix_out)
    # transition_matrix_out_ = convert_tuple_dict_to_dict_of_dicts(transition_matrix_out)
    # emission_matrix_out_ = convert_tuple_dict_to_dict_of_dicts(emission_matrix_out)

    import pandas as pd
    for idx in range(1, num+1):
        path = backtrack_viterbi(viterbi_algorithm(le_string, states_out, transition_matrix_out, emission_matrix_out))
        transition_matrix_out, emission_matrix_out = param_estimation(states_out, le_alphabets, le_string, path)
        transition_matrix_out = convert_dict_of_dicts_to_tuple_dict(transition_matrix_out)
        emission_matrix_out = convert_dict_of_dicts_to_tuple_dict(emission_matrix_out)


    # print(transition_matrix_out)
    # print(emission_matrix_out)
    transition_matrix_out = convert_tuple_dict_to_dict_of_dicts(transition_matrix_out)
    emission_matrix_out = convert_tuple_dict_to_dict_of_dicts(emission_matrix_out)
    print(pd.DataFrame(transition_matrix_out).round(3))
    print(pd.DataFrame(emission_matrix_out).round(3))
