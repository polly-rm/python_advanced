# 1.Sum Matrix Element
# def read_matrix(is_test=False):
#     if is_test:
#         return [
#             [7, 1, 3, 3, 2, 1],
#             [1, 3, 9, 8, 5, 6],
#             [4, 6, 7, 9, 1, 0],
#         ]
#     else:
#         (rows_count, columns_count) = map(int, input().split(', '))
#         matrix = []
#         for row_index in range(rows_count):
#             row = [int(x) for x in input().split(', ')]
#             matrix.append(row)
#
#         return matrix
#
# matrix = read_matrix()
# matrix_sum = 0
#
# for r in range(len(matrix)):
#     row = matrix[r]
#     matrix_sum += sum(row)
#
# print(matrix_sum)
# print(matrix)


# 2.Sum Matrix Column
# def read_matrix(is_test=False):
#     if is_test:
#         return [
#             [7, 1, 3, 3, 2, 1],
#             [1, 3, 9, 8, 5, 6],
#             [4, 6, 7, 9, 1, 0],
#         ]
#     else:
#         (rows_count, columns_count) = map(int, input().split(', '))
#         matrix = []
#         for row_index in range(rows_count):
#             row = [int(x) for x in input().split(' ')]
#             matrix.append(row)
#
#         return matrix
#
# def get_columns_sums(matrix):
#     rows_count = len(matrix)
#     columns_count = len(matrix[0])
#
#     sums = [0] * columns_count
#     for row_index in range (rows_count):
#         for column_index in range (columns_count):
#             sums[column_index] += matrix[row_index][column_index]
#     return sums
#
# def print_result(values):
#     [print(x) for x in values]
#
# matrix = read_matrix()
# result = get_columns_sums(matrix)
# print_result(result)


# 3.Primary Diagonal
# def read_matrix(is_test=False):
#     if is_test:
#         return [
#             [11, 2, 4],
#             [4, 5, 6],
#             [10, 8, -12],
#
#         ]
#     else:
#         size = int(input())
#         matrix = []
#         for row_index in range(size):
#             row = [int(x) for x in input().split(' ')]
#             matrix.append(row)
#
#         return matrix
#
# def get_primary_diagonal_sum(matrix):
#     diagonal_sum = 0
#     for i in range(len(matrix)):
#         diagonal_sum += matrix[i][i]
#     return diagonal_sum
#
# print(get_primary_diagonal_sum(read_matrix()))


# 4.Symbol in Matrix
# def read_matrix(is_test=False):
#     if is_test:
#         return [
#             ['A', 'B', 'C'],
#             ['D', 'E', 'F'],
#             ['X', '!', '@'],
#         ]
#     else:
#         size = int(input())
#         matrix = []
#         for row_index in range(size):
#             row = [x for x in input()]
#             matrix.append(row)
#
#         return matrix
#
# def find_symbol(matrix, symbol):
#     size = len(matrix)
#     for row_index in range(size):
#         row = matrix[row_index]
#         if symbol in row:
#             return row_index, row.index(symbol)
#     return None
#
# def print_result(result, symbol):
#     if result:
#         print(result)
#     else:
#         print(f'{symbol} does not occur in the matrix')
#
# matrix = read_matrix()
# symbol = input()
# print_result(find_symbol(matrix, symbol), symbol)


# 5.Square with Maximum Sum
def read_matrix(is_test=False):
    if is_test:
        return [
            [7, 1, 3, 3, 2, 1],
            [1, 3, 9, 8, 5, 6],
            [4, 6, 7, 9, 1, 0],
        ]
    else:
        (rows_count, columns_count) = map(int, input().split(', '))
        matrix = []
        for row_index in range(rows_count):
            row = [int(x) for x in input().split(', ')]
            matrix.append(row)

        return matrix


def get_sum_of_submatrix(matrix, row_index, column_index, size):
    the_sum = 0
    for r in range(row_index, row_index + size):
        for c in range(column_index, column_index + size):
            the_sum += matrix[r][c]
    return the_sum


def get_best_submatrix_sum_coordinates(matrix, submatrix_size):
    best_row_index = 0
    best_column_index = 0
    best_sum = get_sum_of_submatrix(matrix, 0, 0, submatrix_size)

    for row_index in range(len(matrix) - submatrix_size + 1):
        for col_index in range(len(matrix[row_index]) - submatrix_size + 1):
            current_sum = get_sum_of_submatrix(matrix, row_index, col_index, submatrix_size)
            if best_sum < current_sum:
                best_sum = current_sum
                best_row_index = row_index
                best_column_index = col_index
    return (best_row_index, best_column_index)


def print_result(coordinates, size):
    (row_index, col_index) = coordinates
    for r in range(row_index, row_index + size):
        row = []
        for c in range(col_index, col_index + size):
            row.append(matrix[r][c])
        print(' '.join(str(x) for x in row))
    print(get_sum_of_submatrix(matrix, row_index, col_index, size))


SUBMATRIX_SIZE = 2

matrix = read_matrix()
coordinates = get_best_submatrix_sum_coordinates(matrix, SUBMATRIX_SIZE)
print_result(coordinates, SUBMATRIX_SIZE)


