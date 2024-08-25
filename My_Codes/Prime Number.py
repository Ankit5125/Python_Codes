num = int(input("Enter Number : "))

for i in range (2,int(num/2 + 1)) :
    if num % i == 0 :
        print("Not Prime")
        exit()
        
print("Prime")        
