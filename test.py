
my_dict = { 'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("Value : %s" %  my_dict.items())

# Sort by values
sorted_by_keys = dict(sorted(my_dict.items(), key=lambda item: item[0]))
print(sorted_by_keys)
