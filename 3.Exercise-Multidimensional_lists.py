# 1.Diagonal Difference
# def read_matrix(is_test=False):
#     if is_test:
#         return [
#             [11, 2, 4],
#             [4, 5, 6],
#             [10, 8, -12],
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
# def sum_diagonals(matrix):
#     diagonal_sum = 0
#     for i in range(len(matrix)):
#         diagonal_sum += matrix[i][i]
#         diagonal_sum -= matrix[i][len(matrix) - i - 1]
#     if diagonal_sum < 0:
#         diagonal_sum *= -1
#     return diagonal_sum
#
# print(sum_diagonals(read_matrix()))


# 2.Squares in Matrix
# def read_matrix(is_test=False):
#     if is_test:
#         return [
#             ['A', 'B', 'B', 'D'],
#             ['E', 'B', 'B', 'B'],
#             ['I', 'J', 'B', 'B'],
#         ]
#     else:
#         (rows_count, columns_count) = map(int, input().split(' '))
#         matrix = []
#         for row_index in range(rows_count):
#             row = [x for x in input().split(' ')]
#             matrix.append(row)
#
#         return matrix
#
# def find_num_equal_squares(matrix):
#     num_equal_squares = 0
#     for r in range(len(matrix)-1):
#         row = matrix[r]
#         down_row = matrix[r+1]
#         for c in range(len(row)-1):
#             if row[c] == row[c+1] == down_row[c] == down_row[c+1]:
#                 num_equal_squares += 1
#     return num_equal_squares
#
# print(find_num_equal_squares(read_matrix()))


# 3.Maximal Sum 67/100
# rows, cols = [int(el) for el in input().split()]
#
# def init_matrix():
#     matrix = []
#     for row_index in range(rows):
#         row = [int(x) for x in input().split()]
#         matrix.append(row)
#     return matrix
#
# def biggest_sum_elements_of_submatrix(row, col, matr):
#     current_el = matr[row][col]
#     second_el = matr[row][col+1]
#     third_el = matr[row][col+2]
#     current_el_down = matr[row+1][col]
#     second_el_down = matr[row+1][col+1]
#     third_el_down = matr[row+1][col+2]
#     current_el_bottom = matr[row + 2][col]
#     second_el_bottom = matr[row + 2][col + 1]
#     third_el_bottom = matr[row + 2][col + 2]
#
#     sum_elements = current_el + second_el + third_el + current_el_down + second_el_down + third_el_down + current_el_bottom + second_el_bottom + third_el_bottom
#     return (sum_elements, current_el, second_el, third_el, current_el_down, second_el_down, third_el_down, current_el_bottom, second_el_bottom, third_el_bottom)
#
# matrix = init_matrix()
# biggest_sum = 0
# counter = 0
# submatrix = []
# best_current_el = 0
# best_second_el = 0
# best_third_el = 0
# best_current_el_down = 0
# best_second_el_down = 0
# best_third_el_down = 0
# best_current_el_bottom = 0
# best_second_el_bottom = 0
# best_third_el_bottom = 0
# for row_index in range(rows-2):
#     for col_index in range(cols-2):
#         if biggest_sum_elements_of_submatrix(row_index, col_index, matrix)[0] > biggest_sum:
#             biggest_sum = biggest_sum_elements_of_submatrix(row_index, col_index, matrix)[0]
#             best_current_el = biggest_sum_elements_of_submatrix(row_index, col_index, matrix)[1]
#             best_second_el = biggest_sum_elements_of_submatrix(row_index, col_index, matrix)[2]
#             best_third_el = biggest_sum_elements_of_submatrix(row_index, col_index, matrix)[3]
#             best_current_el_down = biggest_sum_elements_of_submatrix(row_index, col_index, matrix)[4]
#             best_second_el_down = biggest_sum_elements_of_submatrix(row_index, col_index, matrix)[5]
#             best_third_el_down = biggest_sum_elements_of_submatrix(row_index, col_index, matrix)[6]
#             best_current_el_bottom = biggest_sum_elements_of_submatrix(row_index, col_index, matrix)[7]
#             best_second_el_bottom = biggest_sum_elements_of_submatrix(row_index, col_index, matrix)[8]
#             best_third_el_bottom = biggest_sum_elements_of_submatrix(row_index, col_index, matrix)[9]
#
# submatrix.append([best_current_el, best_second_el, best_third_el])
# submatrix.append([best_current_el_down, best_second_el_down, best_third_el_down])
# submatrix.append([best_current_el_bottom, best_second_el_bottom, best_third_el_bottom])
# print(f'Sum = {biggest_sum}')
# for l in submatrix:
#     print(' '.join([str(x) for x in l]))



