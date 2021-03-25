# 1.Count Same Values
# values = tuple(map(float, input().split()))
# values_counts = {}
# for value in values:
#     if not value in values_counts:
#         values_counts[value] = 1
#     else:
#         values_counts[value] += 1
#
# for value, count in values_counts.items():
#     print(f'{value} - {count} times')


# 2.Average Student Grades
# n = int(input())
# students_grades = {}
# for _ in range(n):
#     student, grade = input().split()
#     grade = float(grade)
#     if not student in students_grades:
#         students_grades[student] = [grade]
#     else:
#         students_grades[student].append(grade)
#
# for (student, grades) in students_grades.items():
#     average = sum(grades) / len(grades)
#     grades_string = ' '.join(map(lambda grade: f'{grade:.2f}', grades))
#     print(f'{student} -> {grades_string} (avg: {average:.2f})')


# 3.Record Unique Names
# n = int(input())
# names = set()
# for _ in range(n):
#     name = input()
#     names.add(name)
#
# for name in names:
#     print(name)


# 4.Parking Lot
# n = int(input())
# cars_in = set()
# for _ in range(n):
#     command, car = input().split(', ')
#     if command == 'IN':
#         cars_in.add(car)
#     else:
#         cars_in.remove(car)
#
# if cars_in:
#     for car in cars_in:
#         print(car)
# else:
#     print('Parking Lot is Empty')


# 5.Soft Uni Party
# n = int(input())
# reservations = set()
# guests_who_came = set()
# for _ in range(n):
#     reserv_number = input()
#     reservations.add(reserv_number)
#
# guest = input()
# while not guest == "END":
#     guests_who_came.add(guest)
#     guest = input()
#
# guests_who_didnt_come = reservations - guests_who_came
# print(len(guests_who_didnt_come))
# vip_guests = []
# regular_guests = []
# for guest in guests_who_didnt_come:
#     if guest[0].isdigit():
#         vip_guests.append(guest)
#     else:
#         regular_guests.append(guest)
#
# for guest in sorted(vip_guests):
#     print(guest)
# for guest in sorted(regular_guests):
#     print(guest)

