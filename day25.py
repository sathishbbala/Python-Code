with open("file1.txt", "r") as file1:
    list1 = [int(line.strip()) for line in file1]
print(list1)

with open("file2.txt", "r") as file2:
    list2 = [int(line.strip()) for line in file2]
print(list2)

common_list = [num for num in list1 if num in list2]
print(common_list)

#
# [3, 6, 5, 8, 33, 12, 7, 4, 72, 2, 42, 13]
# [3, 6, 13, 5, 7, 89, 12, 3, 33, 34, 1, 344, 42]