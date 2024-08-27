import random

ls = []

for i in range(10):
    ls.append(random.randint(0,100))

num = int(input("Enter Number : "))

for number in ls:
    if number < num :
        print(f"{number} is greater than {num}")
        exit()

print(ls)
print(num)
print("Number Smaller than all the elements")