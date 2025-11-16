def add(*args):
    print(type(args))
    print(args)
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(3,4,5,6,7,9,10,12,4,67,96))

# Note that args is a tuple while kwargs is a dict
