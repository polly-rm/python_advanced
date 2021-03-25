# 1.Even Numbers
# def find_even_numbers(nums):
#     return list(filter(lambda x: x % 2 == 0, nums))
#
# numbers = [int(el) for el in input().split()]
# print(find_even_numbers(numbers))

# 2.Sort
# def sort_list_numbers(nums):
#     return sorted(nums)
#
# numbers = [int(el) for el in input().split()]
# print(sort_list_numbers(numbers))

# 3.Min Max and Sum
# def min_max_sum(nums):
#     min_num = min(nums)
#     max_num = max(nums)
#     sum_nums = sum(nums)
#     return (min_num, max_num, sum_nums)
#
# numbers = [int(el) for el in input().split()]
# print(f"The minimum number is {min_max_sum(numbers)[0]}")
# print(f"The maximum number is {min_max_sum(numbers)[1]}")
# print(f"The sum number is: {min_max_sum(numbers)[2]}")


# 4.Negative vs Positive
# def find_negative_positive(nums):
#     list_positive = list(filter(lambda x: x >= 0, nums))
#     list_negative = list(filter(lambda x: x < 0, nums))
#     return (sum(list_positive), sum(list_negative))
#
# numbers = [int(el) for el in input().split()]
# print(find_negative_positive(numbers)[1])
# print(find_negative_positive(numbers)[0])
# if abs(find_negative_positive(numbers)[1]) > find_negative_positive(numbers)[0]:
#     print("The negatives are stronger than the positives")
# else:
#     print("The positives are stronger than the negatives")


# 5.Odd or Even
# def odd_even(nums):
#     list_odd = list(filter(lambda x: x % 2 == 1, nums))
#     list_even = list(filter(lambda x: x % 2 == 0, nums))
#     result_odds = sum(list_odd) * len(nums)
#     result_evens = sum(list_even) * len(nums)
#     return (result_odds, result_evens)
#
# command = input()
# numbers = [int(el) for el in input().split()]
# if command == "Odd":
#     print(odd_even(numbers)[0])
# elif command == "Even":
#     print(odd_even(numbers)[1])

# 6.Arguments Length
# def args_length(*args):
#     return len(args)
# print(args_length(1, 32, 5))


# 7.Concetanate
# def concatenate(*args):
#     return f"{''.join(args)}"
# print(concatenate("Soft", "Uni", "Is", "Great", "!"))

# 8.Even or Odd
# def even_odd(*args):
#     command = args[-1]
#     if command == "even":
#         return list(filter(lambda x: x % 2 == 0, args[0:-1]))
#     return list(filter(lambda x: x % 2 == 1, args[0:-1]))

# 9.Function Executor
# def func_executor(*args):
#     result = []
#     for func_name, data in args:
#         result.append(func_name(*data))
#     return result

# 10.Keyword Argument Length
# def kwargs_length(**kwargs):
#     return len(kwargs)


# 11.Age Assignment
# def age_assignment(*args, **kwargs):
#     names_ages = {}
#     for name in args:
#         for key in kwargs:
#             if name.startswith(key):
#                 names_ages[name] = kwargs[key]
#
#     return names_ages
#
# print(age_assignment("Peter", "George", G=26, P=19))


# 12.Recursion Palindrome
# def palindrome(word, index):
#     if word == word[::-1]:
#         return f"{word} is a palindrome"
#     else:
#         return f"{word} is not a palindrome"
#
# print(palindrome("peter", 0))


# 13.Recursive Power
# def recursive_power(number, power):
#     if power == 1:
#         return number
#     return number * recursive_power(number, power-1)