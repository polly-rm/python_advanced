# 1.Reverse String
# text = input()
# s = []
# for char in text[::-1]:
#     s.append(char)
# print(''.join(s))

# 2.Matching Brackets
# text = input()
# s = []
# for index in range(len(text)):
#     if text[index] == '(':
#         s.append(index)
#     elif text[index] == ')':
#         j = s.pop()
#         print(text[j:index+1])

# 3.Supermarket
# from collections import deque
# q = deque()
# name = input()
# while not name == 'End':
#     if not name == 'Paid':
#         q.append(name)
#     else:
#         while q:
#             print(q.popleft())
#
#     name = input()
#
# print(f"{len(q)} people remaining.")

# 4.Water Dispenser
# from collections import deque
# quantity_water = int(input())
# name = input()
# q = deque()
# while not name == 'Start':
#     q.append(name)
#     name = input()
#
# command = input()
# while not command == 'End':
#     if command.startswith('refill'):
#         liters = int(command.split()[1])
#         quantity_water += liters
#     else:
#         liters = int(command)
#         if liters <= quantity_water:
#             print(f"{q.popleft()} got water")
#             quantity_water -= liters
#         else:
#             print(f"{q.popleft()} must wait")
#     command = input()
#
# print(f"{quantity_water} liters left")


# 5.Hot Potato
# from collections import deque
# names = input().split()
# number_toss = int(input())
# q = deque()
# for name in names:
#     q.append(name)
#
# counter = 0
# while len(q) > 1:
#     counter += 1
#     current_player = q.popleft()
#     if counter == number_toss:
#         print(f"Removed {current_player}")
#         counter = 0
#     else:
#         q.append(current_player)
# print(f"Last is {q.popleft()}")


