class Matrix:
    def __init__(self, list_data):
        self.list_data = list_data

    def __str__(self):
        res_matrix = ''
        for line in self.list_data:
            for el in line:
                if el < 0:
                    res_matrix += str(el) + '  '
                else:
                    res_matrix += ' ' + str(el) + '  '
            res_matrix += '\n'
        return res_matrix

    def __add__(self, other):
        if len(self.list_data) == len(other.list_data):
            new_matrix = []
            for i in range(len(self.list_data)):
                if len(self.list_data[i]) == len(other.list_data[i]):
                    list_line = []
                    for i_num in range(len(self.list_data[i])):
                        list_line.append(self.list_data[i][i_num] + other.list_data[i][i_num])
                    new_matrix.append(list_line)
                else:
                    return 'Матрицы не одинакового размера'
            return Matrix(new_matrix)
        else:
            return 'Матрицы не одинакового размера'


matrix_1 = Matrix([[31, 22], [37, 43], [51, 86]])
matrix_2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
matrix_3 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])
matrix_4 = Matrix([[30, 15], [17, 38], [21, 46]])

print(matrix_2)
print(matrix_3)
print(matrix_1)
print(matrix_4)
matrix_5 = matrix_1 + matrix_4
print(matrix_5)
print(matrix_1 + matrix_4)
print(matrix_1 + matrix_3)
