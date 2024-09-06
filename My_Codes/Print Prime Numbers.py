def isPrime(num):
    if num == 1 or num == 2 :
        return True
    else :
        for i in range (2,int(num/2)):
            if num % i == 0 :
                return False
        
        return True           

for i in range(1,20) :
    print(f"{i} -> {isPrime(i)}")
