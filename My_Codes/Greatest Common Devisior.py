
num1 = int(input("Enter Number 1 : "))
num2 = int(input("Enter Number 2 : "))

max = 1 

for i in range(1,min(num1,num2)+1):
    if (num1 / i is int) and (num2 / i is int):
        max = i

print(max)