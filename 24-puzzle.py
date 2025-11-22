class Num:
    def __init__(self, x):
        self.x = x 
    def __truediv__(self, other):
        return(Num(self.x - other.x))
    
    
n1 = Num(10)
n2 = Num(4)
print(f"n1 = {n1.x} and n2 = {n2.x}")
print((n1/n2).x)
