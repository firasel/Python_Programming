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
marks.clear()
print(marks)