# 4.Matrix Shuffling 80/100 Runtime Error
# (rows_count, columns_count) = map(int, input().split())
# matrix = []
# for row_index in range(rows_count):
#     row = [int(x) for x in input().split()]
#     matrix.append(row)
#
# command = input()
# while not command == 'END':
#     data = command.split()
#     if not len(data) == 5:
#         print("Invalid input!")
#     else:
#         command_word = data[0]
#         row_1 = int(data[1])
#         col_1 = int(data[2])
#         row_2 = int(data[3])
#         col_2 = int(data[4])
#         if not command_word == 'swap' or not 0 <= row_1 < rows_count or not 0 <= row_2 < rows_count or not 0 <= col_1 < columns_count or not 0 <= col_1 < columns_count:
#             print("Invalid input!")
#         else:
#             matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]
#             for r in matrix:
#                 print(' '.join(str(x) for x in r))
#     command = input()


# 5.Snake Moves
# rows, cols = [int(el) for el in input().split()]
# word = input()
# matrix = []
# index_word = 0
#
# for row_index in range(rows):
#     matrix.append([0 for el in range(cols)])
#
# for row_index in range(rows):
#     for col_index in range(cols):
#         matrix[row_index][col_index] = word[index_word]
#         index_word += 1
#         if index_word == len(word):
#             index_word = 0
#
# for row_index in range(rows):
#     if row_index % 2 == 1:
#         matrix[row_index].reverse()
#     print(''.join(matrix[row_index]))


# 6.Knight Moves
n = int(input())
matrix = []

for _ in range(n):
    matrix.append(list(input()))

def is_valid_bound (row, col):
    if 0 <= row < n and 0 <= col < n:
        return True
    return False

def calculate_kills(matrix, row, col):
    kills = 0
    rows = [-2, -2, 2, 2, 1, 1, -1, -1]
    cols = [-1, 1, -1, 1, -2, 2, -2, 2]
    for index in range(len(rows)):
        potential_row = row+rows[index]
        potential_col = col+cols[index]
        if is_valid_bound(potential_row, potential_col):
            potential_position = matrix[potential_row][potential_col]
            if potential_position == 'K':
                kills += 1
    return kills

removed_counter = 0
while True:
    max_kills = 0
    killer_position = []

    for row_index in range(n):
        for col_index in range(n):
            if matrix[row_index][col_index] == 'K':
                kills = calculate_kills(matrix, row_index, col_index)
                if max_kills < kills:
                    max_kills = kills
                    killer_position = [row_index, col_index]

    if killer_position:
        matrix[killer_position[0]][killer_position[1]] = '0'
        removed_counter += 1
    else:
        break

print(removed_counter)




