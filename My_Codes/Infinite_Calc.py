i = True ;

while i :
    want_to_go_ahead = input("\n1 -> Go Ahead , 0 -> Exit : ")
    if int(want_to_go_ahead) == 1:
        num1 = input("Enter Number1 : ")
        num2 = input("Enter Number2 : ")

        print("\nEnter Operation :")
        print("+ -> Add")
        print("- -> Subtract")
        print("* -> Multiplication")
        print("/ -> Devision")
        print("% -> Reminder")

        print("\nEnter Choice : ")
        choice = input()

        if choice == '+':
            print("\nSum = ", int(num1) + int(num2))

        elif choice == '-':
            print("\nSubtract = ", int(num1) - int(num2))

        elif choice == '*':
            print("\nMultiplication = ", int(num1) * int(num2))

        elif choice == '/' or choice == '%' :
            if int(num2) == 0:
                print("\nCannot Devide by 0")
            else:    
                if(choice == '%'):
                    print("\nReminder = " , int(num1) % int(num2))
                else:
                    convert_or_not = input("\nDo You want to Make it Int ? \nY -> Yes , N -> No : ")
                    if convert_or_not.upper() == 'y' or convert_or_not.upper() == 'Y':
                        print("\nDevision = " , int(num1) // int(num2))
                    else:
                        print("\nDevision = ", int(num1) / int(num2))
            
        else:
            print("\nEnter Propper Symbol...\n")
    
    elif int(want_to_go_ahead) == 0 :
        i = False
        
    else:
        print("\nEnter Proper Decision...\n")      
