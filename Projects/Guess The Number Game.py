import random

def play():
    guess = random.randint(1,100)
    count = 0 
    
    while True : 
        prompt = int(input("\nEnter Your Guesed Number : "))
        
        if prompt == guess :
            print("\nCongratulations !!\n You Found Answer in : ", count, "Attempts\n")
            break
            
        else :
            print("Wrong Answer...")
            
            if prompt > guess :
                print("Hint : Guess Small Number...\n")
            
            else :
                print("Hint : Guess Bigger Number...\n")
            
            count+=1

while True :
    go_ahead = int(input("\n\nEnter Choice : \n 1 - > Play Ahead\n 0 -> Exit \nChoice : "))
    
    if go_ahead == 1 :
        play()
        
    elif go_ahead == 0 :
        print("\nThank You...\n")
        exit()
        
    else :
        print("\nPlease Enter Valid Choice...\n")