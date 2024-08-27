class calc:
    def __init__(self,num):
        self.num = num
    
    def sqr(self):
        return self.num ** 2
    
    def cube(self):
        return self.num ** 3
    
    def sqrt(self):
        return self.num ** 0.5

num1 = int(input("Enter Number 1 : "))
num2 = int(input("Enter Number 2 : "))

n1 = calc(num1)
n2 = calc(num2)

print(n1.sqr(), n1.cube(), n1.sqrt())
print(n2.sqr(), n2.cube(), n2.sqrt())