# 7.Bombs 90/100?
# size = int(input())
# matrix = []
# for _ in range (size):
#     matrix.append([int(el) for el in input().split()])
#
# coordinates = input().split()
# for data in coordinates:
#     row, col = [int(x) for x in data.split(',')]
#
#     current_num = matrix[row][col]
#     if row == 0:
#         if col == 0:
#             if size > 1:
#                 if matrix[0][1] > 0:
#                     matrix[0][1] -= current_num
#                 if matrix[1][0] > 0:
#                     matrix[1][0] -= current_num
#                 if matrix[1][1] > 0:
#                     matrix[1][1] -= current_num
#             elif size == 0:
#                 matrix[0][0] = 0
#         elif col == size - 1:
#             if matrix[0][size-2] > 0:
#                 matrix[0][size - 2] -= current_num
#             if matrix[1][size-2] > 0:
#                 matrix[1][size - 2] -= current_num
#             if matrix[1][size-1] > 0:
#                 matrix[1][size-1] -= current_num
#         elif 0 < col < size - 1:
#             if matrix[0][col-1] > 0:
#                 matrix[0][col-1] -= current_num
#             if matrix[0][col+1] > 0:
#                 matrix[0][col+1] -= current_num
#             if matrix[1][col-1] > 0:
#                 matrix[1][col-1] -= current_num
#             if matrix[1][col] > 0:
#                 matrix[1][col] -= current_num
#             if matrix[1][col+1] > 0:
#                 matrix[1][col+1] -= current_num
#
#     elif row == size - 1:
#         if col == 0:
#             if matrix[row][1] > 0:
#                 matrix[row][1] -= current_num
#             if matrix[row-1][0] > 0:
#                 matrix[row-1][0] -= current_num
#             if matrix[row-1][1] > 0:
#                 matrix[row-1][1] -= current_num
#         elif col == size - 1:
#             if matrix[row][size - 2] > 0:
#                 matrix[row][size - 2] -= current_num
#             if matrix[row - 1][size - 2] > 0:
#                 matrix[row-1][size - 2] -= current_num
#             if matrix[row-1][size-1] > 0:
#                 matrix[row-1][size-1] -= current_num
#         elif 0 < col < size - 1:
#             if matrix[row][col-1] > 0:
#                 matrix[row][col-1] -= current_num
#             if matrix[row][col+1] > 0:
#                 matrix[row][col+1] -= current_num
#             if matrix[row-1][col-1] > 0:
#                 matrix[row-1][col-1] -= current_num
#             if matrix[row-1][col] > 0:
#                 matrix[row-1][col] -= current_num
#             if matrix[row-1][col+1] > 0:
#                 matrix[row-1][col+1] -= current_num
#
#
#     elif 0 < row < size - 1:
#         if 0 < col < size - 1:
#             if matrix[row - 1][col - 1] > 0:
#                 matrix[row - 1][col - 1] -= current_num
#             if matrix[row - 1][col] > 0:
#                 matrix[row - 1][col] -= current_num
#             if matrix[row - 1][col + 1] > 0:
#                 matrix[row - 1][col + 1] -= current_num
#             if matrix[row][col - 1] > 0:
#                 matrix[row][col - 1] -= current_num
#             if matrix[row][col + 1] > 0:
#                 matrix[row][col + 1] -= current_num
#             if matrix[row + 1][col - 1] > 0:
#                 matrix[row + 1][col - 1] -= current_num
#             if matrix[row + 1][col] > 0:
#                 matrix[row + 1][col] -= current_num
#             if matrix[row + 1][col + 1] > 0:
#                 matrix[row + 1][col + 1] -= current_num
#         elif col == 0:
#             if matrix[row - 1][col] > 0:
#                 matrix[row - 1][col] -= current_num
#             if matrix[row - 1][col + 1] > 0:
#                 matrix[row - 1][col + 1] -= current_num
#             if matrix[row][col + 1] > 0:
#                 matrix[row][col + 1] -= current_num
#             if matrix[row + 1][col] > 0:
#                 matrix[row + 1][col] -= current_num
#             if matrix[row + 1][col + 1] > 0:
#                 matrix[row + 1][col + 1] -= current_num
#         elif col == size - 1:
#             if matrix[row - 1][col - 1] > 0:
#                 matrix[row - 1][col - 1] -= current_num
#             if matrix[row - 1][col] > 0:
#                 matrix[row - 1][col] -= current_num
#             if matrix[row][col - 1] > 0:
#                 matrix[row][col - 1] -= current_num
#             if matrix[row + 1][col - 1] > 0:
#                 matrix[row + 1][col - 1] -= current_num
#             if matrix[row + 1][col] > 0:
#                 matrix[row + 1][col] -= current_num
#
#     matrix[row][col] = 0
#
# alive_cells = []
# for row in matrix:
#     for col in row:
#         if col > 0:
#             alive_cells.append(col)
#
# print(f'Alive cells: {len(alive_cells)}')
# print(f'Sum: {sum(alive_cells)}')
#
# for row in matrix:
#     print(' '.join([str(x) for x in row]))


# 8.Miner
# size = int(input())
# commands = input().split()
# matrix = []
# for _ in range(size):
#     matrix.append([el for el in input().split()])
#
# row_index_current_pos = 0
# col_index_current_pos = 0
# total_coals = 0
# coals_taken = 0
# is_valid = True
# for row_index in range(size):
#     for col_index in range(size):
#         if matrix[row_index][col_index] == 's':
#             row_index_current_pos = row_index
#             col_index_current_pos = col_index
#         elif matrix[row_index][col_index] == 'c':
#             total_coals += 1
#
# for command in commands:
#     if command == 'left':
#         if col_index_current_pos != 0:
#             col_index_current_pos -= 1
#     elif command == 'right':
#         if col_index_current_pos != size-1:
#             col_index_current_pos += 1
#     elif command == 'up':
#         if row_index_current_pos != 0:
#             row_index_current_pos -= 1
#     elif command == 'down':
#         if row_index_current_pos != size-1:
#             row_index_current_pos += 1
#     current_position = matrix[row_index_current_pos][col_index_current_pos]
#
#     if matrix[row_index_current_pos][col_index_current_pos] == 'e':
#         print(f'Game over! ({row_index_current_pos}, {col_index_current_pos})')
#         is_valid = False
#         break
#
#     elif matrix[row_index_current_pos][col_index_current_pos] == 'c':
#         matrix[row_index_current_pos][col_index_current_pos] = '*'
#         coals_taken += 1
#         if coals_taken == total_coals:
#             print(f'You collected all coals! ({row_index_current_pos}, {col_index_current_pos})')
#             is_valid = False
#             break
#
# if is_valid:
#     print(f'{total_coals-coals_taken} coals left. ({row_index_current_pos}, {col_index_current_pos})')





