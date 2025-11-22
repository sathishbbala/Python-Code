import pandas as pd

df = pd.read_csv("data/salaries_by_college_major.csv")
print(df.tail())

#x,y = 12,15
#result = y if x&1 == 0 else x
#print(result)

x=12
print(x&1)
if x&1 == 0:
    print("12")
else:
    print("15")
