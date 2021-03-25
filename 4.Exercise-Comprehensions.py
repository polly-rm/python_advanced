# 1.Word Filter
# result = [el for el in input().split() if len(el) % 2 == 0]
# for word in result:
#     print(word)

# 2.Words Lengths
# result = {word: len(word) for word in input().split(', ')}
# final = [f'{key} -> {value}' for key,value in result.items()]
# print(', '.join(final))


# 3.Capitals
# countires = tuple(input().split(', '))
# capitals = tuple(input().split(', '))
# # pairs = list(zip(countires, capitals))
# result = {el[0]: el[1] for el in list(zip(countires, capitals))}
# for key, value in result.items():
#     print(f'{key} -> {value}')


# 4.Number Class
# nums = input().split(', ')
# positive = [num for num in nums if int(num) >= 0]
# negative = [num for num in nums if int(num) < 0]
# even = [num for num in nums if int(num) % 2 == 0]
# odd = [num for num in nums if int(num) % 2 == 1]
# print(f"Positive: {', '.join(positive)}")
# print(f"Negative: {', '.join(negative)}")
# print(f"Even: {', '.join(even)}")
# print(f"Odd: {', '.join(odd)}")


# 5.Diagonals
# n = int(input())
# matrix = []
# for _ in range (n):
#     matrix.append([int(el) for el in input().split(', ')])
#
# first_d = [matrix[i][i] for i in range(n)]
# second_d = [matrix[i][n - i - 1] for i in range(n)]
# print(f"First diagonal: {', '.join([str(x) for x in first_d])}. Sum: {sum(first_d)}")
# print(f"Second diagonal: {', '.join([str(x) for x in second_d])}. Sum: {sum(second_d)}")


# 6.Matrix of Palindromes
# rows, cols = [int(el) for el in input().split()]
# alfa = "abcdefghijklmnopqrstuvwxyz"
# matrix = []
# for r in range(rows):
#     matrix.append([['a', 'a', 'a'] for _ in range(cols)])
#
# for row_i in range(rows):
#     i = row_i
#     for col_i in range(cols):
#         current_el = matrix[row_i][col_i]
#         current_el[0] = alfa[row_i]
#         current_el[-1] = alfa[row_i]
#         current_el[1] = alfa[i]
#         i += 1
#
# for row in matrix:
#     for col_i in range(len(row)):
#         str_el = ''.join(row[col_i])
#         row[col_i] = str_el
#
#     print(*row)


# 7.Flatten List
# elements = [int(n) for el in input().split('|')[::-1] for n in el.split()]
# print(*elements)


# 8.Heroes Inventory   80/100
# names = [name for name in input().split(', ')]
# data = input()
# people = {}
# while not data == "End":
#     name, item, price = data.split('-')
#     if not name in people:
#         people[name] = {item: int(price)}
#     else:
#         if not item in people[name]:
#             people[name].update({item: int(price)})
#     data = input()
#
# for person, item_data in people.items():
#     print(f'{person} -> Items: {len(item_data)}, Cost: {sum(item_data.values())}')


# 9.Bunker
# categories = {category: {} for category in input().split(', ')}
# n = int(input())
# for _ in range(n):
#     data = input().split(' - ')
#     category = data[0]
#     item = data[1]
#     q_q_data = data[2]
#     quantity_data, quality_data = q_q_data.split(';')
#     quantity = int(quantity_data.split(':')[1])
#     quality = int(quality_data.split(':')[1])
#     if item not in categories[category]:
#         categories[category].update({item: {'quantity': quantity, 'quality': quality}})
#     else:
#         categories[category][item]['quantity'] += quantity
#         categories[category][item]['quality'] += quality
#
# total_items = 0
# total_quality = 0
# for category, items_data in categories.items():
#     for item, q_q_data in categories[category].items():
#         total_items += q_q_data['quantity']
#         total_quality += q_q_data['quality']
#
# print(f'Count of items: {total_items}')
# average_quality = total_quality / len(categories)
# print(f'Average quality: {average_quality:.2f}')
# items_per_category = []
# for category, items_data in categories.items():
#     for item, q_q_data in categories[category].items():
#         items_per_category.append(item)
#     print(f"{category} -> {', '.join(items_per_category)}")
#     items_per_category.clear()


# 10.Matrix Modification
# n = int(input())
# matrix = []
# for _ in range (n):
#     matrix.append([int(el) for el in input().split()])
#
# data = input()
# while not data == 'END':
#     command, row_index, col_index, value = data.split()
#     row_index = int(row_index)
#     col_index = int(col_index)
#     value = int(value)
#
#     if row_index < 0 or row_index > n-1 or col_index < 0 or col_index > n-1:
#         print('Invalid coordinates')
#
#     else:
#         if command == 'Add':
#             matrix[row_index][col_index] += value
#         elif command == 'Subtract':
#             matrix[row_index][col_index] -= value
#
#     data = input()
#
# for row in matrix:
#     print(*row)