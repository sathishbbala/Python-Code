def add(*args):
    print(type(args))
    print(args)
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(3,4,5,6,7,9,10,12,4,67,96))
# Note that args is a tuple while kwargs is a dict
x = "5"
print(type(x))
print(int(x))
print(type(int(x)))

categories = ["Travel","Meals","Accommodation","Software","Hardware","Training","Taxi","Internet","Office Supplies","Team Event"]
for category_name in categories:
    print(category_name)

x=['1','2','3']
y=['4','5']
print(x+y)
