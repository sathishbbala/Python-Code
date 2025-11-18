import random, pandas
names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan', 'Fiona', 'George', 'Hannah']
students_scores = {name: random.randint(0, 100) for name in names}
print(students_scores)
# new_dict = {key: value for key, value in original_dict.items() if condition}
passed_students = {name:score for name, score in students_scores.items() if score >= 60}
print(passed_students)

sentence = "The quick brown fox jumps over the lazy dog!!"
words = sentence.split()
word_length = {word: len(word) for word in words}
print(word_length)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {key:(value * 9/5) + 32 for key, value in weather_c.items()}
print(weather_f)

# Looping through a dictionary
for day, temp in weather_c.items():
    print(f"On {day}, the temperature is {temp}°C") 
for day, temp in weather_f.items():
    print(temp)

weather_dict = {
    "day":["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "temp_c":[12, 14, 15, 14, 21, 22, 24]
}

weather_df = pandas.DataFrame(weather_dict)
# print(weather_df)

# Loop through rows of a DataFrame
for index, row in weather_df.iterrows():
    print(row.temp_c)
