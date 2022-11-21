import numpy as np

py_list = [1, 2, 36, 56, 49, 84]

np_array = np.array(py_list)
five_zeros = np.zeros(5)
ten_ones = np.ones(10)
sequence = np.arange(16)
stepper = np.arange(0, 51, 5)
spaced = np.linspace(0, 10, num=3)

two_d = np.array([[1, 2], [6, 5], [4, 3], ])

shaped = np_array.reshape(3, 2)
changed = np.flip(shaped)
add = two_d + changed
back_to_one = add.flatten().sum()
# print(back_to_one)
# print(two_d.shape)
# print(two_d.dtype)
print(two_d)
print(np.sort(two_d))
