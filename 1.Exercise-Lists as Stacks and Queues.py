# 1.Reverse number with a Stack
# numbers = input().split()
# while numbers:
#     print(numbers.pop(), end=' ')

# 2.Maximum and Minimum Element
# N = int(input())
# s = []
# for _ in range(N):
#     text = input()
#     if text.startswith('1'):
#         number = int(text.split()[1])
#         s.append(number)
#     elif text.startswith('2'):
#         if s:
#             s.pop()
#     elif text.startswith('3'):
#         if s:
#             print(max(s))
#     elif text.startswith('4'):
#         if s:
#             print(min(s))
#
# stack = []
# for el in s[::-1]:
#     stack.append(str(el))
# print(', '.join(stack))

# 3.Fast Food RUNTIME ERROR!
# from collections import deque
# q = deque()
# quantity_all_food = int(input())
# quantity_meals = input().split()
# for meal in quantity_meals:
#     q.append(int(meal))
# print(max(q))
#
# while q:
#     meal_on_current_position = q.popleft()
#     if meal_on_current_position <= quantity_all_food:
#         quantity_all_food -= meal_on_current_position
#     else:
#         q.append(meal_on_current_position)
#         print(f"Orders left: ", end='')
#         while q:
#             print(f"{q.popleft()}", end=' ')
#         break
#
#     if not q:
#         print("Orders complete")

# 4.Fashion Boutique
# clothes_values = input().split()
# capacity = int(input())
# number_shelves = 1
# capacity_per_shelf = capacity
# s = []
# for cloth in clothes_values:
#     s.append(int(cloth))
#
# while s:
#     cloth_value = s.pop()
#     if cloth_value <= capacity_per_shelf:
#         capacity_per_shelf -= cloth_value
#     else:
#         number_shelves += 1
#         capacity_per_shelf = capacity
#         s.append(cloth_value)
#
# print(number_shelves)


# 5.Truck Tour
# from collections import deque
# n = int(input())
# stations = deque([])
# for _ in range (n):
#     stations.append(input())
#
# for big_circle_iteration in range (n):
#     is_valid = True
#     tank_petrol = 0
#     for small_circle_iteration in range (n):
#         current_station = stations[small_circle_iteration]
#         petrol, distance = current_station.split()
#         petrol = int(petrol)
#         distance = int(distance)
#         tank_petrol += petrol - distance
#
#         if tank_petrol < 0:
#             is_valid = False
#             stations.append(stations.popleft())
#             break
#
#     if is_valid:
#         print(big_circle_iteration)
#         break


# 6.Balanced Parentheses
# text = input()
# is_balanced = True
# parentheses = []
# parentheses_dict = {'(': ')', '{': '}', '[': ']'}
# for el in text:
#     if el in '({[':
#         parentheses.append(el)
#     else:
#         if not parentheses:
#             is_balanced = False
#             break
#         current_opening_p = parentheses.pop()
#         if parentheses_dict[current_opening_p] != el:
#             is_balanced = False
#             break
#
# if is_balanced:
#     print("YES")
# else:
#     print("NO")


# 7.Robothics
# from collections import deque
# from datetime import datetime, timedelta
#
# data = input().split(';')
# time = datetime.strptime(input(), '%H:%M:%S')
#
# robots = []
# available_robots = deque([])
# products = []
#
# for el in data:
#     robot_data = el.split('-')
#     robot = {}
#     robot['name'] = robot_data[0]
#     robot['processing_time'] = int(robot_data[1])
#     robot['available_at'] = time
#     robots.append(robot)
#     available_robots.append(robot)
#
# product = input()
# available_robots = deque(available_robots)
# while not product == 'End':
#     products.append(product)
#     product = input()
#
# products = deque(products)
# time = time + timedelta(seconds=1)
#
# while len(products) > 0:
#     current_product = products.popleft()
#
#     if available_robots:
#         current_robot = available_robots.popleft()
#         current_robot['available_at'] = time + timedelta(seconds=current_robot['processing_time'])
#         robot = [el for el in robots if el == current_robot][0]
#         robot['available_at'] = time + timedelta(seconds=current_robot['processing_time'])
#         print(f"{robot['name']} - {current_product} [{time.strftime('%H:%M:%S')}]")
#     else:
#         for r in robots:
#             if time >= r['available_at']:
#                 available_robots.append(r)
#         if not available_robots:
#             products.append(current_product)
#         else:
#             current_robot = available_robots.popleft()
#             current_robot['available_at'] = time + timedelta(seconds=current_robot['processing_time'])
#             robot = [el for el in robots if el == current_robot][0]
#             robot['available_at'] = time + timedelta(seconds=current_robot['processing_time'])
#             print(f"{robot['name']} - {current_product} [{time.strftime('%H:%M:%S')}]")
#
#     time = time + timedelta(seconds=1)


# 8.Crossroads
from collections import deque
duration_green_light = int(input())
duration_free_window = int(input())
data = input()
cars = deque()

total_cars = 0
is_valid = True
duration_green_light_new = duration_green_light
while not data == 'END':
    if not data == 'green':
        cars.append(data)
    else:
        duration_green_light = duration_green_light_new
        while cars:
            current_car = cars.popleft()
            for ch in current_car:
                duration_green_light -= 1
                if duration_green_light < 0:
                    duration_free_window -= 1
                    if duration_free_window < 0:
                        print("A crash happened!")
                        print(f"{current_car} was hit at {ch}.")
                        is_valid = False
                        break
            if not is_valid:
                break
            total_cars += 1
            if duration_green_light < 0:
                break

    data = input()

if is_valid:
    print("Everyone is safe.")
    print(f"{total_cars} total cars passed the crossroads.")

