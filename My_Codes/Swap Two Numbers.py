num1 = int(input("Entr Number 1 : "))
num2 = int(input("Entr Number 2 : "))

print(f"Before : \nNum1 :{num1} \tNum2 :{num2}")

# temp = num1
# num1 = num2 
# num2 = temp 

num1 = num1 + num2 
num2 = num1 - num2
num1 = num1 - num2

print(f"After : \nNum1 :{num1} \tNum2 :{num2}")
