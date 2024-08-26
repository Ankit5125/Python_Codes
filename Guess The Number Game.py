import random

guess = random.randint(1,100)
count = 0 

while True : 
    prompt = int(input("Enter Your Guesed Number : "))

    if prompt == guess :
        print("Congratulations !!\n You Found Answer in : ", count, "Attempts")
        exit()
    
    else :
        print("Wrong Answer...")
        if prompt > guess :
            print("Hint : Guess Small Number...")
        else :
            print("Hint : Guess Bigger Number...")
        count+=1