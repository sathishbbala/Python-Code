import csv
import pandas


#with open('test.txt', 'r') as file:
#    content = file.read()
#    print(content)

#with open('test.txt', 'w') as file:
#    file.write('This is a test file for python code test #3\n')

#with open('weather_data.csv', 'r') as data_file:
#    data = csv.reader(data_file)
#    temperatures = []
#    for row in data:
#        if row[1] != 'temp':
#            temperatures.append(int(row[1]))
#    print(temperatures)

data = pandas.read_csv('weather_data.csv')  
print(type(data))
print(type(data['temp']))
temp_list = data['temp'].to_list()
print(temp_list)
print(len(temp_list))
print(data['temp'].mean())
print(data['temp'].max())
print(data[data.temp == data.temp.max()])
print(data['temp'].mean())

