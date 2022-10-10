numbers = [12, 34, 45, 12, 45, 78, 89, 90]

print(numbers[1])
print(numbers[-6])
print(numbers[5:-1])
print(numbers)
# Set
nums = {12, 34, 45, 12, 45, 78, 89, 90}
nums2 = set(numbers)
print(nums)
print(nums2)

nums_tuple = 12, 34, 45, 12, 45, 78, 89, 90
print(nums_tuple)

# Dictionary
marks = {'physics': 12, 'chemistry': 45, 'math': 56}
marks['math'] = 57
marks['english'] = 65
print(marks)
marks_keys = marks.keys()
marks_values = marks.values()
print(marks_keys)
print(marks_values)
# marks.clear()
print(marks)

print(sum(numbers))

for mark in marks:
    print(mark)

for i, num in enumerate(numbers):
    print(i, num)


def square(x): return x*x


def double_it(x): return x*2


print(square(5))
print(double_it(4))
double_numbers = map(double_it, numbers)
double_numbers2 = list(map(lambda x: x*x, numbers))
print(list(double_numbers))
print(double_numbers2)

bigger_numbers = list(filter(lambda x: x > 1000, double_numbers2))
print(bigger_numbers)
print(max(bigger_numbers))
print(min(bigger_numbers))
print(list(reversed(bigger_numbers)))

numbers_iter = iter(bigger_numbers)
print(next(numbers_iter))
print(next(numbers_iter))
print(next(numbers_iter))
print(next(numbers_iter))
