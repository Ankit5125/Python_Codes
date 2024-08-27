'''
create a class to store 2 complex number
print their sum and product
'''

class comp:
    inc = "+"
    mult = "*"
    
    def __init__(self,i,j):
        self.i = i
        self.j = j
        self.num = complex(i,j)
        
    def operator(self,str):
        if str is inc :
            self.increase()
        else :
            self.multiply()
    
    def printsum(self):
        i = int(input("Enter i : "))
        j = int(input("Enter j : "))
        num2 = complex(i,j)
        return self.num + num2
        
    def multiply(self):  
        i = int(input("Enter i : "))
        j = int(input("Enter j : "))
        num2 = complex(i,j)
        return self.num * num2
        
i = int(input("Enter i : "))
j = int(input("Enter j : "))

c = comp(i,j)
print("Sum =" , c.printsum())
print("Multiplication =", c.multiply())
