import pandas
data = pandas.read_csv('data/Squirrel_Data.csv')
print(data['Primary Fur Color'])
print(data[data['Primary Fur Color']])
print(data)
# count = len(data[data['ColumnName'] == 'Value'])
# This is a classic Pandas filtering + counting pattern:
gray_squirrel_count = len(data[(data['Primary Fur Color']) == 'Gray'])
red_squirrel_count = len(data[(data['Primary Fur Color']) == 'Cinnamon'])
black_squirrel_count = len(data[(data['Primary Fur Color']) == 'Black'])

print(gray_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)

data_dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [gray_squirrel_count, red_squirrel_count, black_squirrel_count]}

df = pandas.DataFrame(data_dict)
df.to_csv('data/squirrel_count.csv')