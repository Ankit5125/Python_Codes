class nums():
    num1 = 0
    num2 = 0

    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def check():
        if num1 is int and num2 is int:
            return True
        else :
            return False
num1 = int(input("Enter Number 1 : "))
num2 = int(input("Enter Number 2 : "))

cls = nums(num1,num2)
print(cls.check())