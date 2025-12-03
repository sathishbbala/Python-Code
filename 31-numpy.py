import numpy as np

# Rows = days, Columns = cities
temps = np.array([
    [30, 32, 35],
    [31, 33, 36],
    [29, 31, 34],
    [28, 30, 33],
    [32, 34, 37],
    [33, 35, 38],
    [31, 36, 39]
])

print(temps.shape) # prints the array rows x columns 7 x 3

city_avg = np.mean(temps, axis=0) # axis=0 down rows per city 3 values
print(city_avg)

daily_avg = np.mean(temps, axis=1) # axis = 1 across columns per day 7 values
print(daily_avg) 

max_temp = np.max(temps)
print(max_temp) # Highest recorded temperature

min_per_city = np.min(temps, axis=0)
print(min_per_city) # 3 values 

calibrated = temps + 1.5 #vectorization add 1.5 to all elements
print(calibrated) # new array with 1.5 added to all values

above_35 = temps > 35
print(above_35) #Boolean Matrix

hot_days = np.any(temps > 35, axis=1)
print(hot_days) # output 7 values 1 value per day either true or false

min_val = temps.min()
max_val = temps.max()

normalized = (temps - min_val) / (max_val - min_val)
print(normalized)

# Find average temperature per day
avg_temp = np.average(temps, axis=1)
print(avg_temp)

#Count how many values are > 34°C
count_above_34 = np.sum(temps > 34)
print(count_above_34)

#Replace all temperatures < 30 with 30
temps_fixed = temps.copy()
temps_fixed[temps < 30] = 30
print(temps_fixed)

#Find the city index with highest average temperature
avg_city_temp = np.average(temps, axis=0)
print(avg_city_temp.max())
city_index = np.argmax(avg_city_temp)
print(city_index)
