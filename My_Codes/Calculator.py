num1 = input("Enter Number1 : ")
num2 = input("Enter Number2 : ")

print("\nEnter Operation :")
print("+ -> Add")
print("- -> Subtract")
print("* -> Multiplication")
print("/ -> Devision")
print("% -> Reminder")

print("Enter Choice : ")
choice = input()

if choice == '+':
    print("Sum = ", int(num1) + int(num2))

elif choice == '-':
    print("Subtract = ", int(num1) - int(num2))

elif choice == '*':
    print("Multiplication = ", int(num1) * int(num2))

elif choice == '/' or choice == '%' :
    if int(num2) == 0:
        print("Cannot Devide by 0")
    else:    
        if(choice == '%'):
            print("Reminder = " , int(num1) % int(num2))
        else:
            convert_or_not = input("Do You want to Make it Int ? \nY -> Yes , N -> No : ")
            if convert_or_not.upper() == 'Y':
                print("Devision = " , int(num1) // int(num2))
            else:
                print("Devision = ", int(num1) / int(num2))
            
else:
    print("Enter Propper Symbol...\n")
