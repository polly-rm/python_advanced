# 2.Sets Of Elements
# n, m = input().split()
# n = int(n)
# m = int(m)
# n_set = set()
# m_set = set()
# for _ in range(n):
#     number = int(input())
#     n_set.add(number)
#
# for _ in range(m):
#     num = int(input())
#     m_set.add(num)
#
# result_nums = n_set.intersection(m_set)
# for n in result_nums:
#     print(n)


# 3.Periodic Table
# n = int(input())
# elements = set()
# for _ in range(n):
#     data = input().split()
#     for el in data:
#         elements.add(el)
#
# for element in elements:
#     print(element)


# 4.Count Symbols
# text = input()
# symbols = {}
# for el in text:
#     if el not in symbols:
#         symbols[el] = 1
#     else:
#         symbols[el] += 1
#
# # sorted_heroes = dict(sorted(heroes.items(), key = lambda x: (-x[1]['hit_points'], x[0])))
# sorted_symbols = dict(sorted(symbols.items(), key= lambda x: x[0]))
# for symbol, count in sorted_symbols.items():
#     print(f'{symbol}: {count} time/s')


# 5.PhoneBook
# data = input()
# phone_book = {}
# while not data.isdigit():
#     name, phone = data.split('-')
#     phone_book[name] = phone
#     data = input()
#
# data = int(data)
# for _ in range(data):
#     name_to_call = input()
#     if name_to_call in phone_book.keys():
#         print(f'{name_to_call} -> {phone_book[name_to_call]}')
#     else:
#         print(f'Contact {name_to_call} does not exist.')


# 6.Longest Intersection
# n = int(input())
# intersections = []
# for _ in range(n):
#     data = input()
#     first_seq, second_seq = data.split('-')
#     start, stop = [int(el) for el in first_seq.split(',')]
#     first_seq = range(start, stop + 1)
#     start, stop = [int(el) for el in second_seq.split(',')]
#     second_seq = range(start, stop + 1)
#     intersection = set(first_seq).intersection(set(second_seq))
#     intersections.append(intersection)
#
# longest = sorted(intersections, key= lambda x: -len(x))[0]
# print(f'Longest intersection is {list(longest)} with length {len(longest)}')


# 7.Battle of Names






