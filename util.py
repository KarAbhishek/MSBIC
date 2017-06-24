class Util:
    id_var = 0

    @staticmethod
    def get_id():
        temp = Util.id_var
        Util.id_var += 1
        return temp

    @staticmethod
    def find_matrix_min(dist_mat):
        min_elem = float('inf')
        min_pos = None
        for i_idx in range(len(dist_mat)):
            for j_idx in range(i_idx + 1, len(dist_mat)):
                comp_elem = dist_mat[i_idx][j_idx]
                if comp_elem < min_elem:
                    min_elem = comp_elem
                    min_pos = (i_idx, j_idx)
        return min_elem, min_pos

    @staticmethod
    def remove(edge, from_list):
        parent = edge[0]
        child = edge[1]
        if not from_list[parent]:
            del from_list[parent]
        del from_list[child][parent]
        if not from_list[child]:
            del from_list[child]

    # Get a matrix
    @staticmethod
    def get_matrix_from_string(lines):
        from collections import defaultdict
        matrix = defaultdict(dict)
        column_keys = lines[0].strip().split('\t')
        for line in lines[1:]:
            row = line.split('\t')
            row_key, matrix_row = row[0], row[1:]
            for content_idx, content in enumerate(matrix_row):
                matrix[row_key, column_keys[content_idx]] = content
        return dict(matrix)
