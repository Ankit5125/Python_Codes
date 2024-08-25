num = int(input("Enter Number : "))

if num == 0:
    print("Prime")
else:
    for i in range (2,int(num/2 + 1)) :
        if num % i == 0 :
            print("Not Prime")
            exit()
        print("Prime")
