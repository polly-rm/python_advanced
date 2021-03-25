# 1.ASCII values
# chars = input().split(', ')
# print({char: ord(char) for char in chars})

# 2.No vowels
# vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']
# text = input()
# print(''.join([char for char in text if char not in vowels]))

# 3.Even Matrix
# n = int(input())
# matrix = []
# for _ in range (n):
#     matrix.append([int(el) for el in input().split(', ')])
#
# new_matrix = [[c for c in row if c % 2 == 0] for row in matrix]
# print(new_matrix)


# 4.Flatenninf Matrix
# n = int(input())
# matrix = []
# for _ in range (n):
#     matrix.append([int(el) for el in input().split(', ')])
#
# new_matrix = [c for r in matrix for c in r]
# print(new_matrix)


# 5.Filter Numbers
# start = int(input())
# end = int(input())
# print([x for x in range(start, end + 1) if any (x % i == 0 for i in range(2, 11))])