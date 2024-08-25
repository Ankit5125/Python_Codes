def see():
    num1 = int(input("Enter Number 1 :"))
    num2 = int(input("Enter Number 2 :"))
    num3 = int(input("Enter Number 3 :"))
    
    if(num1 > num2 and num1 > num3):
        print(f"Largest = {num1}")
    elif(num1 < num2 and num2 > num3):
        print(f"Largest = {num2}")
    else:
        print(f"Largest = {num3}")    
        
        
n = int(input("How many Time You want to Check ? : "))

for i in range(n):
    print(f"Calling {i+1} : ")
    see()