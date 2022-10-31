my_list = ["@F1", "O@BCD", "!", "@F2", "ADDAB", "!", "@F3", "OKKA", "!"]
result = {}
index = 0
while index < len(my_list):
    if my_list[index][0] == '@':
        result[my_list[index]] = my_list[index+1]
        index += 1
    index += 1
print(result)
