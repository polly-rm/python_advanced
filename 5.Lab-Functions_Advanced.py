# 1.Absolute Value
# def absolute_values(nums):
#     result = [abs(num) for num in nums]
#     return result
#
# numbers = [float(el) for el in input().split()]
# print(absolute_values(numbers))

# 2.Rounding
# def round_numbers(nums):
#     result = [round(num) for num in nums]
#     return result
#
# numbers = [float(el) for el in input().split()]
# print(round_numbers(numbers))


# 3.Multiplication Function
# def multiply(*args):
#     prod = 1
#     for el in args:
#         prod *= el
#     return prod

# 3.Second Way
# from functools import reduce
# def multiply(*args):
#     return reduce(lambda x, y: x * y, args)
#
# print(multiply(1, 4, 5))

# 4.Operate
# from functools import reduce
# mapper = {
#     "+": lambda x,y: x+y,
#     "-": lambda x,y: x-y,
#     "*": lambda x,y: x*y,
#     "/": lambda x,y: x/y
# }
#
# def operate(operator, *args):
#     return reduce(mapper[operator], args)
#
# print(operate("+", 1, 2, 3))

# 5.Person Info
# def get_info(**kwargs):
#     return f"This is {kwargs.get('name')} from {kwargs.get('town')} and he is {kwargs.get('age')} years old"


# 6.Character Combination
# from itertools import permutations
# text = list(input())
# result = [f"{''.join(el)}" for el in list(permutations(text))]
# for el in result:
#     print(el)


# 7.Chairs
# from itertools import combinations
# names = input().split(', ')
# n = int(input())
# result = [f"{', '.join(el)}" for el in list(combinations(names, n))]
# for el in result:
#     print(el)

# 8.Expressions
def expressions(nums, current_sum=0, expression=""):
    if not nums:
        return [(expression, current_sum)]
    result_plus = expressions(nums[1:], current_sum+nums[0], f"{expression}+{nums[0]}")
    result_minus = expressions(nums[1:], current_sum-nums[0], f"{expression}-{nums[0]}")
    return result_plus + result_minus

nums=[int(el) for el in input().split(', ')]
print(*[f"{el[0]}={el[1]}" for el in expressions(nums)], sep="\n")